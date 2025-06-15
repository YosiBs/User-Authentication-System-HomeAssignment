import unittest
import json
from backend.app import app
from backend.utils.extensions import db
from backend.models import UserModel
import bcrypt

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        response = self.client.post('/register', json={
            "email": "test@example.com",
            "password": "Aa123456",
            "name": "Tester"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"User registered successfully!", response.data)

    def test_login(self):
        with app.app_context():
            hashed_pw = bcrypt.hashpw("Aa123456".encode(), bcrypt.gensalt())
            user = UserModel(email="test2@example.com", hashed_password=hashed_pw, name="Tester")
            user.is_verified = True
            db.session.add(user)
            db.session.commit()

        response = self.client.post('/login', json={
            "email": "test2@example.com",
            "password": "Aa123456"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"token", response.data)

    def test_dashboard_unauthorized(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"Token missing", response.data)

    def test_login_invalid(self):
        with app.app_context():
            hashed_pw = bcrypt.hashpw("password123".encode(), bcrypt.gensalt())
            user = UserModel(email="test3@example.com", hashed_password=hashed_pw, name="Tester")
            user.is_verified = True
            db.session.add(user)
            db.session.commit()

        response = self.client.post('/login', json={
            "email": "test3@example.com",
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"Invalid credentials", response.data)

if __name__ == '__main__':
    unittest.main()
