"""Contact Management System - terminal-based contacts app."""

import csv
import os

CONTACTS_FILE = "contacts.txt"
BACKUP_FILE = "contacts_backup.txt"
CSV_FILE = "contacts_export.csv"
REPORT_FILE = "contact_report.txt"

contacts = {}


def load_contacts():
    """Load contacts from CONTACTS_FILE into the contacts dict, if it exists."""
    if not os.path.exists(CONTACTS_FILE):
        return

    with open(CONTACTS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 5:
                continue
            contact_id, name, phone, email, city = parts
            contacts[int(contact_id)] = {
                "id": int(contact_id),
                "name": name,
                "phone": phone,
                "email": email,
                "city": city,
            }


def save_contacts():
    """Write all contacts to CONTACTS_FILE."""
    with open(CONTACTS_FILE, "w") as f:
        for contact in contacts.values():
            f.write(
                f"{contact['id']},{contact['name']},{contact['phone']},"
                f"{contact['email']},{contact['city']}\n"
            )


def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10


def validate_email(email):
    return bool(email) and "@" in email and "." in email


def add_contact():
    try:
        contact_id = int(input("Enter Contact ID: ").strip())
    except ValueError:
        print("Contact ID must be a number.")
        return

    if contact_id in contacts:
        print("ID already exists.")
        return

    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter Phone Number: ").strip()
    if not validate_phone(phone):
        print("Invalid phone number. Must be exactly 10 digits.")
        return

    email = input("Enter Email: ").strip()
    if not validate_email(email):
        print("Invalid email address.")
        return

    city = input("Enter City: ").strip()

    contacts[contact_id] = {
        "id": contact_id,
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
    }
    save_contacts()
    print("Contact added successfully.")


def delete_contact():
    try:
        contact_id = int(input("Enter Contact ID to delete: ").strip())
    except ValueError:
        print("Contact ID must be a number.")
        return

    if contact_id not in contacts:
        print("No contact found with that ID.")
        return

    del contacts[contact_id]
    save_contacts()
    print("Contact deleted successfully.")


def update_contact():
    try:
        contact_id = int(input("Enter Contact ID to update: ").strip())
    except ValueError:
        print("Contact ID must be a number.")
        return

    if contact_id not in contacts:
        print("No contact found with that ID.")
        return

    contact = contacts[contact_id]

    name = input(f"Enter new Name [{contact['name']}]: ").strip()
    if name:
        contact["name"] = name

    phone = input(f"Enter new Phone [{contact['phone']}]: ").strip()
    if phone:
        if not validate_phone(phone):
            print("Invalid phone number. Update to phone skipped.")
        else:
            contact["phone"] = phone

    email = input(f"Enter new Email [{contact['email']}]: ").strip()
    if email:
        if not validate_email(email):
            print("Invalid email. Update to email skipped.")
        else:
            contact["email"] = email

    city = input(f"Enter new City [{contact['city']}]: ").strip()
    if city:
        contact["city"] = city

    save_contacts()
    print("Contact updated successfully.")


def print_contact(contact):
    print("--------------------------------")
    print(f"ID    : {contact['id']}")
    print(f"Name  : {contact['name']}")
    print(f"Phone : {contact['phone']}")
    print(f"Email : {contact['email']}")
    print(f"City  : {contact['city']}")
    print("--------------------------------")


def search_by_name():
    query = input("Search by Name: ").strip().lower()
    found = [c for c in contacts.values() if query in c["name"].lower()]

    if not found:
        print("No matching contacts found.")
        return

    for contact in found:
        print_contact(contact)


def search_by_phone():
    query = input("Search by Phone: ").strip()
    found = [c for c in contacts.values() if query in c["phone"]]

    if not found:
        print("No matching contacts found.")
        return

    for contact in found:
        print_contact(contact)


def display_contacts():
    if not contacts:
        print("No contacts to display.")
        return

    for contact in contacts.values():
        print_contact(contact)


def sort_by_name():
    if not contacts:
        print("No contacts to display.")
        return

    for contact in sorted(contacts.values(), key=lambda c: c["name"].lower()):
        print_contact(contact)


def sort_by_city():
    if not contacts:
        print("No contacts to display.")
        return

    for contact in sorted(contacts.values(), key=lambda c: c["city"].lower()):
        print_contact(contact)


def export_csv():
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Phone", "Email", "City"])
        for contact in contacts.values():
            writer.writerow(
                [contact["id"], contact["name"], contact["phone"],
                 contact["email"], contact["city"]]
            )
    print(f"Contacts exported to {CSV_FILE}.")


def backup_contacts():
    with open(BACKUP_FILE, "w") as f:
        for contact in contacts.values():
            f.write(
                f"{contact['id']},{contact['name']},{contact['phone']},"
                f"{contact['email']},{contact['city']}\n"
            )
    print(f"Backup created at {BACKUP_FILE}.")


def generate_report():
    city_counts = {}
    for contact in contacts.values():
        city_counts[contact["city"]] = city_counts.get(contact["city"], 0) + 1

    with open(REPORT_FILE, "w") as f:
        f.write(f"Total Contacts: {len(contacts)}\n\n")
        f.write("Cities:\n")
        max_city_len = max((len(city) for city in city_counts), default=0)
        for city in sorted(city_counts):
            f.write(f"{city.ljust(max_city_len)} : {city_counts[city]}\n")

    print(f"Report generated at {REPORT_FILE}.")


def menu():
    print("========== Contact Management System ==========")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search by Name")
    print("5. Search by Phone")
    print("6. Display All Contacts")
    print("7. Sort by Name")
    print("8. Sort by City")
    print("9. Export CSV")
    print("10. Backup Contacts")
    print("11. Generate Report")
    print("12. Exit")
    print("===============================================")


def main():
    load_contacts()

    actions = {
        "1": add_contact,
        "2": delete_contact,
        "3": update_contact,
        "4": search_by_name,
        "5": search_by_phone,
        "6": display_contacts,
        "7": sort_by_name,
        "8": sort_by_city,
        "9": export_csv,
        "10": backup_contacts,
        "11": generate_report,
    }

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "12":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action()


if __name__ == "__main__":
    main()
