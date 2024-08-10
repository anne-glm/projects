class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password 

class Reservation:
    def __init__(self, username, time_slot):
        self.username = username
        self.time_slot = time_slot
