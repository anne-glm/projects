from models import Reservation
from database import Database

db = Database()

def view_available_times():
    return db.get_available_times()

def make_reservation(username, time_slot):
    if not db.get_user(username):
        raise ValueError(f"Error: User '{username}' does not exist!")
    available_times = db.get_available_times()
    if time_slot not in available_times:
        raise ValueError(f"Error: Time slot '{time_slot}' is not available!")
    reservation = Reservation(username, time_slot)
    db.add_reservation(reservation)
    return "Reservation made successfully!"

def cancel_reservation(username, time_slot):
    if not db.get_user(username):
        raise ValueError(f"Error: User '{username}' does not exist!")
    existing_reservations = db.get_user_reservations(username)
    if not any(res['time_slot'] == time_slot for res in existing_reservations):
        raise ValueError(f"Error: No reservation found for time slot '{time_slot}'.")
    db.remove_reservation(username, time_slot)
    return "Reservation canceled successfully!"

def view_user_reservations(username):
    if not db.get_user(username):
        raise ValueError(f"Error: User '{username}' does not exist!")
    reservations = db.get_user_reservations(username)
    if not reservations:
        return "No reservations found."
    return reservations
