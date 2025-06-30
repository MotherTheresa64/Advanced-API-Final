from app import create_app
from app.config import Config  # Use Config for local dev/testing

app = create_app(Config)

if __name__ == "__main__":
    app.run(debug=True)
