import os

DATA_FILE = "students.txt"

def load_students():
    students = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, age, roll_no, dept, gpa = [part.strip() for part in line.split(",")]
                
                students[name] = {
                    "age": int(age), 
                    "roll_no": int(roll_no), 
                    "dept": dept, 
                    "gpa": float(gpa)
                }
    except FileNotFoundError:
        pass
    except ValueError:
        print("Warning: Data file is corrupted or contains invalid formats.")
    return students


def save_students():
    with open(DATA_FILE, "w") as file:
        for name, info in students.items():
            file.write(f"{name}, {info['age']}, {info['roll_no']}, {info['dept']}, {info['gpa']}\n")

students = load_students()

def add_student():
    name = input("Enter Name: ")
    if name in students:
        print("Student already exists.")
        return

    try:
        age = int(input("Enter Age: "))
        roll_no = int(input("Enter Roll Number: "))
        dept = input("Enter Department: ")
        gpa = float(input("Enter GPA: "))
        
        students[name] = {'age': age, 'roll_no': roll_no, 'dept': dept, 'gpa': gpa}
        save_students()
        print("Student added successfully.")
    except ValueError:
        print("Error: Age and Roll Number must be integers, and GPA must be a number. Student not added.")


def view_students():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    for name, info in students.items():
        print(f"Name: {name}\nAge: {info['age']}\nRoll Number: {info['roll_no']}\nDepartment: {info['dept']}\nGPA: {info['gpa']}")
        print("-----------------")


def search_student():
    name = input("Enter Name: ")
    if name in students:
        info = students[name]
        print(f"Name: {name}\nAge: {info['age']}\nRoll Number: {info['roll_no']}\nDepartment: {info['dept']}\nGPA: {info['gpa']}")
    else:
        print("Student not found.")


def edit_student():
    name = input("Enter Name: ")
    if name not in students:
        print("Student not found.")
        return

    info = students[name]
    age = input(f"Enter new Age (leave blank to keep '{info['age']}'): ")
    roll_no = input(f"Enter new Roll Number (leave blank to keep '{info['roll_no']}'): ")
    dept = input(f"Enter new Department (leave blank to keep '{info['dept']}'): ")
    gpa = input(f"Enter new GPA (leave blank to keep '{info['gpa']}'): ")

    try:
        if age:
            info["age"] = int(age)
        if roll_no:
            info["roll_no"] = int(roll_no)
        if dept:
            info["dept"] = dept
        if gpa:
            info["gpa"] = float(gpa)

        save_students()
        print("Student updated successfully.")
    except ValueError:
        print("Error: Invalid number format entered. Changes aborted.")


def delete_student():
    name = input("Enter Name: ")
    if name in students:
        del students[name]
        save_students()
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def sort_by_gpa():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    for name, info in sorted(students.items(), key=lambda item: item[1]["gpa"], reverse=True):
        print(f"Name: {name}\nAge: {info['age']}\nRoll Number: {info['roll_no']}\nDepartment: {info['dept']}\nGPA: {info['gpa']}")
        print("-----------------")


def sort_alphabetically():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    for name, info in sorted(students.items()):
        print(f"Name: {name}\nAge: {info['age']}\nRoll Number: {info['roll_no']}\nDepartment: {info['dept']}\nGPA: {info['gpa']}")
        print("-----------------")


def export_class_report():
    if not students:
        print("Student Profile Manager is empty.\n")
        return

    gpas = {name: info["gpa"] for name, info in students.items()}
    highest_name = max(gpas, key=gpas.get)
    lowest_name = min(gpas, key=gpas.get)
    average_gpa = sum(gpas.values()) / len(gpas)

    with open("class_report.txt", "w") as file:
        file.write("===== Student Report =====\n\n")
        file.write(f"Total Students: {len(students)}\n\n")
        file.write("Highest GPA:\n")
        file.write(f"{highest_name} - {gpas[highest_name]}\n\n")
        file.write("Lowest GPA:\n")
        file.write(f"{lowest_name} - {gpas[lowest_name]}\n\n")
        file.write("Average GPA:\n")
        file.write(f"{average_gpa:.2f}\n")

    print("Class report exported to class_report.txt.")

while True:
    choice = input(
        "===== Student Profile Manager =====\n"
        "1. Add Student\n"
        "2. View Students\n"
        "3. Search Student\n"
        "4. Edit Student\n"
        "5. Delete Student\n"
        "6. Sort by GPA\n"
        "7. Sort Alphabetically\n"
        "8. Export Class Report\n"
        "9. Exit\n\n"
        "Enter your choice: "
    )

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        edit_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        sort_by_gpa()
    elif choice == "7":
        sort_alphabetically()
    elif choice == "8":
        export_class_report()
    elif choice == "9":
        print("Thank you for using the Student Profile Manager.")
        break
    else:
        print("Invalid Choice. Please pick 1-9.")

    print()