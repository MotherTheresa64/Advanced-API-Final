# Advanced API Final Project

A production-ready RESTful API for managing **Mechanics** and **Service Tickets**, built with Flask, SQLAlchemy, Marshmallow, and PostgreSQL, with CI/CD to Render and interactive Swagger documentation.

---

## 🚀 Live Demo

**API Base URL:**  
https://advanced-api-final.onrender.com  

**Swagger UI:**  
https://advanced-api-final.onrender.com/apidocs/  

---

## 📖 Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Clone & Install](#clone--install)  
  - [Environment Variables](#environment-variables)  
  - [Database](#database)  
- [Running Locally](#running-locally)  
- [Testing](#testing)  
- [CI/CD Pipeline](#cicd-pipeline)  
- [Deployment to Render](#deployment-to-render)  
- [API Endpoints](#api-endpoints)  
- [Swagger Documentation](#swagger-documentation)  
- [Postman Collection](#postman-collection)  
- [Contributing](#contributing)  
- [License](#license)

---

## 🔥 Features

- **CRUD for Mechanics**  
- **Create & list Service Tickets**  
- **Assign / remove Mechanics** on a Ticket  
- **Flask Application Factory** pattern  
- **Environment-protected** secrets (no hardcoded URIs or keys)  
- **Gunicorn** WSGI server for production  
- **CI/CD** pipeline (lint → tests → deploy) via GitHub Actions  
- **Automated Deploy** to Render on every push to `main`  
- **Interactive Swagger UI** at `/apidocs/` over HTTPS  

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Marshmallow  
- **Database:** PostgreSQL (hosted on Render)  
- **Serialization & Validation:** Marshmallow, marshmallow-sqlalchemy  
- **Production WSGI:** Gunicorn  
- **CI/CD:** GitHub Actions  
- **Hosting:** Render.com  
- **API Docs:** Flasgger (Swagger UI)  

---

## 📥 Getting Started

### Prerequisites

- Python 3.11+  
- Git  
- (Optional) virtual environment tool (`venv`, `virtualenv`, etc.)  

---

### Clone & Install

```bash
git clone https://github.com/MotherTheresa64/Advanced-API-Final.git
cd Advanced-API-Final

# create and activate a virtual environment
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt

Environment Variables
Copy the example:

bash
Copy
Edit
cp .env.example .env
Edit .env and set:

ini
Copy
Edit
DATABASE_URI=postgres://<user>:<pass>@<host>:<port>/<db_name>
SECRET_KEY=your-secret-key
Do not commit your real .env – it’s already in .gitignore.

Database
On Render, provision a PostgreSQL database and paste its connection string into DATABASE_URI.

Locally, omitting DATABASE_URI falls back to sqlite:///local.db.

▶️ Running Locally
bash
Copy
Edit
# Development server
python run.py

# Open in browser:
# http://127.0.0.1:5000/      → redirects to /apidocs/
# http://127.0.0.1:5000/apidocs/
🧪 Testing
bash
Copy
Edit
# Check style
flake8 app/

# Run tests
pytest --maxfail=1 --disable-warnings -q
You should see all tests pass:

css
Copy
Edit
.......                                                              [100%]
🔄 CI/CD Pipeline
Every push to main triggers GitHub Actions:

Lint (flake8 app/)

Test (pytest tests/)

Deploy (calls your Render deploy webhook stored in the RENDER_DEPLOY_HOOK secret)

See .github/workflows/main.yaml for details.

🚢 Deployment to Render
In Render dashboard, create a Web Service on branch main.

Build Command:

nginx
Copy
Edit
pip install -r requirements.txt
Start Command:

nginx
Copy
Edit
gunicorn flask_app:app
Add environment variables under Environment:

DATABASE_URI

SECRET_KEY

Enable Auto-Deploy on push to main.

🔗 API Endpoints
Method	Endpoint	Description
GET	/mechanics/	List all mechanics
POST	/mechanics/	Create a new mechanic
PUT	/mechanics/{id}	Update a mechanic by ID
DELETE	/mechanics/{id}	Delete a mechanic by ID
GET	/service-tickets/	List all service tickets
POST	/service-tickets/	Create a new service ticket
PUT	/service-tickets/{ticket_id}/assign-mechanic/{mechanic_id}	Assign a mechanic to a ticket
PUT	/service-tickets/{ticket_id}/remove-mechanic/{mechanic_id}	Remove a mechanic from a ticket

📋 Swagger Documentation
Swagger UI:
https://advanced-api-final.onrender.com/apidocs/

Raw OpenAPI JSON:
https://advanced-api-final.onrender.com/apispec_1.json


