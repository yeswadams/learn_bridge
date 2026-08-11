# The Auth Business Logic 
import uuid
from flask_jwt_extended import create_access_token
from app.extensions.database import db
from app.features.auth.models import User, UserRole
from werkzeug.security import generate_password_hash, check_password_hash

class AuthService:
    """Handles business logic for registering users, checking login passwords, and generating tokens"""

    @staticmethod
    def register_user(data: dict) -> User:
        """
        Takes validated user data dictionary, hashes the password, and saves them to the db
        """

        # validate if email is unique:
        existing_user = User.query.filter_by(email=data["email"]).first()

        if existing_user:
            raise ValueError("A user with this email already exists")

        # hashing the password
        hashed_password = generate_password_hash(data["password"])

        # Instantiate New user
        new_user = User(
            full_name=data["full_name"],
            email=data["email"],
            password_hash=hashed_password,
            age=data["age"],
            role=data.get("role", UserRole.STUDENT)
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def authenticate_user(email: str, password: str) -> dict:
        """
        Verifies login credential and return a signed JWT access token alongside user info
        """

        # check if user with the email exists
        user = User.query.filter_by(email=email).first()

        # confirm credentials
        if not user or not check_password_hash(user.password_hash, password):
            raise ValueError("Invalid email or password.")

        # creation of the jwt
        access_token = create_access_token(identity=str(user.id))

        return {
            "access_token": access_token,
            "user": User
        }



