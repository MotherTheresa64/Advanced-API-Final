import pytest
from app import create_app, db
from app.config import Config
import werkzeug
from importlib.metadata import version

# Patch werkzeug.__version__ so FlaskClient can import it
if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = version("werkzeug")

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

@pytest.fixture
def client():
    # Create app and push an app context for the duration of each test
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        client = app.test_client()
        yield client
        db.drop_all()
