from flask import Blueprint

courses_bp = Blueprint(
    "programs",
    __name__,
)

@courses_bp.get("/")
def get_programs():
    return {
        "message": "Programs Endpoint"
    }