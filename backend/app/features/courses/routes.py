from flask import Blueprint

courses_bp = Blueprint(
    "programs",
    __name__
)

@courses_bp.get("/")
def get_courses():
    return {
        "message": "Programs Endpoint"
    }