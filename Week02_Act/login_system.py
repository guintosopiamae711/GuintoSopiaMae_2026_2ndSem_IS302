correct_username_smg = "admin"
correct_password_smg = "1234"
attempts_smg = 0
while attempts_smg < 3:
    username_smg = input("Enter username: ")
    password_smg = input("Enter password: ")
    if username_smg == correct_username_smg and password_smg == correct_password_smg:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts_smg += 1
if attempts_smg == 3:
    print("Account Locked")
