# Advanced API Final

Production-ready Flask API for Mechanics & Service Tickets.

## Live
https://<your-render-service>.onrender.com

## Setup
1. Copy `.env.example` → `.env`
2. `python -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python flask_app.py`

## Endpoints
- `GET /mechanics/`
- `POST /mechanics/`
- `PUT /mechanics/<id>`
- `DELETE /mechanics/<id>`
- `GET /service-tickets/`
- `POST /service-tickets/`
- `PUT /service-tickets/<id>/assign-mechanic/<mech_id>`
- `PUT /service-tickets/<id>/remove-mechanic/<mech_id>`
