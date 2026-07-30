from flask import Blueprint

health_bp = Blueprint("health", __name__)

@health_bp.get("/")
def index():
    return {
        "message": "Learn Bridge API is Running"
    }

@health_bp.get("/status")
def health_status():
    return {
        "status": "ok",
        "service": "Learn Bridge API"
    }