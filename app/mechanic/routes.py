from flask import Blueprint, request, jsonify
from app import db
from .schemas import mechanic_schema, mechanics_schema
from app.models import Mechanic

mechanic_bp = Blueprint('mechanic_bp', __name__)

@mechanic_bp.route('/', methods=['POST'])
def create_mechanic():
    """
    Create a new mechanic
    ---
    tags:
      - Mechanics
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/definitions/Mechanic'
    responses:
      201:
        description: Mechanic created
        content:
          application/json:
            schema:
              $ref: '#/definitions/Mechanic'
      400:
        description: Missing fields
    """
    data = request.get_json()
    if not data or 'name' not in data or 'specialty' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_mech = Mechanic(name=data['name'], specialty=data['specialty'])
    db.session.add(new_mech)
    db.session.commit()
    return mechanic_schema.jsonify(new_mech), 201

@mechanic_bp.route('/', methods=['GET'])
def get_mechanics():
    """
    List all mechanics
    ---
    tags:
      - Mechanics
    responses:
      200:
        description: A list of mechanics
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/definitions/Mechanic'
    """
    mechanics = Mechanic.query.all()
    return mechanics_schema.jsonify(mechanics), 200

@mechanic_bp.route('/<int:id>', methods=['PUT'])
def update_mechanic(id):
    """
    Update a mechanic by ID
    ---
    tags:
      - Mechanics
    parameters:
      - in: path
        name: id
        schema:
          type: integer
        required: true
    requestBody:
      required: false
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
              specialty:
                type: string
    responses:
      200:
        description: Mechanic updated
        content:
          application/json:
            schema:
              $ref: '#/definitions/Mechanic'
      404:
        description: Mechanic not found
    """
    mech = Mechanic.query.get_or_404(id)
    data = request.get_json()
    mech.name = data.get('name', mech.name)
    mech.specialty = data.get('specialty', mech.specialty)
    db.session.commit()
    return mechanic_schema.jsonify(mech), 200

@mechanic_bp.route('/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    """
    Delete a mechanic by ID
    ---
    tags:
      - Mechanics
    parameters:
      - in: path
        name: id
        schema:
          type: integer
        required: true
    responses:
      204:
        description: Mechanic deleted
      404:
        description: Mechanic not found
    """
    mech = Mechanic.query.get_or_404(id)
    db.session.delete(mech)
    db.session.commit()
    return '', 204
