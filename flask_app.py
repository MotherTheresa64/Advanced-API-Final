# flask_app.py

# ——— Monkey‐patchs for Flasgger compatibility on Python 3.13+ ———
import sys
import types
import importlib.machinery
import flask.json
from flask.json.provider import DefaultJSONProvider

# 1) Give flask.json a JSONEncoder alias Flasgger expects  
flask.json.JSONEncoder = DefaultJSONProvider

# 2) Inject a fake imp module so Flasgger.utils can import it  
_imp = types.ModuleType("imp")
def _load_module(name, path):
    loader = importlib.machinery.SourceFileLoader(name, path)
    return loader.load_module()
_imp.load_module = _load_module
_imp.load_source = _load_module
sys.modules["imp"] = _imp
# ———————————————————————————————————————————————————————————————

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
