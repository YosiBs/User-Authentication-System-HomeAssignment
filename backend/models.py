import uuid
class User:
    def __init__(self, email, hashed_password, name=""):
        self.email = email
        self.hashed_password = hashed_password
        self.name = name
        self.is_verified = False
        self.verification_token = str(uuid.uuid4())
        self.reset_token = None 
        

    def to_dict(self):
        return {
            "email": self.email,
            "name": self.name,
            "is_verified": self.is_verified
        }
