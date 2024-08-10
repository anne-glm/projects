from auth import sign_up, log_in
from reservation import view_available_times, make_reservation, cancel_reservation, view_user_reservations

def main():
    while True:
        print("\n1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            try:
                print(sign_up(username, password))
            except ValueError as e:
                print(e)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            try:
                print(log_in(username, password))
                user_session(username)
            except ValueError as e:
                print(e)

        elif choice == "3":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

def user_session(username):
    while True:
        print("\n1. View Available Times")
        print("2. Make a Reservation")
        print("3. Cancel a Reservation")
        print("4. View My Reservations")
        print("5. Logout")
        action = input("Choose an action: ")

        if action == "1":
            try:
                available_times = view_available_times()
                print("Available times:", available_times)
            except ValueError as e:
                print(e)

        elif action == "2":
            time_slot = input("Enter time slot: ")
            try:
                print(make_reservation(username, time_slot))
            except ValueError as e:
                print(e)

        elif action == "3":
            time_slot = input("Enter time slot to cancel: ")
            try:
                print(cancel_reservation(username, time_slot))
            except ValueError as e:
                print(e)

        elif action == "4":
            try:
                reservations = view_user_reservations(username)
                if reservations == "No reservations found.":
                    print(reservations)
                else:
                    print("Your reservations:", reservations)
            except ValueError as e:
                print(e)

        elif action == "5":
            print("Logging out.")
            break

        else:
            print("Invalid action. Please select a valid option.")

if __name__ == "__main__":
    main()
