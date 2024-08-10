import unittest
from reservation import view_available_times, make_reservation, cancel_reservation, view_user_reservations
from auth import sign_up
from database import Database


class TestReservation(unittest.TestCase):
    def setUp(self):
        self.db = Database('test_data.json')
        self.db.write_data({"users": [], "reservations": []})
        sign_up("testuser", "password123")

    def test_view_available_times(self):
        times = view_available_times()
        self.assertIn("10:00 AM", times)

    def test_make_reservation(self):
        result = make_reservation("testuser", "10:00 AM")
        self.assertEqual(result, "Reservation made successfully!")

    def test_make_reservation_unavailable(self):
        make_reservation("testuser", "10:00 AM")
        with self.assertRaises(ValueError) as context:
            make_reservation("testuser", "10:00 AM")
        self.assertIn("Time slot '10:00 AM' is not available", str(context.exception))

    def test_cancel_reservation(self):
        make_reservation("testuser", "10:00 AM")
        result = cancel_reservation("testuser", "10:00 AM")
        self.assertEqual(result, "Reservation canceled successfully!")

    def test_cancel_reservation_not_found(self):
        with self.assertRaises(ValueError) as context:
            cancel_reservation("testuser", "10:00 AM")
        self.assertIn("No reservation found for time slot", str(context.exception))

    def test_view_user_reservations(self):
        make_reservation("testuser", "10:00 AM")
        reservations = view_user_reservations("testuser")
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0]['time_slot'], "10:00 AM")


if __name__ == '__main__':
    unittest.main()
