# flask_app.py

from flask import redirect
from flasgger import Swagger           # ← import Swagger
from app import create_app
from app.config import ProductionConfig

app = create_app(ProductionConfig)

# Initialize Swagger UI here
swagger = Swagger(app,               # this will serve the UI at /apidocs
                  template={
                      "swagger": "2.0",
                      "info": {
                          "title": "Advanced API Final",
                          "description": "Mechanics & Service Tickets API",
                          "version": "1.0"
                      },
                      "schemes": ["https"],
                      "host": "advanced-api-final.onrender.com"  # your Render host
                  })

@app.route("/", methods=["GET", "HEAD"])
def index():
    # Redirect users (and Render health checks) to the Swagger UI
    return redirect("/apidocs")
