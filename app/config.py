import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///local.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY")
