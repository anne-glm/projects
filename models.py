class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # Note: In a real application, never store passwords in plain text

class Reservation:
    def __init__(self, username, time_slot):
        self.username = username
        self.time_slot = time_slot