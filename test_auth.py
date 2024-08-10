import unittest
from auth import sign_up, log_in
from database import Database


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.db = Database('test_data.json')
        self.db.write_data({"users": [], "reservations": []})

    def test_sign_up(self):
        result = sign_up("testuser", "password123")
        self.assertEqual(result, "User signed up successfully!")

    def test_sign_up_existing_user(self):
        sign_up("testuser", "password123")
        with self.assertRaises(ValueError) as context:
            sign_up("testuser", "password123")
        self.assertIn("already exists", str(context.exception))

    def test_log_in(self):
        sign_up("testuser", "password123")
        result = log_in("testuser", "password123")
        self.assertEqual(result, "Logged in successfully!")

    def test_log_in_incorrect_password(self):
        sign_up("testuser", "password123")
        with self.assertRaises(ValueError) as context:
            log_in("testuser", "wrongpassword")
        self.assertIn("Incorrect password", str(context.exception))

    def test_log_in_non_existent_user(self):
        with self.assertRaises(ValueError) as context:
            log_in("nonexistent", "password123")
        self.assertIn("does not exist", str(context.exception))


if __name__ == '__main__':
    unittest.main()
