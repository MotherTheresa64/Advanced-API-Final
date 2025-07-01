from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    ma.init_app(app)

    # register blueprints from their routes modules
    from .mechanic.routes import mechanic_bp
    from .service_ticket.routes import service_ticket_bp

    app.register_blueprint(mechanic_bp, url_prefix='/mechanics')
    app.register_blueprint(service_ticket_bp, url_prefix='/service-tickets')

    # ensure all tables exist
    with app.app_context():
        db.create_all()

    return app
