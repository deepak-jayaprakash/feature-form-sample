from flask import Blueprint, jsonify
from services.entity_service import EntityService

# Create a Blueprint for entity routes
entity_bp = Blueprint('entity', __name__)
entity_service = EntityService()

@entity_bp.route('/api/entities', methods=['GET'])
def list_entities():
    """List all entities in the feature registry"""
    try:
        entities = entity_service.list_entities()
        return jsonify({
            "status": "success",
            "entities": entities
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@entity_bp.route('/api/entities/<entity_name>', methods=['GET'])
def get_entity_by_name(entity_name: str):
    """Get a specific entity by name"""
    try:
        entity = entity_service.get_entity_by_name(entity_name)
        
        if entity is None:
            return jsonify({
                "status": "error",
                "message": f"Entity with name '{entity_name}' not found"
            }), 404
        
        return jsonify({
            "status": "success",
            "entity": entity
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500 