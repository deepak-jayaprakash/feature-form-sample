from flask import Flask
from controllers.entity_controller import entity_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(entity_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 