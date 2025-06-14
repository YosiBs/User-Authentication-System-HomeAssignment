from backend.utils.extensions import db
import uuid

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.LargeBinary(128), nullable=False)
    name = db.Column(db.String(100), default="")
    is_verified = db.Column(db.Boolean, default=False)
    verification_token = db.Column(db.String(100), default=lambda: str(uuid.uuid4()))
    reset_token = db.Column(db.String(100), nullable=True)

    def __init__(self, email, hashed_password, name=""):
        self.email = email
        self.hashed_password = hashed_password
        self.name = name
        self.verification_token = str(uuid.uuid4())
        self.is_verified = False
        self.reset_token = None

    def to_dict(self):
        return {
            "email": self.email,
            "name": self.name,
            "is_verified": self.is_verified
        }