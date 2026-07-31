import os

class Config():
    """
    Base config shared across environments
    """
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "development-secret-key"
    )

class DevelopmentConfig:
    DEBUG = True

class TestConfig:
    TESTING = True

class ProductionConfig:
    DEBUG = False