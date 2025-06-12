import unittest
from backend.app import app

class RegisterInputValidationTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_missing_email(self):
        response = self.client.post('/register', json={
            "password": "somepassword"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Email and password required", response.data)

    def test_missing_password(self):
        response = self.client.post('/register', json={
            "email": "user@missingpass.com"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Email and password required", response.data)

    def test_duplicate_email(self):
        self.client.post('/register', json={
            "email": "duplicate@example.com",
            "password": "abc123"
        })
        response = self.client.post('/register', json={
            "email": "duplicate@example.com",
            "password": "different"
        })
        self.assertEqual(response.status_code, 409)
        self.assertIn(b"User already exists", response.data)

if __name__ == '__main__':
    unittest.main()
