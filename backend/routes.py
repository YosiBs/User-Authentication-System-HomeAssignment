from flask import Blueprint, request, jsonify
import bcrypt
import jwt
import datetime
from .config import SECRET_KEY, JWT_ALGORITHM
from .models import User

auth_routes = Blueprint('auth', __name__)

# Temporary in-memory user store
users = {}
#----------------------------------------------------------------------------------------------------------register [POST]
@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    if email in users:
        return jsonify({"error": "User already exists"}), 409

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User(email, hashed_pw)
    users[email] = user
    return jsonify({"message": "User registered successfully!"})
#----------------------------------------------------------------------------------------------------------login [POST]
@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    user = users.get(email)
    if not user or not bcrypt.checkpw(password.encode(), user.hashed_password):
      return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode(
        {
            "email": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )

    return jsonify({"token": token})
#----------------------------------------------------------------------------------------------------------Dashboard [GET]
@auth_routes.route('/dashboard', methods=['GET'])
def dashboard():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Token missing"}), 401

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        email = decoded["email"]
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

    user = users.get(email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "message": f"Welcome {user.email}!",
        "user": user.to_dict()
    })
