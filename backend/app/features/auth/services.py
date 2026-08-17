# The Auth Business Logic 
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from app.extensions.database import db
from app.features.auth.models import User, UserRole
from app.features.auth.services.password_service import PasswordService


class AuthService:
    """Handles business logic for registering users, checking login passwords, and generating tokens"""

    def __init__(self):
        # this relationship is called composition
        self.password_service = PasswordService() 

    def register_user(self, data: dict) -> User:
        """
        Takes validated user data dictionary, hashes the password, and saves them to the db
        """

        # validate if email is unique:
        existing_user = User.query.filter_by(email=data["email"]).first()

        if existing_user:
            raise ValueError("A user with this email already exists")

        # hashing the password
        hashed_password = self.password_service.hash_password(
            data["password"]
        )

        # Instantiate New user
        new_user = User(
            full_name=data["full_name"],
            email=data["email"],
            password_hash=hashed_password,
            age=data["age"],
            role=UserRole.STUDENT
        )
        try: 
            db.session.add(new_user)
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            raise

        return new_user

    
    def authenticate_user(self, email: str, password: str) -> dict:
        """
        Verifies login credential and return a signed JWT access token alongside user info
        """

        # check if user with the email exists
        user = User.query.filter_by(email=email).first()

        # confirm credentials
        if not user or not self.password_service.verify_password(
            password, 
            user.password_hash
        ):
            raise ValueError("Invalid email or password.")

        # creation of the jwt
        access_token = create_access_token(identity=str(user.id))

        return {
            "access_token": access_token,
            "user": user
        }



