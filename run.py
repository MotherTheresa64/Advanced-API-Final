from flask_app import app

if __name__ == "__main__":
    # this will pick up everything you wired up in flask_app.py,
    # including your Swagger docs and root redirect
    app.run(debug=True)
