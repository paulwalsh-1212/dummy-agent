from flask import Flask
from flask_cors import CORS

# Initialize SQLAlchemy

def create_app():
    app = Flask(__name__)
    
    # Initialize CORS with default options (allows all origins)
    CORS(app, resources={
        r"/api/*": {
            "origins": app.config.get('CORS_ORIGINS', "*"),
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Initialize database with app

    from app.api.routes.agents import agents_bp
    
    app.register_blueprint(agents_bp, url_prefix='/api')
    return app
