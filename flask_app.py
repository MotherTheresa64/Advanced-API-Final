# flask_app.py
from app import create_app
from app.config import ProductionConfig

app = create_app(ProductionConfig)
