from app.extensions.database import db
from app.features.auth.models import User

def create_test_user():
    user = User (
        full_name="Test Student",
        email="teststudent@example.com",
        password_hash="fake_hash",
        age=23
    )

    db.session.add(user)
    db.session.commit()

    print("User created!")
    print("ID:", user.id)