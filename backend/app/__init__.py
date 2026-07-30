# Application Factory

from flask import Flask
from app.features.programs.routes import programs_bp
from app.features.users.routes import users_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(
        programs_bp, 
        users_bp,
        url_prefix="/api/vi/programs"
    )

    @app.get('/')
    def index():
        return {
            "message": "Learn Bridge API is Running"
        }
    return app
