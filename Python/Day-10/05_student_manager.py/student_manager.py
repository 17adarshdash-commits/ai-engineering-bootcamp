print("===== Student Manager =====\n")
print("1. Add Student")
print("2. View Students")
print("3. Exit")

def add_student():
    try:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        branch = input("Enter Branch: ")
        cgpa = float(input("Enter CGPA: "))

        student = {
            "Name": name,
            "Age": age,
            "Branch": branch,
            "CGPA": cgpa
        }

        with open("students.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Branch: {branch}\n")
            file.write(f"CGPA: {cgpa}\n")
            file.write(f"------------------------\n")

        print("Student saved successfully!")
    except FileNotFoundError:
        print("File not found.")
    
def view_students():
    try:
        with open("students.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")

choice = input("Enter your choice: ")
print()

if choice == "1":
    add_student()
elif choice == "2":
    view_students()
elif choice == "3":
    print("Thank you for using Student Manager.")
else:
    print("Invalid choice.")