# flask_app.py

# ——— Patch in a fake imp module so Flasgger can import it ———
import sys
import types
import importlib.machinery

_imp = types.ModuleType("imp")

def load_module(name, path):
    loader = importlib.machinery.SourceFileLoader(name, path)
    return loader.load_module()

# Flasgger’s utils.py expects both load_module and load_source
_imp.load_module = load_module
_imp.load_source = load_module

sys.modules["imp"] = _imp
# ————————————————————————————————————————————————————————

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
