import json
import os

class Database:
    def __init__(self, filename='data.json'):
        self.filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump({"users": [], "reservations": []}, file)

    def read_data(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def write_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def add_user(self, user):
        data = self.read_data()
        data['users'].append({"username": user.username, "password": user.password})
        self.write_data(data)

    def add_reservation(self, reservation):
        data = self.read_data()
        data['reservations'].append({"username": reservation.username, "time_slot": reservation.time_slot})
        self.write_data(data)

    def remove_reservation(self, username, time_slot):
        data = self.read_data()
        data['reservations'] = [
            res for res in data['reservations']
            if not (res['username'] == username and res['time_slot'] == time_slot)
        ]
        self.write_data(data)

    def get_user(self, username):
        data = self.read_data()
        for user in data['users']:
            if user['username'] == username:
                return user
        return None

    def get_user_reservations(self, username):
        data = self.read_data()
        return [res for res in data['reservations'] if res['username'] == username]

    def get_available_times(self):
        all_time_slots = ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM"]
        data = self.read_data()
        booked_slots = [res['time_slot'] for res in data['reservations']]
        return [slot for slot in all_time_slots if slot not in booked_slots]
