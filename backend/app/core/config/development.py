from .base import Config

class DevelopmentConfig(Config):
    """
    Configuration used during local development.
    """

    DEBUG = True