# flask_app.py
from app import create_app
from app.config import ProductionConfig

app = create_app(ProductionConfig)
from flask import redirect   # ← add this import
from app import create_app
from app.config import ProductionConfig

app = create_app(ProductionConfig)

# Health check & convenience redirect
@app.route("/", methods=["GET", "HEAD"])
def index():
    # Option A: simple OK message
    # return "API is live!", 200

    # Option B: redirect to your Swagger docs
    return redirect("/apidocs")
