from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.features.auth.services import AuthService
from app.features.auth.schemas import UserRegisterSchema, UserSchema

auth_bp = Blueprint("auth", __name__)

# instatiate stateless global schemas for serilization/deserialization
register_schema= UserRegisterSchema
user_schema =UserSchema

@auth_bp.route("/register", methods=["POST"])
def register():
    """Endpoint handling user accounts enrollment"""

    # "or {}" prevents app from crashing in the event the request body is empty
    payload = request.get_json() or {}

    try: 
        # validate the input values using marshamallow
        validated_data = register_schema.load(payload)

        #pass validate data to the service layer
        new_user = AuthService.register_user(validated_data)

        #convert the db object back into clean JSON - user_schema.dump()
        return jsonify({
            "message": "User registered successfully.",
            "user": user_schema.dump(new_user)
        }), 201
    
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    except ValueError as err:
        return jsonify({"error": str(err)}), 409

@auth_bp.route("/login", methods=["POST"])
def login():
    """Handles security credential validation"""
    payload = request.get_json() or {}

    email = payload.get("email")
    password = payload.get("password")

    if not email or not password:
        return jsonify({
            "error": "Email and password are required fields"
        }), 400

    try:
        auth_data = AuthService.authenticate_user(email, password)

        return jsonify({
            "message": "Login Successful",
            "access_token": auth_data["access_token"],
            "user": user_schema.dump(auth_data["user"])
        })
    
    except ValueError as err:
        return jsonify({"error": str(err)}), 401
