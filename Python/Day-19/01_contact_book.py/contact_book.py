DATA_FILE = "contacts.txt"


def load_contacts():
    contacts = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, phone_no, email = [part.strip() for part in line.split(",")]
                contacts[name] = {"phone_no": phone_no, "email": email}
    except FileNotFoundError:
        pass
    return contacts


def save_contacts():
    with open(DATA_FILE, "w") as file:
        for name, info in contacts.items():
            file.write(f"{name}, {info['phone_no']}, {info['email']}\n")


contacts = load_contacts()


def add_contact():
    name = input("Enter Name: ")
    if name in contacts:
        print("Contact already exists.")
        return

    phone_no = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contacts[name] = {"phone_no": phone_no, "email": email}
    save_contacts()
    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("Contact book is empty.\n")
        return
    for name, info in contacts.items():
        print(f"Name: {name}\nPhone No.: {info['phone_no']}\nEmail: {info['email']}")
        print("-----------------")


def search_contact():
    name = input("Enter Name: ")
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}\nPhone No.: {info['phone_no']}\nEmail: {info['email']}")
    else:
        print("Contact not found.")


def edit_contact():
    name = input("Enter Name: ")
    if name not in contacts:
        print("Contact not found.")
        return

    info = contacts[name]
    phone_no = input(f"Enter new Phone Number (leave blank to keep '{info['phone_no']}'): ")
    email = input(f"Enter new Email (leave blank to keep '{info['email']}'): ")

    if phone_no:
        info["phone_no"] = phone_no
    if email:
        info["email"] = email

    save_contacts()
    print("Contact updated successfully.")


def delete_contact():
    name = input("Enter Name: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


while True:
    choice = input(
        "===== Contact Book =====\n"
        "1. Add Contact\n"
        "2. View Contacts\n"
        "3. Search Contact\n"
        "4. Edit Contact\n"
        "5. Delete Contact\n"
        "6. Exit\n\n"
        "Enter your choice: "
    )

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using Contact Book.")
        break
    else:
        print("Invalid Choice. Please pick 1-6.")

    print()
