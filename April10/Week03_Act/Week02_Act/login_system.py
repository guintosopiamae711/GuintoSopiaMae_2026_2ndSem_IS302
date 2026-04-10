correct_username_nbs = "admin"
correct_password_nbs = "1234"
attempts_nbs = 0
while attempts_nbs < 3:
    username_nbs = input("Enter username: ")
    password_nbs = input("Enter password: ")
    if username_nbs == correct_username_nbs and password_nbs == correct_password_nbs:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts_nbs += 1
if attempts_nbs == 3:
    print("Account Locked")
