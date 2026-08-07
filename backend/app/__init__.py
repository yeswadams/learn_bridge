# Application Factory
from flask import Flask

# config
from app.core.config import DevelopmentConfig
from app.extensions import db
from app.extensions import ma 
from app.extensions import migrate

#blue prints
from app.features.courses.routes import courses_bp
from app.features.users.routes import users_bp
from app.core.health.routes import health_bp

def register_bp(app):
    app.register_blueprint(
        courses_bp, 
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
    

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    import app.features

    migrate.init_app(app, db)

    ma.init_app(app)

    register_bp(app)
    return app
