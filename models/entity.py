from dataclasses import dataclass, asdict
from typing import List, Dict, Optional

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
            import traceback
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