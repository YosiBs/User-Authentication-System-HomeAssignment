class User:
    def __init__(self, email, hashed_password):
        self.email = email
        self.hashed_password = hashed_password

    def to_dict(self):
        return {
            "email": self.email
            # Add more fields here in future (like name, created_at)
        }
