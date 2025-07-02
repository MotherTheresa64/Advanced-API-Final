from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_class=None):
    app = Flask(__name__)

    # load config (default to Development)
    if config_class:
        app.config.from_object(config_class)
    else:
        # fallback to .env or defaults
        from app.config import Config
        app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    # register blueprints
    from app.mechanic import mechanic_bp
    from app.service_ticket import service_ticket_bp

    app.register_blueprint(mechanic_bp, url_prefix='/mechanics')
    app.register_blueprint(service_ticket_bp, url_prefix='/service-tickets')

    # create tables if needed
    with app.app_context():
        db.create_all()

    return app
