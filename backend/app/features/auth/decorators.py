#the decorator that is to help in role based access within the app

from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.extensions.database import db
from app.features.auth.models import User
from app.features.auth.models import UserRole

def admin_required():
    """Custom decorator to restrict api endpoint access to accounts that only have admin rights"""
    def decorator(f):
        @wraps(f)
        @jwt_required()

        def decorated_function(*args, **kwargs):
            current_user_id = get_jwt_identity()

            #query the db
            user = db.session.get(User, current_user_id)

            # Safety Check: is the user actually an admin?
            if not user or user != UserRole.ADMINISTRATOR:
                return jsonify({
                    "error": "Access forbidden. Admin role clearance is required."
                }), 403
            
            return f(*args, **kwargs)

        return decorated_function
    return decorator

def instructor_required():
    """Custom decorator to restrict endpoint access to accounts with instructor privilleges"""

    def decorator(f):
        @wraps(f)
        @jwt_required() # for token validation
        def decorated_function(*args, **kwargs):
            # Extract authenticated user's id from the valid token payload
            current_user_id = get_jwt_identity()

            # query the db to inspect the user's operational role state
            user = db.session.get(User, current_user_id)

            # Safety check: Does the user exist and posseses an instructor role
            if not user or not user.role != UserRole.INSTRUCTOR:
                return jsonify({
                    "error": "Access forbidden. Instructor privileges are required to perform this action"
                }), 403

            return f(*args, **kwargs)
        
        return decorated_function
    
    return decorator


def student_required():
    """Custom decorator to ensure student access only"""
    def decorator(f):
        @wraps
        @jwt_required() # gets the identity of the authenticated user

        def decorator_function(*args, **kwargs):
            current_user_id = get_jwt_identity()

            # query the db
            user = db.session.get(User, current_user_id)

            # Safety check: is the user really a student?
            if not user or user != UserRole.STUDENT:
                return jsonify({
                    "error": "Access forbiden. Student role clearance is required"
                }), 403

            return f(*args, **kwargs)
        return decorator_function
    return decorator


