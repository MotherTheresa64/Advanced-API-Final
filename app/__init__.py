# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_object):
    """Application factory to create Flask app instances."""
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Register blueprints
    from .mechanic import mechanic_bp
    from .service_ticket import service_ticket_bp

    app.register_blueprint(mechanic_bp, url_prefix="/mechanics")
    app.register_blueprint(service_ticket_bp, url_prefix="/service-tickets")

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
