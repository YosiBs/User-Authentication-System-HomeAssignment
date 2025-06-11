import unittest
import json
from backend.app import app

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_register(self):
        response = self.client.post('/register', json={
            "email": "test@example.com",
            "password": "test123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"User registered successfully!", response.data)

    def test_login(self):
        # First, register the user
        self.client.post('/register', json={
            "email": "test2@example.com",
            "password": "test123"
        })
        # Then, try to login
        response = self.client.post('/login', json={
            "email": "test2@example.com",
            "password": "test123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"token", response.data)

    def test_dashboard_unauthorized(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"Token missing", response.data)

    def test_login_invalid(self):
        # Register user first
        self.client.post('/register', json={
            "email": "test3@example.com",
            "password": "password123"
        })
        # Attempt to login with wrong password
        response = self.client.post('/login', json={
            "email": "test3@example.com",
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"Invalid credentials", response.data)



if __name__ == '__main__':
    unittest.main()
