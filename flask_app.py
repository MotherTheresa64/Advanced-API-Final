# flask_app.py

from flask import redirect
from flasgger import Swagger
from app import create_app
from app.config import ProductionConfig

app = create_app(ProductionConfig)

# Configure Swagger UI
swagger = Swagger(
    app,
    template={
        "swagger": "2.0",
        "info": {
            "title": "Advanced API Final",
            "description": "Mechanics & Service Tickets API",
            "version": "1.0"
        },
        "host": "advanced-api-final.onrender.com",  # your Render URL (no https://)
        "schemes": ["https"],
        "basePath": "/"
    }
)

@app.route("/", methods=["GET", "HEAD"])
def index():
    # redirect root to Swagger UI
    return redirect("/apidocs")
