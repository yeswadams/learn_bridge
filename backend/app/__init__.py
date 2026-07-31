# Application Factory
from flask import Flask

# config
from app.core.config import DevelopmentConfig

#blue prints
from app.features.programs.routes import programs_bp
from app.features.users.routes import users_bp
from app.core.health.routes import health_bp

def register_bp(app):
    app.register_blueprint(
        programs_bp, 
        url_prefix="/api/v1/programs"
    )
    app.register_blueprint(
        users_bp, 
        url_prefix="/api/v1/users"
    )
    app.register_blueprint(
        health_bp, 
        url_prefix="/api/v1/health"
    )
    

def create_app():
    app = Flask(__name__)

    app.config.from_object(
        DevelopmentConfig
    )

    register_bp(app)
    return app
