# Featureform Entity Management API

This is a Flask-based REST API for managing entities in Featureform. The API provides endpoints for creating, retrieving, and managing entities with their associated features.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
Create a `.env` file with the following variables:
```
FEATUREFORM_HOST=your_featureform_host
FEATUREFORM_PORT=your_featureform_port
```

3. Run the application:
```bash
python app.py
```

The server will start on `http://localhost:8080`

## API Endpoints

### Entities

- `POST /api/entities` - Create a new entity
- `GET /api/entities` - List all entities
- `GET /api/entities/<entity_id>` - Get entity details
- `PUT /api/entities/<entity_id>` - Update entity
- `DELETE /api/entities/<entity_id>` - Delete entity

### Features

- `POST /api/entities/<entity_id>/features` - Add a feature to an entity
- `GET /api/entities/<entity_id>/features` - List features for an entity
- `DELETE /api/entities/<entity_id>/features/<feature_id>` - Remove a feature from an entity

## Project Structure

```
.
├── app.py                 # Main Flask application
├── controllers/           # API route controllers
│   └── entity_controller.py
├── services/             # Business logic
│   └── entity_service.py
├── models/              # Data models
│   └── entity.py
├── utils/              # Utility functions
│   └── featureform_client.py
└── requirements.txt    # Python dependencies
```

