from models import User
from database import Database

db = Database()

def sign_up(username, password):
    if db.get_user(username):
        raise ValueError(f"Error: User '{username}' already exists!")
    if not username or not password:
        raise ValueError("Error: Username and password cannot be empty.")
    user = User(username, password)
    db.add_user(user)
    return "User signed up successfully!"

def log_in(username, password):
    user = db.get_user(username)
    if not user:
        raise ValueError(f"Error: User '{username}' does not exist!")
    if user['password'] != password:
        raise ValueError("Error: Incorrect password!")
    return "Logged in successfully!"
