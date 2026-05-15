def authenticate_user_smg(username_smg, password_smg):
    """Check credentials against users.txt."""
    try:
        with open("users.txt", "r") as file_smg:
            for line_smg in file_smg:
                line_smg = line_smg.strip()
                if not line_smg:
                    continue
                try:
                    stored_username_smg, stored_password_smg = line_smg.split(",", 1)
                except ValueError:
                    print("Invalid user record format found in users.txt")
                    continue

                if stored_username_smg == username_smg and stored_password_smg == password_smg:
                    return True
        return False
    except FileNotFoundError:
        raise


def main_smg():
    try:
        username_smg = input("Enter username: ").strip()
        password_smg = input("Enter password: ").strip()

        if not username_smg or not password_smg:
            raise ValueError("Username and password cannot be empty.")

        if authenticate_user_smg(username_smg, password_smg):
            print("Login successful!")
        else:
            print("Invalid username or password.")
    except FileNotFoundError:
        print("File not found: users.txt")
    except ValueError as error_smg:
        print("Incorrect input format:", error_smg)


if __name__ == "__main__":
    main_smg()
