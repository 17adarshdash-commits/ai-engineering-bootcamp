contacts = {
    "Adarsh": "9876543210",
    "Rahul": "9123456780",
    "Priya": "9988776655",
    "Ananya": "9012345678",
    "Arjun": "9871234560"
}

name = input("Enter contact name: ")

if name in contacts:
    print(f"Phone Number: {contacts[name]}")
else:
    print("Contact not found.")