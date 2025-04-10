from featureform import Client
from models.entity import Entity
import traceback

class EntityService:
    def __init__(self):
        self.client = Client(insecure=True)
    
    def list_entities(self):
        """List all entities in the feature registry"""
        try:
            entities = self.client.list_entities()
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
            
            return structured_entities
        except Exception as e:
            print(f"Error in list_entities: {str(e)}")
            print(traceback.format_exc())
            raise
    
    def get_entity_by_name(self, entity_name: str):
        """Get a specific entity by name"""
        try:
            # First list all entities and find the one we want
            entities = self.client.list_entities()
            target_entity = None
            
            for entity in entities:
                if entity.name == entity_name:
                    target_entity = entity
                    break
            
            if target_entity is None:
                return None
            
            # Print entity details for debugging
            print(f"Entity type: {type(target_entity)}")
            print(f"Entity dir: {dir(target_entity)}")
            print(f"Entity str: {str(target_entity)}")
            
            # Convert to structured format using our dataclass
            try:
                structured_entity = Entity.from_featureform_entity(target_entity).to_dict()
                return structured_entity
            except Exception as e:
                print(f"Error converting entity: {str(e)}")
                print(traceback.format_exc())
                return {"name": entity_name, "raw": str(target_entity)}
        except Exception as e:
            print(f"Error in get_entity_by_name: {str(e)}")
            print(traceback.format_exc())
            raise 