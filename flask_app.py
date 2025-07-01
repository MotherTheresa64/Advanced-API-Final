from flask import redirect
from flasgger import Swagger
from app import create_app
from app.config import ProductionConfig

# create the Flask app using your ProductionConfig
app = create_app(ProductionConfig)

# configure and initialize Flasgger / Swagger UI
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}
Swagger(app, config=swagger_config)


@app.route("/", methods=["GET", "HEAD"])
def root_redirect():
    """
    Redirect the root URL to /apidocs/ so users land on your Swagger UI.
    """
    return redirect("/apidocs/")
