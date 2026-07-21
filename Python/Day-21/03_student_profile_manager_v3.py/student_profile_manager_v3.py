import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "students.txt")
CLASS_REPORT_FILE = os.path.join(SCRIPT_DIR, "class_report.txt")
CLASS_STATISTICS_FILE = os.path.join(SCRIPT_DIR, "class_statistics.txt")

def load_students():
    students = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, age, roll_no, dept, gpa, date_added = [part.strip() for part in line.split(",")]

                students[name] = {
                    "age": int(age),
                    "roll_no": int(roll_no),
                    "dept": dept,
                    "gpa": float(gpa),
                    "date_added": date_added
                }
    except FileNotFoundError:
        pass
    except ValueError:
        print("Warning: Data file is corrupted or contains invalid formats.")
    return students


def save_students():
    with open(DATA_FILE, "w") as file:
        for name, info in students.items():
            file.write(f"{name}, {info['age']}, {info['roll_no']}, {info['dept']}, {info['gpa']}, {info['date_added']}\n")

students = load_students()

def get_valid_name(exclude_name=None):
    while True:
        name = input("Enter Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        if name != exclude_name and name in students:
            print("Student already exists.")
            return None
        return name


def get_valid_age():
    while True:
        try:
            age = int(input("Enter Age: "))
        except ValueError:
            print("Age must be an integer.")
            continue
        if age < 15 or age > 100:
            print("Must be between 15 and 100.")
            continue
        return age


def get_valid_roll_no(exclude_name=None):
    existing_rolls = {
        info["roll_no"] for n, info in students.items() if n != exclude_name
    }
    while True:
        roll_no = input("Enter Roll Number: ").strip()
        if not roll_no:
            print("Roll Number cannot be empty.")
            continue
        try:
            roll_no = int(roll_no)
        except ValueError:
            print("Roll Number must be an integer.")
            continue
        if roll_no in existing_rolls:
            print("Roll Number must be unique.")
            continue
        return roll_no


def get_valid_gpa():
    while True:
        try:
            gpa = float(input("Enter GPA: "))
        except ValueError:
            print("GPA must be a number.")
            continue
        if gpa < 0.0 or gpa > 10.0:
            print("Must be between 0.0 and 10.0.")
            continue
        return gpa


def add_student():
    name = get_valid_name()
    if name is None:
        return

    age = get_valid_age()
    roll_no = get_valid_roll_no()
    dept = input("Enter Department: ")
    gpa = get_valid_gpa()
    date_added = datetime.now().strftime("%Y-%m-%d")

    students[name] = {'age': age, 'roll_no': roll_no, 'dept': dept, 'gpa': gpa, 'date_added': date_added}
    save_students()
    print("Student added successfully.")


def view_students():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    for name, info in students.items():
        print(f"Name: {name}\nAge: {info['age']}\nRoll Number: {info['roll_no']}\nDepartment: {info['dept']}\nGPA: {info['gpa']}\nDate Added: {info['date_added']}")
        print("-----------------")


def search_student():
    name = input("Enter Name: ")
    if name in students:
        info = students[name]
        print(f"Name: {name}\nAge: {info['age']}\nRoll Number: {info['roll_no']}\nDepartment: {info['dept']}\nGPA: {info['gpa']}\nDate Added: {info['date_added']}")
    else:
        print("Student not found.")


def edit_student():
    name = input("Enter Name: ").strip()
    if name not in students:
        print("Student not found.")
        return

    info = students[name]

    while True:
        age = input(f"Enter new Age (leave blank to keep '{info['age']}'): ").strip()
        if not age:
            break
        try:
            age = int(age)
        except ValueError:
            print("Age must be an integer.")
            continue
        if age < 15 or age > 100:
            print("Must be between 15 and 100.")
            continue
        info["age"] = age
        break

    existing_rolls = {
        n_info["roll_no"] for n, n_info in students.items() if n != name
    }
    while True:
        roll_no = input(f"Enter new Roll Number (leave blank to keep '{info['roll_no']}'): ").strip()
        if not roll_no:
            break
        try:
            roll_no = int(roll_no)
        except ValueError:
            print("Roll Number must be an integer.")
            continue
        if roll_no in existing_rolls:
            print("Roll Number must be unique.")
            continue
        info["roll_no"] = roll_no
        break

    dept = input(f"Enter new Department (leave blank to keep '{info['dept']}'): ").strip()
    if dept:
        info["dept"] = dept

    while True:
        gpa = input(f"Enter new GPA (leave blank to keep '{info['gpa']}'): ").strip()
        if not gpa:
            break
        try:
            gpa = float(gpa)
        except ValueError:
            print("GPA must be a number.")
            continue
        if gpa < 0.0 or gpa > 10.0:
            print("Must be between 0.0 and 10.0.")
            continue
        info["gpa"] = gpa
        break

    save_students()
    print("Student updated successfully.")


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
        print(f"Name: {name}\nAge: {info['age']}\nRoll Number: {info['roll_no']}\nDepartment: {info['dept']}\nGPA: {info['gpa']}\nDate Added: {info['date_added']}")
        print("-----------------")


def sort_alphabetically():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    for name, info in sorted(students.items()):
        print(f"Name: {name}\nAge: {info['age']}\nRoll Number: {info['roll_no']}\nDepartment: {info['dept']}\nGPA: {info['gpa']}\nDate Added: {info['date_added']}")
        print("-----------------")


def generate_class_report():
    if not students:
        print("Student Profile Manager is empty.\n")
        return

    gpas = {name: info["gpa"] for name, info in students.items()}
    highest_gpa = max(gpas.values())
    lowest_gpa = min(gpas.values())
    average_gpa = sum(gpas.values()) / len(gpas)

    departments = {}
    for info in students.values():
        departments[info["dept"]] = departments.get(info["dept"], 0) + 1

    with open(CLASS_REPORT_FILE, "w") as file:
        file.write("========== CLASS REPORT ==========\n\n")
        file.write("Generated On:\n")
        file.write(f"{datetime.now().strftime('%Y-%m-%d')}\n\n")
        file.write("Total Students:\n")
        file.write(f"{len(students)}\n\n")
        file.write("Average GPA:\n")
        file.write(f"{average_gpa:.2f}\n\n")
        file.write("Highest GPA:\n")
        file.write(f"{highest_gpa}\n\n")
        file.write("Lowest GPA:\n")
        file.write(f"{lowest_gpa}\n\n")
        file.write("Students Per Department\n\n")
        for dept, count in sorted(departments.items()):
            file.write(f"{dept} : {count}\n")
        file.write("\n-------------------------------\n\n")
        file.write("Student List\n\n")
        file.write(f"{'Roll No':<11}{'Name':<13}{'GPA':<7}{'Department':<14}{'Date Added'}\n\n")
        for name, info in sorted(students.items(), key=lambda item: item[1]["roll_no"]):
            file.write(
                f"{info['roll_no']:<11}{name:<13}{info['gpa']:<7}{info['dept']:<14}{info['date_added']}\n"
            )

    print("Class report generated to class_report.txt.")


def export_class_statistics():
    if not students:
        print("Student Profile Manager is empty.\n")
        return

    gpas = {name: info["gpa"] for name, info in students.items()}
    highest_name = max(gpas, key=gpas.get)
    lowest_name = min(gpas, key=gpas.get)
    average_gpa = sum(gpas.values()) / len(gpas)

    departments = {}
    for info in students.values():
        departments[info["dept"]] = departments.get(info["dept"], 0) + 1

    with open(CLASS_STATISTICS_FILE, "w") as file:
        file.write("===== Class Statistics =====\n\n")
        file.write(f"Total Students: {len(students)}\n\n")
        file.write(f"Average GPA: {average_gpa:.2f}\n\n")
        file.write("Highest GPA:\n")
        file.write(f"{highest_name} - {gpas[highest_name]}\n\n")
        file.write("Lowest GPA:\n")
        file.write(f"{lowest_name} - {gpas[lowest_name]}\n\n")
        file.write("Departments:\n")
        file.write(f"{', '.join(sorted(departments))}\n\n")
        file.write("Students per Department:\n")
        for dept, count in sorted(departments.items()):
            file.write(f"{dept}: {count}\n")

    print("Class statistics exported to class_statistics.txt.")

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
        "8. Generate Class Report\n"
        "9. Export Statistics\n"
        "10. Exit\n\n"
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
        generate_class_report()
    elif choice == "9":
        export_class_statistics()
    elif choice == "10":
        print("Thank you for using the Student Profile Manager.")
        break
    else:
        print("Invalid Choice. Please pick 1-10.")

    print()
