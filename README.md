# Advanced API Final Project

A production-ready RESTful API for managing Mechanics and Service Tickets, built with Flask, SQLAlchemy, Marshmallow, and PostgreSQL, and deployed using CI/CD to Render.

## 🚀 Live API

- [View Deployed API on Render](https://advanced-api-final.onrender.com)

## 🛠️ Tech Stack

- Flask & Flask-SQLAlchemy
- Flask-Marshmallow
- PostgreSQL (hosted on Render)
- Gunicorn (production WSGI server)
- GitHub Actions (CI/CD pipeline)
- Render (hosting)

## 🔐 Environment Variables

Copy `.env.example` to `.env` and fill in your secrets for local dev.

| Variable      | Purpose                |
| ------------- | ---------------------- |
| DATABASE_URI  | PostgreSQL connection string |
| SECRET_KEY    | Flask app secret key   |

## ⚡ API Endpoints

| Method | Endpoint                          | Description                   |
|--------|-----------------------------------|-------------------------------|
| GET    | `/mechanics/`                     | List all mechanics            |
| POST   | `/mechanics/`                     | Add a new mechanic            |
| GET    | `/mechanics/<id>`                 | Get mechanic by ID            |
| PUT    | `/mechanics/<id>`                 | Update mechanic               |
| DELETE | `/mechanics/<id>`                 | Delete mechanic               |
| GET    | `/service-tickets/`               | List all service tickets      |
| POST   | `/service-tickets/`               | Create service ticket         |
| PUT    | `/service-tickets/<id>/assign-mechanic/<mech_id>` | Assign mechanic     |
| PUT    | `/service-tickets/<id>/remove-mechanic/<mech_id>` | Remove mechanic     |

- **Full docs**: See [Swagger Docs](https://advanced-api-final.onrender.com/apidocs)  
  *(update link if different)*

## 🔄 Postman Collection

- [Download Postman Collection (JSON)](./postman_collection.json)
- Import into Postman, and you’re ready to test every endpoint live!

## 🧑‍💻 Local Development

```bash
git clone https://github.com/MotherTheresa64/Advanced-API-Final.git
cd Advanced-API-Final
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # Add your secrets to .env
python flask_app.py           # Or use Flask CLI if set up

🚦 CI/CD and Deployment
Every push to main triggers GitHub Actions workflow:

Lint/build

Run tests (if present)

Deploy to Render (using secure deploy hook)

See .github/workflows/main.yaml for full pipeline config

🤝 Contributors
Noah Ragan (MotherTheresa64)