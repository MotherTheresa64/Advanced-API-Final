# flask_app.py

from app import create_app
from app.config import ProductionConfig

# WSGI entrypoint for Gunicorn
app = create_app(ProductionConfig)
