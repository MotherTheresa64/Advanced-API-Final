# Advanced API Final Project

A production-ready Flask REST API for managing Mechanics & Service Tickets, with full CI/CD to Render and local dev parity.

## 🚀 Live on Render

- **Base URL:** https://advanced-api-final.onrender.com  
- **Swagger UI:** https://advanced-api-final.onrender.com/apidocs/  

## 🛠️ Tech Stack

- **Framework:** Flask  
- **ORM:** SQLAlchemy  
- **Serialization:** Marshmallow  
- **Docs:** Flasgger (Swagger UI)  
- **DB:** PostgreSQL (Render)  
- **WSGI:** Gunicorn  
- **CI/CD:** GitHub Actions → Render deploy hook  
- **Lint & Test:** flake8, pytest

## 🔧 Local Development

```bash
# 1) Clone & enter
git clone https://github.com/MotherTheresa64/Advanced-API-Final.git
cd Advanced-API-Final

# 2) Create & activate venv
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4) Lint & auto-format (optional)
flake8 app/
autopep8 --in-place --aggressive --aggressive -r app/

# 5) Run tests
pytest --maxfail=1 --disable-warnings -q

# 6) Start dev server
python run.py
# → http://127.0.0.1:5000
# Swagger at http://127.0.0.1:5000/apidocs/
