username = "admin"
password = "python123"

user = input("Enter username: ")
pw = input("Enter password: ")

if (user == username) and (pw == password):
    print("Login Successful")
else:
    print("Invalid Credentials")