"""
main.py

Command-line interface for the Contact Management System.
"""

from contact_manager import ContactManager
from exceptions import ContactError

DATA_FILE = "contacts.json"

MENU = """
========== Contact Management System ==========
1. Add Contact
2. Update Contact
3. Delete Contact
4. Search Contact
5. Display All Contacts
6. Save Contacts to JSON
7. Load Contacts from JSON
8. Exit
=================================================
"""


def add_contact(manager):
    contact_id = input("Enter contact ID: ").strip()
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    try:
        manager.add_contact(contact_id, name, phone, email)
        print("Contact added successfully.")
    except ContactError as e:
        print(f"Error: {e}")


def update_contact(manager):
    contact_id = input("Enter contact ID to update: ").strip()
    print("Leave a field blank to keep it unchanged.")
    name = input("New name: ").strip() or None
    phone = input("New phone number: ").strip() or None
    email = input("New email: ").strip() or None

    try:
        manager.update_contact(contact_id, name=name, phone=phone, email=email)
        print("Contact updated successfully.")
    except ContactError as e:
        print(f"Error: {e}")


def delete_contact(manager):
    contact_id = input("Enter contact ID to delete: ").strip()
    try:
        manager.delete_contact(contact_id)
        print("Contact deleted successfully.")
    except ContactError as e:
        print(f"Error: {e}")


def search_contact(manager):
    keyword = input("Enter search keyword (ID/name/phone/email): ").strip()
    results = manager.search_contact(keyword)
    if not results:
        print("No matching contacts found.")
        return

    for contact in results:
        print(contact)


def display_contacts(manager):
    manager.display_contacts()


def save_contacts(manager):
    filepath = input(f"Enter filepath to save [{DATA_FILE}]: ").strip() or DATA_FILE
    manager.save_to_json(filepath)
    print(f"Contacts saved to '{filepath}'.")


def load_contacts(manager):
    filepath = input(f"Enter filepath to load [{DATA_FILE}]: ").strip() or DATA_FILE
    try:
        manager.load_from_json(filepath)
        print(f"Contacts loaded from '{filepath}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")


def main():
    manager = ContactManager()

    actions = {
        "1": add_contact,
        "2": update_contact,
        "3": delete_contact,
        "4": search_contact,
        "5": display_contacts,
        "6": save_contacts,
        "7": load_contacts,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "8":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action(manager)


if __name__ == "__main__":
    main()
