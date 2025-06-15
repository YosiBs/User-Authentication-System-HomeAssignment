from flask import Blueprint, request, jsonify, Response
import bcrypt
import jwt
import datetime
from backend.utils.html_templates import INVALID_LINK_HTML, RESET_FORM_MAIL, VERIFIED_HTML
from .config import JWT_EXPIRATION_HOURS, RATE_LIMIT_LOGIN, SECRET_KEY, JWT_ALGORITHM
# from .models import User
from .utils.limiter import limiter
from .utils.email_util import send_verification_email, send_reset_email
import uuid
from backend.utils.extensions import db
from .models import UserModel


auth_routes = Blueprint('auth', __name__)

#----------------------------------------------------------------------------------------------------------register [POST]
@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email',"").lower()
    name = data.get('name', "")
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    if UserModel.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 409

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = UserModel(email=email, hashed_password=hashed_pw, name=name)
    db.session.add(user)
    db.session.commit()

    send_verification_email(email, user.verification_token)
    return jsonify({"message": "User registered successfully!"})

#----------------------------------------------------------------------------------------------------------login [POST]
@auth_routes.route('/login', methods=['POST'])
@limiter.limit(RATE_LIMIT_LOGIN)
def login():
    data = request.json
    email = data.get('email',"").lower()
    password = data.get('password')
    
    user = UserModel.query.filter_by(email=email).first()
    if not user or not bcrypt.checkpw(password.encode(), user.hashed_password):
        return jsonify({"error": "Invalid credentials"}), 401

    if not user.is_verified:
        return jsonify({"error": "Email not verified. Check your inbox."}), 403
    
    token = jwt.encode(
        {
            "email": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=JWT_EXPIRATION_HOURS)
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

    user = UserModel.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "message": f"Welcome {user.email}!",
        "user": user.to_dict()
    })

#----------------------------------------------------------------------------------------------------------Email Verification [GET]
@auth_routes.route('/verify', methods=['GET'])
def verify_email():
    token = request.args.get('token')
    user = UserModel.query.filter_by(verification_token=token).first()
    if user:
        user.is_verified = True
        db.session.commit()
        return Response(VERIFIED_HTML, mimetype='text/html')
    return Response(INVALID_LINK_HTML, mimetype='text/html'), 400

#----------------------------------------------------------------------------------------------------------Reset Password [POST]
@auth_routes.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email',"").lower()
    user = UserModel.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Email not found"}), 404

    user.reset_token = str(uuid.uuid4())
    db.session.commit()
    send_reset_email(email, user.reset_token)

    return jsonify({"message": "Password reset link sent to your email"})

#----------------------------------------------------------------------------------------------------------Reset Password [GET]
@auth_routes.route('/reset', methods=['GET'])
def reset_form():
    token = request.args.get('token')
    return Response(RESET_FORM_MAIL.format(token=token), mimetype='text/html')

#----------------------------------------------------------------------------------------------------------Reset Password [POST]
@auth_routes.route('/reset', methods=['POST'])
def reset_password():
    token = request.form.get('token')
    new_password = request.form.get('new_password')

    user = UserModel.query.filter_by(reset_token=token).first()
    if user:
        user.hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        user.reset_token = None
        db.session.commit()
        return Response("<h2 style='text-align:center;'>Password reset successful!</h2>", mimetype='text/html')
    return Response("<h2 style='text-align:center; color:red;'>Invalid or expired reset link</h2>", mimetype='text/html'), 400

#----------------------------------------------------------------------------------------------------------Update Profile (name) [PUT]
@auth_routes.route('/update-profile', methods=['PUT'])
def update_profile():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Missing token"}), 401

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        email = decoded.get("email")
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

    user = UserModel.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user.name = data.get('name', user.name)
    db.session.commit()

    return jsonify({"message": "Profile updated", "user": user.to_dict()})
