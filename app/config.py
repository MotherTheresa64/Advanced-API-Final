import os


class Config:
    """Base configuration with default settings."""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///local.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")


class ProductionConfig(Config):
    """Production configuration that reads from environment variables."""
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI",
        Config.SQLALCHEMY_DATABASE_URI
    )
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        Config.SECRET_KEY
    )
