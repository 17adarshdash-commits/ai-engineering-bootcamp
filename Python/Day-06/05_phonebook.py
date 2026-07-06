phonebook = {
    "Alice": "9999999999",
    "Bob": "8888888888",
    "Charlie": "7777777777"
}

name = input("Enter name: ")
if name in phonebook:
    print(f"Phone Number: {phonebook.get(name)}")
else:
    print("Contact not found")