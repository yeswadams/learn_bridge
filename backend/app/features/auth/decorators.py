#the decorator that is to help in role based access within the app

from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.extensions.database import db
from app.features.auth.models import User, UserRole

def roles_required(*allowed_roles: UserRole):
    """Generic role-based accross control decorator"""
    def decorator(f):
        @wraps(f)
        @jwt_required()

        def decorated_function(*args, **kwargs):
            current_user_id = get_jwt_identity()
            #query the db
            user = db.session.get(User, current_user_id)

            # Safety Check: is the user actually an admin?
            if not user:
                return jsonify({
                    "error": "User account not found."
                }), 404
            
            return f(*args, **kwargs)

        return decorated_function
    return decorator

def admin_required():
    """Custom shortcut decorator for admin role"""
    return roles_required(UserRole.ADMINISTRATOR)

def instructor_required():
    """Custom decorator to restrict endpoint access to accounts with instructor privilleges"""
    return roles_required(UserRole.INSTRUCTOR)

def student_required():
    """Custom decorator to ensure student access only"""
    return roles_required(UserRole.STUDENT)
    


