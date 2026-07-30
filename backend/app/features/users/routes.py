from flask import Blueprint

users_bp = Blueprint(
    'users',
    __name__,
)

@users_bp.get('/')
def get_users():
    return {
        "message": "Users Endpoint"
    }