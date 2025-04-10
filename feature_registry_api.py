from flask import Flask, jsonify
from featureform import Client
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
import json
import traceback

app = Flask(__name__)
client = Client(insecure=True)

@dataclass
class Feature:
    name: str
    variant: str

@dataclass
class Label:
    name: str
    variant: str

@dataclass
class TrainingSet:
    name: str
    variant: str

@dataclass
class Tag:
    key: str
    value: str

@dataclass
class Entity:
    name: str
    features: List[Feature]
    labels: List[Label]
    training_sets: List[TrainingSet]
    tags: List[Tag]
    properties: Dict[str, str]

    @classmethod
    def from_featureform_entity(cls, entity) -> 'Entity':
        """Create an Entity from a Featureform entity object"""
        try:
            # Extract name
            name = entity.name
            
            # Extract features
            features = []
            try:
                for feature in entity.features:
                    features.append(Feature(
                        name=feature.name,
                        variant=feature.variant
                    ))
            except Exception as e:
                print(f"Error extracting features: {str(e)}")
                features = []
            
            # Extract labels
            labels = []
            try:
                for label in entity.labels:
                    labels.append(Label(
                        name=label.name,
                        variant=label.variant
                    ))
            except Exception as e:
                print(f"Error extracting labels: {str(e)}")
                labels = []
            
            # Extract training sets
            training_sets = []
            try:
                for ts in entity.training_sets:
                    training_sets.append(TrainingSet(
                        name=ts.name,
                        variant=ts.variant
                    ))
            except Exception as e:
                print(f"Error extracting training sets: {str(e)}")
                training_sets = []
            
            # Extract tags
            tags = []
            try:
                for tag in entity.tags:
                    tags.append(Tag(
                        key=tag.key,
                        value=tag.value
                    ))
            except Exception as e:
                print(f"Error extracting tags: {str(e)}")
                tags = []
            
            # Extract properties
            properties = {}
            try:
                for key, value in entity.properties.items():
                    properties[key] = value
            except Exception as e:
                print(f"Error extracting properties: {str(e)}")
                properties = {}
            
            return cls(
                name=name,
                features=features,
                labels=labels,
                training_sets=training_sets,
                tags=tags,
                properties=properties
            )
        except Exception as e:
            print(f"Error in from_featureform_entity: {str(e)}")
            print(traceback.format_exc())
            # Return a minimal entity with the name if available
            try:
                name = entity.name
            except:
                name = "unknown"
            return cls(
                name=name,
                features=[],
                labels=[],
                training_sets=[],
                tags=[],
                properties={}
            )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "features": [asdict(feature) for feature in self.features],
            "labels": [asdict(label) for label in self.labels],
            "training_sets": [asdict(ts) for ts in self.training_sets],
            "tags": [asdict(tag) for tag in self.tags],
            "properties": self.properties
        }

@app.route('/api/entities', methods=['GET'])
def list_entities():
    """List all entities in the feature registry"""
    try:
        entities = client.list_entities()
        # Convert entities to structured format using our dataclasses
        structured_entities = []
        for entity in entities:
            try:
                structured_entity = Entity.from_featureform_entity(entity).to_dict()
                structured_entities.append(structured_entity)
            except Exception as e:
                print(f"Error processing entity: {str(e)}")
                print(traceback.format_exc())
                # Add a minimal entity with just the name if possible
                try:
                    structured_entities.append({"name": str(entity)})
                except:
                    structured_entities.append({"name": "unknown"})
        
        return jsonify({
            "status": "success",
            "entities": structured_entities
        })
    except Exception as e:
        print(f"Error in list_entities: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/entities/<entity_name>', methods=['GET'])
def get_entity_by_name(entity_name: str):
    """Get a specific entity by name"""
    try:
        # Directly get the entity by name
        entity = client.get_entity(entity_name)
        
        if entity is None:
            return jsonify({
                "status": "error",
                "message": f"Entity with name '{entity_name}' not found"
            }), 404
        
        # Print entity details for debugging
        print(f"Entity type: {type(entity)}")
        print(f"Entity dir: {dir(entity)}")
        print(f"Entity str: {str(entity)}")
        
        # Convert to structured format using our dataclass
        try:
            structured_entity = Entity.from_featureform_entity(entity).to_dict()
        except Exception as e:
            print(f"Error converting entity: {str(e)}")
            print(traceback.format_exc())
            return jsonify({
                "status": "error",
                "message": f"Error converting entity: {str(e)}",
                "entity_raw": str(entity)
            }), 500
        
        return jsonify({
            "status": "success",
            "entity": structured_entity
        })
    except Exception as e:
        print(f"Error in get_entity_by_name: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 