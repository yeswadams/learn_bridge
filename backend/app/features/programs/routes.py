from flask import Blueprint

programs_bp = Blueprint(
    "programs",
    __name__,
)

@programs_bp.get("/")
def get_programs():
    return {
        "message": "Programs Endpoint"
    }