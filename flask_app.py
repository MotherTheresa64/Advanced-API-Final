import importlib
import sys

# monkey‐patch so flasgger.utils can `import imp`
sys.modules['imp'] = importlib

from flasgger import Swagger
from app import create_app
from app.config import ProductionConfig

app = create_app(ProductionConfig)

# initialize Swagger with defaults
Swagger(app)

# redirect root → docs
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return '', 302, {'Location': '/apidocs/'}
