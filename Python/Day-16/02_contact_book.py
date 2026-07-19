contacts = {}

def add_contact():
    name = input("Enter Name: ")
    
    if name in contacts:
        choice = input("Contact already exists.\nDo you want to update the phone number? (y/n)")
        if choice == "y":
            phone_no = input("Enter Phone Number: ")
            contacts[name] = phone_no
            print("Contact updated successfully.")
            
    else:
        phone_no = input("Enter Phone Number: ")
        contacts[name] = phone_no
        print("Contact added successfully.")

def search_contact():
    name = input("Enter Name: ")

    if name in contacts:
        print(f"Phone Number: {contacts[name]}\n")
    else:
        print("Contact not found.")

def view_contacts():
    if not contacts:
        print("Contact book is empty.\n")
        return
    for key, value in contacts.items():
        print(f"{key}: {value}")
    print()

while True:

    choice = int(input("===== Contact Book =====\n1. Add Contact\n2. Search Contact\n3. View All Contacts\n4. Exit\n\nEnter your choice:"))

    if choice == 1:
        add_contact()
        continue

    elif choice == 2:
        search_contact()
        continue

    elif choice == 3:
        view_contacts()
        continue

    elif choice == 4:
        print("Thank you for using Contact Book.")
        break

    else:
        print("Invalid Choice.")

