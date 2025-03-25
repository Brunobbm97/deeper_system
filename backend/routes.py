from flask import Blueprint, request, jsonify
from config import db
from bson import ObjectId
from datetime import datetime

routes = Blueprint('routes', __name__)

# Utilitário para converter ObjectId e datetimes para JSON
def serialize_user(user):
    user['_id'] = str(user['_id'])
    return user

# CREATE - POST /users
@routes.route('/users', methods=['POST'])
def create_user():
    data = request.json

    new_user = {
        "username": data['username'],
        "password": data['password'],
        "roles": data.get('roles', []),
        "preferences": {
            "timezone": data['preferences']['timezone']
        },
        "active": data.get('active', True),
        "created_ts": data.get('created_ts', datetime.utcnow().timestamp())
    }

    result = db.users.insert_one(new_user)
    return jsonify({"message": "USER CREATED", "id": str(result.inserted_id)}), 201

# READ ALL - GET /users
@routes.route('/users', methods=['GET'])
def get_users():
    users = list(db.users.find())
    return jsonify([serialize_user(u) for u in users])

# READ ONE - GET /users/<id>
@routes.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = db.users.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify(serialize_user(user))
    return jsonify({"error": "USER NOT FOUND"}), 404

# UPDATE - PUT /users/<id>
@routes.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    update_data = {
        "username": data['username'],
        "password": data['password'],
        "roles": data.get('roles', []),
        "preferences": {
            "timezone": data['preferences']['timezone']
        },
        "active": data.get('active', True),
        "created_ts": data.get('created_ts', datetime.utcnow().timestamp())
    }

    result = db.users.update_one({"_id": ObjectId(id)}, {"$set": update_data})

    if result.matched_count:
        return jsonify({"message": "User updated successfully"})
    return jsonify({"error": "User not found"}), 404

# DELETE - DELETE /users/<id>
@routes.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = db.users.delete_one({"_id": ObjectId(id)})

    if result.deleted_count:
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404
