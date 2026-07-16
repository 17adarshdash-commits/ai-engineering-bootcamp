students = {}

def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    students[name] = {"age": age, "marks": marks}

    print("Student added successfully.")

def view_students():
    if not students:
        print("No student records found.")
        return

    for name, info in students.items():
        print(f"Name: {name}\nAge: {info['age']}\nMarks: {info['marks']}\n")
        print("-----------------\n")

def search_student():
    name = input("Enter Student Name: ")
    if name in students:
        info = students[name]
        print(f"\nStudent Found:\nName: {name}\nAge: {info['age']}\nMarks: {info['marks']}\n")
    else:
        print("Student not found.\n")

while True:
    choice = int(input("1. Add Student\n2. View Students\n3. Search Student\n4. Exit\n\nEnter choice: "))

    if choice == 1:
        add_student()
        continue

    elif choice == 2:
        view_students()
        continue

    elif choice == 3:
        search_student()
        continue

    elif choice == 4:
        print("Thank you for using Student Database.")
        break

    else:
        print("Invalid Choice. Please pick 1, 2, 3, or 4.\n")
        continue

