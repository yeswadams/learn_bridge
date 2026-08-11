# Application Factory
from flask import Flask
# config
from app.core.config import DevelopmentConfig
from app.extensions import db, ma, migrate, jwt
#blue prints
from app.features.courses.routes import courses_bp
from app.features.auth.routes import auth_bp
from app.core.health.routes import health_bp

def register_bp(app):
    app.register_blueprint(
            health_bp, 
            url_prefix="/api/v1/health"
    )
    app.register_blueprint(
        courses_bp, 
        url_prefix="/api/v1/programs"
    )
    app.register_blueprint(
        auth_bp, 
        url_prefix="/api/v1/users"
    )
    
    

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    # register bps
    register_bp(app)
    return app
