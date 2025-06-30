from flask import Blueprint, request, jsonify
from app import db
from .schemas import mechanic_schema, mechanics_schema
from app.models import Mechanic

mechanic_bp = Blueprint('mechanic_bp', __name__)

@mechanic_bp.route('/', methods=['POST'])
def create_mechanic():
    data = request.get_json()
    if not data or 'name' not in data or 'specialty' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    try:
        new_mechanic = Mechanic(name=data['name'], specialty=data['specialty'])
        db.session.add(new_mechanic)
        db.session.commit()
        return mechanic_schema.jsonify(new_mechanic), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@mechanic_bp.route('/', methods=['GET'])
def get_mechanics():
    mechanics = Mechanic.query.all()
    return mechanics_schema.jsonify(mechanics), 200

@mechanic_bp.route('/<int:id>', methods=['PUT'])
def update_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    data = request.get_json()
    mechanic.name = data.get('name', mechanic.name)
    mechanic.specialty = data.get('specialty', mechanic.specialty)
    db.session.commit()
    return mechanic_schema.jsonify(mechanic), 200

@mechanic_bp.route('/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    db.session.delete(mechanic)
    db.session.commit()
    return '', 204
