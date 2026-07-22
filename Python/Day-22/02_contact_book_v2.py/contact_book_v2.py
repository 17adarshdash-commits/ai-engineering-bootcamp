import os
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "contacts.txt")
REPORT_FILE = os.path.join(BASE_DIR, "contact_report.txt")


def load_contacts():
    contacts = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = [part.strip() for part in line.split(",")]
                if len(parts) == 4:
                    name, phone_no, email, date_added = parts
                else:
                    name, phone_no, email = parts
                    date_added = ""
                contacts[name] = {"phone_no": phone_no, "email": email, "date_added": date_added}
    except FileNotFoundError:
        pass
    return contacts


def save_contacts():
    with open(DATA_FILE, "w") as file:
        for name, info in contacts.items():
            file.write(f"{name}, {info['phone_no']}, {info['email']}, {info['date_added']}\n")


contacts = load_contacts()


def is_valid_phone(phone_no):
    return phone_no.isdigit() and len(phone_no) == 10


def is_valid_email(email):
    return "@" in email and "." in email


def phone_exists(phone_no, ignore_name=None):
    for name, info in contacts.items():
        if name == ignore_name:
            continue
        if info["phone_no"] == phone_no:
            return True
    return False


def add_contact():
    name = input("Enter Name: ")
    if name in contacts:
        print("Contact already exists.")
        return

    phone_no = input("Enter Phone Number: ")
    if not is_valid_phone(phone_no):
        print("Invalid phone number. It must contain exactly 10 digits.")
        return
    if phone_exists(phone_no):
        print("A contact with this phone number already exists.")
        return

    email = input("Enter Email: ")
    if not is_valid_email(email):
        print("Invalid email. It must contain '@' and '.'.")
        return

    contacts[name] = {
        "phone_no": phone_no,
        "email": email,
        "date_added": date.today().isoformat(),
    }
    save_contacts()
    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("Contact book is empty.\n")
        return
    for name, info in contacts.items():
        print(
            f"Name: {name}\nPhone No.: {info['phone_no']}\nEmail: {info['email']}"
            f"\nDate Added: {info['date_added']}"
        )
        print("-----------------")


def search_contact():
    name = input("Enter Name: ")
    if name in contacts:
        info = contacts[name]
        print(
            f"Name: {name}\nPhone No.: {info['phone_no']}\nEmail: {info['email']}"
            f"\nDate Added: {info['date_added']}"
        )
    else:
        print("Contact not found.")


def search_by_phone():
    query = input("Enter Phone Number (or part of it): ").strip()
    matches = [(name, info) for name, info in contacts.items() if query in info["phone_no"]]

    if not matches:
        print("No matching contacts found.")
        return

    for name, info in matches:
        print(
            f"Name: {name}\nPhone No.: {info['phone_no']}\nEmail: {info['email']}"
            f"\nDate Added: {info['date_added']}"
        )
        print("-----------------")


def search_by_email():
    query = input("Enter Email (or part of it): ").strip().lower()
    matches = [(name, info) for name, info in contacts.items() if query in info["email"].lower()]

    if not matches:
        print("No matching contacts found.")
        return

    for name, info in matches:
        print(
            f"Name: {name}\nPhone No.: {info['phone_no']}\nEmail: {info['email']}"
            f"\nDate Added: {info['date_added']}"
        )
        print("-----------------")


def edit_contact():
    name = input("Enter Name: ")
    if name not in contacts:
        print("Contact not found.")
        return

    info = contacts[name]
    phone_no = input(f"Enter new Phone Number (leave blank to keep '{info['phone_no']}'): ")
    email = input(f"Enter new Email (leave blank to keep '{info['email']}'): ")

    if phone_no:
        if not is_valid_phone(phone_no):
            print("Invalid phone number. It must contain exactly 10 digits.")
            return
        if phone_exists(phone_no, ignore_name=name):
            print("A contact with this phone number already exists.")
            return
        info["phone_no"] = phone_no

    if email:
        if not is_valid_email(email):
            print("Invalid email. It must contain '@' and '.'.")
            return
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


def generate_contact_report():
    lines = []
    lines.append("========== CONTACT REPORT ==========\n")
    lines.append(f"Generated On: {date.today().isoformat()}\n")
    lines.append(f"Total Contacts: {len(contacts)}\n")

    lines.append("\nContacts Beginning With\n")
    counts_by_letter = {}
    for name in contacts:
        letter = name[0].upper() if name else "#"
        counts_by_letter[letter] = counts_by_letter.get(letter, 0) + 1
    for letter in sorted(counts_by_letter):
        lines.append(f"{letter} : {counts_by_letter[letter]}\n")

    lines.append("\n--------------------------------\n")
    lines.append("\nComplete Contact List\n\n")
    for name in sorted(contacts):
        info = contacts[name]
        lines.append(
            f"Name: {name}\nPhone: {info['phone_no']}\nEmail: {info['email']}"
            f"\nDate Added: {info['date_added']}\n\n"
        )

    with open(REPORT_FILE, "w") as file:
        file.writelines(lines)

    print(f"Contact report exported to {REPORT_FILE}")


while True:
    choice = input(
        "===== Contact Book =====\n"
        "1. Add Contact\n"
        "2. View Contacts\n"
        "3. Search Contact by Name\n"
        "4. Search Contact by Phone\n"
        "5. Search Contact by Email\n"
        "6. Edit Contact\n"
        "7. Delete Contact\n"
        "8. Export Contact Report\n"
        "9. Exit\n\n"
        "Enter your choice: "
    )

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        search_by_phone()
    elif choice == "5":
        search_by_email()
    elif choice == "6":
        edit_contact()
    elif choice == "7":
        delete_contact()
    elif choice == "8":
        generate_contact_report()
    elif choice == "9":
        print("Thank you for using Contact Book.")
        break
    else:
        print("Invalid Choice. Please pick 1-9.")

    print()
