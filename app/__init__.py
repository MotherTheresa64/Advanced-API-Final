import sys
import types
import importlib.machinery
import flask.json
from flask.json.provider import DefaultJSONProvider

from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger

# ─── Monkey-patch for Flasgger + Python 3.13+ ───
flask.json.JSONEncoder = DefaultJSONProvider
_imp = types.ModuleType("imp")


def _load_module(name, path):
    loader = importlib.machinery.SourceFileLoader(name, path)
    return loader.load_module()


_imp.load_module = _load_module
_imp.load_source = _load_module
sys.modules["imp"] = _imp
# ───────────────────────────────────────────────

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    ma.init_app(app)

    from app.mechanic.routes import mechanic_bp
    from app.service_ticket.routes import service_ticket_bp
    app.register_blueprint(mechanic_bp, url_prefix="/mechanics")
    app.register_blueprint(service_ticket_bp, url_prefix="/service-tickets")

    @app.route("/", methods=["GET", "HEAD"])
    def index():
        # health-check and redirect to docs
        return redirect("/apidocs/")

    Swagger(
        app,
        template={
            "swagger": "2.0",
            "info": {
                "title": "Advanced API Final",
                "description": "Mechanics & Service Tickets API",
                "version": "1.0"
            },
            "host": "advanced-api-final.onrender.com",
            "schemes": ["https"],
            "basePath": "/",
            "definitions": {
                "Mechanic": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "readOnly": True},
                        "name": {"type": "string"},
                        "specialty": {"type": "string"}
                    }
                },
                "ServiceTicket": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "readOnly": True},
                        "description": {"type": "string"},
                        "is_open": {"type": "boolean"},
                        "mechanics": {
                            "type": "array",
                            "items": {"$ref": "#/definitions/Mechanic"}
                        }
                    }
                }
            }
        }
    )

    with app.app_context():
        db.create_all()

    return app
