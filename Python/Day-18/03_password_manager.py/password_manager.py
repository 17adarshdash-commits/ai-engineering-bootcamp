def load_passwords():
    passwords = {}
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                website, username, password = [part.strip() for part in line.split(",")]
                passwords[website] = {"username": username, "password": password}
    except FileNotFoundError:
        pass
    return passwords

passwords = load_passwords()

def add_password():
    
    website = input("Enter Website: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    passwords[website] = {"username": username, "password": password}

    data = f"{website}, {username}, {password}\n"

    with open("passwords.txt","a") as file:
        file.write(data)

    print("Password added successsfully.")

def view_passwords():
    try:
        with open("passwords.txt","r") as file:
            content = file.read()
            print(f"{content}\n")
    except FileNotFoundError:
        print("No passwords recorded yet.\n")

def search_password():
    website = input("Enter Website Name: ")
    if website in passwords:
        info = passwords[website]
        print(f"\nWebsite Found:\nWebsite Name: {website}\nUsername: {info['username']}\nPassword: {info['password']}\n")
    else:
        print("Website not found.\n")

while True:
    choice = int(input("1. Add Password\n2. View Paswords\n3. Search Password\n4. Exit\n\nEnter choice: "))

    if choice == 1:
        add_password()
        continue

    elif choice == 2:
        view_passwords()
        continue

    elif choice == 3:
        search_password()
        continue

    elif choice == 4:
        print("Thank you for using Password Manager.")
        break

    else:
        print("Invalid Choice. Please pick 1, 2, 3, or 4.\n")
        continue