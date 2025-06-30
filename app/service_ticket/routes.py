from flask import Blueprint, request, jsonify
from app import db
from .schemas import service_ticket_schema, service_tickets_schema
from app.models import ServiceTicket, Mechanic

service_ticket_bp = Blueprint('service_ticket_bp', __name__)

@service_ticket_bp.route('/', methods=['POST'])
def create_ticket():
    data = request.get_json()
    if not data or 'description' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    try:
        ticket = ServiceTicket(description=data['description'])
        db.session.add(ticket)
        db.session.commit()
        return service_ticket_schema.jsonify(ticket), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@service_ticket_bp.route('/', methods=['GET'])
def get_tickets():
    tickets = ServiceTicket.query.all()
    return service_tickets_schema.jsonify(tickets), 200

@service_ticket_bp.route('/<int:ticket_id>/assign-mechanic/<int:mechanic_id>', methods=['PUT'])
def assign_mechanic(ticket_id, mechanic_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    if mechanic not in ticket.mechanics:
        ticket.mechanics.append(mechanic)
        db.session.commit()
    return service_ticket_schema.jsonify(ticket), 200

@service_ticket_bp.route('/<int:ticket_id>/remove-mechanic/<int:mechanic_id>', methods=['PUT'])
def remove_mechanic(ticket_id, mechanic_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    if mechanic in ticket.mechanics:
        ticket.mechanics.remove(mechanic)
        db.session.commit()
    return service_ticket_schema.jsonify(ticket), 200
