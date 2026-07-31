import os

class Config():
    """
    Base config shared across all environments
    """
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "development-secret-key"
    )

    # DB Config
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://postgres:postgres@localhost:5432/learnbridge"
    )

    #SQLAlchemy Settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Setting for preventing it from sorting our JSON alphabetically
    JSON_SORT_KEYS = False