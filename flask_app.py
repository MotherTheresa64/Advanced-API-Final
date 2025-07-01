# flask_app.py

# ─── Monkey-patch Flask’s JSONEncoder for Flasgger compatibility ───
import flask.json
from flask.json.provider import DefaultJSONProvider

flask.json.JSONEncoder = DefaultJSONProvider
# ────────────────────────────────────────────────────────────────


from app import create_app
from app.config import ProductionConfig
from flask import redirect
from flasgger import Swagger


app = create_app(ProductionConfig)


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
                    "id":        {"type": "integer", "readOnly": True},
                    "name":      {"type": "string"},
                    "specialty": {"type": "string"}
                }
            },
            "ServiceTicket": {
                "type": "object",
                "properties": {
                    "id":          {"type": "integer", "readOnly": True},
                    "description": {"type": "string"},
                    "is_open":     {"type": "boolean"},
                    "mechanics": {
                        "type":  "array",
                        "items": {"$ref": "#/definitions/Mechanic"}
                    }
                }
            }
        }
    }
)


@app.route("/", methods=["GET", "HEAD"])
def index():
    """
    Redirect root to Swagger UI.
    """
    return redirect("/apidocs/")
