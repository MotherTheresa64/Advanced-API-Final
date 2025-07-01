# flask_app.py

# ——— Monkey‐patch for Flasgger + Flask 2.3 compatibility ———
import flask.json
from flask.json.provider import DefaultJSONProvider
flask.json.JSONEncoder = DefaultJSONProvider
# ——————————————————————————————————————————————————————————————

from flask import redirect
from flasgger import Swagger
from app import create_app
from app.config import ProductionConfig

app = create_app(ProductionConfig)

swagger = Swagger(
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
        "basePath": "/"
    }
)

@app.route("/", methods=["GET", "HEAD"])
def index():
    return redirect("/apidocs")
