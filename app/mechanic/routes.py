# app/mechanic/routes.py
from flask import Blueprint, request, jsonify
from app import db
from .schemas import mechanic_schema, mechanics_schema
from app.models import Mechanic

mechanic_bp = Blueprint("mechanic_bp", __name__)

@mechanic_bp.route("/", methods=["POST"])
def create_mechanic():
    data = request.get_json() or {}
    if not data.get("name") or not data.get("specialty"):
        return jsonify({"error": "Missing required fields"}), 400
    mech = Mechanic(name=data["name"], specialty=data["specialty"])
    db.session.add(mech)
    db.session.commit()
    return mechanic_schema.jsonify(mech), 201

@mechanic_bp.route("/", methods=["GET"])
def get_mechanics():
    all_mech = Mechanic.query.all()
    return mechanics_schema.jsonify(all_mech), 200

@mechanic_bp.route("/<int:id>", methods=["PUT"])
def update_mechanic(id):
    mech = Mechanic.query.get_or_404(id)
    data = request.get_json() or {}
    mech.name = data.get("name", mech.name)
    mech.specialty = data.get("specialty", mech.specialty)
    db.session.commit()
    return mechanic_schema.jsonify(mech), 200

@mechanic_bp.route("/<int:id>", methods=["DELETE"])
def delete_mechanic(id):
    mech = Mechanic.query.get_or_404(id)
    db.session.delete(mech)
    db.session.commit()
    return "", 204
