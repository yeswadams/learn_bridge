from flask import Blueprint

health_bp = Blueprint("health", __name__)

@health_bp.get("/")
def health_status():
    return {
        "status": "ok",
        "service": "Learn Bridge API"
    }