import os

# File name where user data will be stored
USER_FILE_SMG = 'users.txt'

def register_user_smg():
    """Function to register a new user."""
    print("\n--- Register New User ---")
    username_smg = input("Enter a username: ")
    password_smg = input("Enter a password: ")

    # Check if username already exists
    if check_user_exists_smg(username_smg):
        print("Username already exists. Try a different one.")
        return

    # Save user data to the file
    with open(USER_FILE_SMG, 'a') as file_smg:
        file_smg.write(f'{username_smg},{password_smg}\n')
    print("User registered successfully.")

def check_user_exists_smg(username_smg):
    """Function to check if a user already exists."""
    if not os.path.exists(USER_FILE_SMG):
        return False

    with open(USER_FILE_SMG, 'r') as file_smg:
        for line_smg in file_smg:
            stored_username_smg, _ = line_smg.strip().split(',')
            if stored_username_smg == username_smg:
                return True
    return False

def login_user_smg():
    """Function to log in an existing user."""
    print("\n--- Login ---")
    username_smg = input("Enter your username: ")
    password_smg = input("Enter your password: ")

    if authenticate_user_smg(username_smg, password_smg):
        print("Login successful!")
    else:
        print("Invalid username or password.")

def authenticate_user_smg(username_smg, password_smg):
    """Function to authenticate the user."""
    if not os.path.exists(USER_FILE_SMG):
        return False

    with open(USER_FILE_SMG, 'r') as file_smg:
        for line_smg in file_smg:
            stored_username_smg, stored_password_smg = line_smg.strip().split(',')
            if stored_username_smg == username_smg and stored_password_smg == password_smg:
                return True
    return False

def main_smg():
    """Main menu for the login system."""
    while True:
        print("\n--- Login System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice_smg = input("Select an option (1/2/3): ")

        if choice_smg == '1':
            register_user_smg()
        elif choice_smg == '2':
            login_user_smg()
        elif choice_smg == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_smg()