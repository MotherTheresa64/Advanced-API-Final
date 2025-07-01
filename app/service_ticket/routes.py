# app/service_ticket/routes.py
from flask import Blueprint, request, jsonify
from app import db
from .schemas import service_ticket_schema, service_tickets_schema
from app.models import ServiceTicket, Mechanic

service_ticket_bp = Blueprint("service_ticket_bp", __name__)

@service_ticket_bp.route("/", methods=["POST"])
def create_ticket():
    data = request.get_json() or {}
    if not data.get("description"):
        return jsonify({"error": "Missing required fields"}), 400
    ticket = ServiceTicket(description=data["description"])
    db.session.add(ticket)
    db.session.commit()
    return service_ticket_schema.jsonify(ticket), 201

@service_ticket_bp.route("/", methods=["GET"])
def get_tickets():
    all_tix = ServiceTicket.query.all()
    return service_tickets_schema.jsonify(all_tix), 200

@service_ticket_bp.route("/<int:ticket_id>/assign-mechanic/<int:mechanic_id>", methods=["PUT"])
def assign_mechanic(ticket_id, mechanic_id):
    t = ServiceTicket.query.get_or_404(ticket_id)
    m = Mechanic.query.get_or_404(mechanic_id)
    if m not in t.mechanics:
        t.mechanics.append(m)
        db.session.commit()
    return service_ticket_schema.jsonify(t), 200

@service_ticket_bp.route("/<int:ticket_id>/remove-mechanic/<int:mechanic_id>", methods=["PUT"])
def remove_mechanic(ticket_id, mechanic_id):
    t = ServiceTicket.query.get_or_404(ticket_id)
    m = Mechanic.query.get_or_404(mechanic_id)
    if m in t.mechanics:
        t.mechanics.remove(m)
        db.session.commit()
    return service_ticket_schema.jsonify(t), 200
