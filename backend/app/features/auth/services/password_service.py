from werkzeug.security import generate_password_hash, check_password_hash

class PasswordService:
    """Handles hashing the passwords"""

    def hash_password(self, password: str) -> str:
        return generate_password_hash(password)

    def verify_password(self, password: str, password_hash: str) -> bool:
        return check_password_hash(password_hash, password)