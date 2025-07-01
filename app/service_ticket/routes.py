from flask import Blueprint, request, jsonify
from app import db
from .schemas import service_ticket_schema, service_tickets_schema
from app.models import ServiceTicket, Mechanic

service_ticket_bp = Blueprint('service_ticket_bp', __name__)


@service_ticket_bp.route('/', methods=['POST'])
def create_ticket():
    """
    Create a new service ticket
    ---
    tags:
      - ServiceTickets
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [description]
            properties:
              description:
                type: string
    responses:
      201:
        description: Ticket created
        content:
          application/json:
            schema:
              $ref: '#/definitions/ServiceTicket'
      400:
        description: Missing description
    """
    data = request.get_json()
    if not data or 'description' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    ticket = ServiceTicket(description=data['description'])
    db.session.add(ticket)
    db.session.commit()
    return service_ticket_schema.jsonify(ticket), 201


@service_ticket_bp.route('/', methods=['GET'])
def get_tickets():
    """
    List all service tickets
    ---
    tags:
      - ServiceTickets
    responses:
      200:
        description: A list of tickets
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/definitions/ServiceTicket'
    """
    tickets = ServiceTicket.query.all()
    return service_tickets_schema.jsonify(tickets), 200


@service_ticket_bp.route(
    '/<int:ticket_id>/assign-mechanic/<int:mechanic_id>',
    methods=['PUT'])
def assign_mechanic(ticket_id, mechanic_id):
    """
    Assign a mechanic to a ticket
    ---
    tags:
      - ServiceTickets
    parameters:
      - in: path
        name: ticket_id
        schema:
          type: integer
        required: true
      - in: path
        name: mechanic_id
        schema:
          type: integer
        required: true
    responses:
      200:
        description: Mechanic assigned
        content:
          application/json:
            schema:
              $ref: '#/definitions/ServiceTicket'
      404:
        description: Ticket or Mechanic not found
    """
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    mech = Mechanic.query.get_or_404(mechanic_id)
    if mech not in ticket.mechanics:
        ticket.mechanics.append(mech)
        db.session.commit()
    return service_ticket_schema.jsonify(ticket), 200


@service_ticket_bp.route(
    '/<int:ticket_id>/remove-mechanic/<int:mechanic_id>',
    methods=['PUT'])
def remove_mechanic(ticket_id, mechanic_id):
    """
    Remove a mechanic from a ticket
    ---
    tags:
      - ServiceTickets
    parameters:
      - in: path
        name: ticket_id
        schema:
          type: integer
        required: true
      - in: path
        name: mechanic_id
        schema:
          type: integer
        required: true
    responses:
      200:
        description: Mechanic removed
        content:
          application/json:
            schema:
              $ref: '#/definitions/ServiceTicket'
      404:
        description: Ticket or Mechanic not found
    """
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    mech = Mechanic.query.get_or_404(mechanic_id)
    if mech in ticket.mechanics:
        ticket.mechanics.remove(mech)
        db.session.commit()
    return service_ticket_schema.jsonify(ticket), 200
