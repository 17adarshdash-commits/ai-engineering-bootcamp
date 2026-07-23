import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(SCRIPT_DIR, "students.txt")
REPORT_FILE = os.path.join(SCRIPT_DIR, "class_report.txt")
BACKUP_FILE = os.path.join(SCRIPT_DIR, "students_backup.txt")
DEPARTMENT_REPORT_FILE = os.path.join(SCRIPT_DIR, "department_report.txt")
DATE_FORMAT = "%Y-%m-%d"

MIN_AGE = 15
MAX_AGE = 100

MIN_GPA = 0.0
MAX_GPA = 10.0

DEPARTMENT_CHOICES = {
    "1": "CSE AI",
    "2": "CSE Core",
    "3": "ECE",
    "4": "Other",
}

KNOWN_DEPARTMENTS = {"CSE AI", "CSE Core", "ECE"}

RECENT_STUDENTS_COUNT = 5


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


def format_header(title, width=5):
    return f"{'=' * width} {title} {'=' * width}"


def write_section_header(file, title, width=10):
    file.write(f"{format_header(title, width)}\n\n")


def write_student_block(file, title, name, info, fields):
    file.write(f"{title}\n\n")
    for label, key in fields:
        value = name if key == "name" else info[key]
        file.write(f"{label}: {value}\n")
    file.write("\n--------------------------------\n\n")


def find_student(name):
    return students.get(name)


def display_student(name, info):
    print(f"Name: {name}\nAge: {info['age']}\nRoll Number: {info['roll_no']}\nDepartment: {info['dept']}\nGPA: {info['gpa']}\nDate Added: {info['date_added']}")
    print("-----------------")


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
        if age < MIN_AGE or age > MAX_AGE:
            print(f"Must be between {MIN_AGE} and {MAX_AGE}.")
            continue
        return age


def get_valid_department():
    while True:
        dept = input("Enter Department: ").strip()
        if not dept:
            print("Department cannot be empty.")
            continue
        return dept


def get_unique_roll_number(exclude_name=None):
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
        if gpa < MIN_GPA or gpa > MAX_GPA:
            print(f"Must be between {MIN_GPA} and {MAX_GPA}.")
            continue
        return gpa


def add_student():
    name = get_valid_name()
    if name is None:
        return

    age = get_valid_age()
    roll_no = get_unique_roll_number()
    dept = get_valid_department()
    gpa = get_valid_gpa()
    date_added = datetime.now().strftime(DATE_FORMAT)

    students[name] = {'age': age, 'roll_no': roll_no, 'dept': dept, 'gpa': gpa, 'date_added': date_added}
    save_students()
    print("Student added successfully.")


def view_students():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    for name, info in students.items():
        display_student(name, info)


def get_average_gpa():
    return sum(info["gpa"] for info in students.values()) / len(students)


def get_highest_gpa_student():
    name = max(students, key=lambda n: students[n]["gpa"])
    return name, students[name]


def get_lowest_gpa_student():
    name = min(students, key=lambda n: students[n]["gpa"])
    return name, students[name]


def get_oldest_student():
    name = max(students, key=lambda n: students[n]["age"])
    return name, students[name]


def get_youngest_student():
    name = min(students, key=lambda n: students[n]["age"])
    return name, students[name]


def get_department_counts():
    departments = {}
    for info in students.values():
        departments[info["dept"]] = departments.get(info["dept"], 0) + 1
    return departments


def search_by_roll():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    try:
        roll_no = int(input("Enter Roll Number: ").strip())
    except ValueError:
        print("Roll Number must be an integer.")
        return
    for name, info in students.items():
        if info["roll_no"] == roll_no:
            display_student(name, info)
            return
    print("Student not found.")


def search_by_name():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    query = input("Enter Name: ").strip().lower()
    found = False
    for name, info in students.items():
        if query in name.lower():
            display_student(name, info)
            found = True
    if not found:
        print("Student not found.")


def search_by_department():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    dept_query = input("Enter Department: ").strip().lower()
    found = False
    for name, info in students.items():
        if info["dept"].lower() == dept_query:
            display_student(name, info)
            found = True
    if not found:
        print("Student not found.")


def search_student():
    while True:
        choice = input(
            f"\n{format_header('Search Student')}\n"
            "1. Search by Roll Number\n"
            "2. Search by Name\n"
            "3. Search by Department\n"
            "4. Back\n\n"
            "Enter your choice: "
        )

        if choice == "1":
            search_by_roll()
        elif choice == "2":
            search_by_name()
        elif choice == "3":
            search_by_department()
        elif choice == "4":
            break
        else:
            print("Invalid Choice. Please pick 1-4.")


def statistics_menu():
    while True:
        choice = input(
            f"\n{format_header('Statistics')}\n"
            "1. Average GPA\n"
            "2. Highest GPA\n"
            "3. Lowest GPA\n"
            "4. Students Per Department\n"
            "5. Return\n\n"
            "Enter your choice: "
        )

        if choice in ("1", "2", "3", "4") and not students:
            print("Student Profile Manager is empty.\n")
            continue

        if choice == "1":
            print(f"{get_average_gpa():.2f}")
        elif choice == "2":
            name, info = get_highest_gpa_student()
            display_student(name, info)
        elif choice == "3":
            name, info = get_lowest_gpa_student()
            display_student(name, info)
        elif choice == "4":
            for dept, count in sorted(get_department_counts().items()):
                print(f"{dept} : {count}")
        elif choice == "5":
            break
        else:
            print("Invalid Choice. Please pick 1-5.")


def backup_data():
    if not os.path.exists(DATA_FILE):
        print("No student data file found to back up.")
        return
    with open(DATA_FILE, "r") as source, open(BACKUP_FILE, "w") as backup:
        backup.write(source.read())
    print("Backup created successfully as students_backup.txt.")


def restore_backup():
    global students
    if not os.path.exists(BACKUP_FILE):
        print("No backup file found to restore.")
        return
    with open(BACKUP_FILE, "r") as backup:
        content = backup.read()
    with open(DATA_FILE, "w") as source:
        source.write(content)
    students = load_students()
    print("Backup restored successfully.")


def edit_student():
    name = input("Enter Name: ").strip()
    info = find_student(name)
    if info is None:
        print("Student not found.")
        return

    while True:
        age = input(f"Enter new Age (leave blank to keep '{info['age']}'): ").strip()
        if not age:
            break
        try:
            age = int(age)
        except ValueError:
            print("Age must be an integer.")
            continue
        if age < MIN_AGE or age > MAX_AGE:
            print(f"Must be between {MIN_AGE} and {MAX_AGE}.")
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
        if gpa < MIN_GPA or gpa > MAX_GPA:
            print(f"Must be between {MIN_GPA} and {MAX_GPA}.")
            continue
        info["gpa"] = gpa
        break

    save_students()
    print("Student updated successfully.")


def delete_student():
    name = input("Enter Name: ")
    if find_student(name) is not None:
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
        display_student(name, info)


def sort_alphabetically():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    for name, info in sorted(students.items()):
        display_student(name, info)


def generate_class_report():
    if not students:
        print("Student Profile Manager is empty.\n")
        return

    highest_name, highest_info = get_highest_gpa_student()
    lowest_name, lowest_info = get_lowest_gpa_student()
    average_gpa = get_average_gpa()
    newest_name = max(students, key=lambda n: students[n]["date_added"])
    newest_info = students[newest_name]
    oldest_name, oldest_info = get_oldest_student()
    youngest_name, youngest_info = get_youngest_student()

    departments = get_department_counts()

    with open(REPORT_FILE, "w") as file:
        write_section_header(file, "CLASS REPORT")
        file.write("Generated On:\n")
        file.write(f"{datetime.now().strftime(DATE_FORMAT)}\n\n")
        file.write("Total Students:\n")
        file.write(f"{len(students)}\n\n")
        file.write("Average GPA:\n")
        file.write(f"{average_gpa:.2f}\n\n")
        file.write("Highest GPA:\n")
        file.write(f"{highest_info['gpa']}\n\n")
        file.write("Lowest GPA:\n")
        file.write(f"{lowest_info['gpa']}\n\n")
        file.write("Students Per Department\n\n")
        for dept, count in sorted(departments.items()):
            file.write(f"{dept} : {count}\n")
        file.write("\n--------------------------------\n\n")

        write_student_block(
            file, "Top Performing Student", highest_name, highest_info,
            [("Roll", "roll_no"), ("Name", "name"), ("Department", "dept"), ("GPA", "gpa")]
        )

        write_student_block(
            file, "Newest Student", newest_name, newest_info,
            [("Roll", "roll_no"), ("Name", "name"), ("Department", "dept"), ("Date Added", "date_added")]
        )

        write_student_block(
            file, "Oldest Student", oldest_name, oldest_info,
            [("Roll", "roll_no"), ("Name", "name"), ("Age", "age")]
        )

        write_student_block(
            file, "Youngest Student", youngest_name, youngest_info,
            [("Roll", "roll_no"), ("Name", "name"), ("Age", "age")]
        )

        file.write("Complete Student List\n\n")
        file.write(f"{'Roll':<8}{'Name':<15}{'GPA':<7}{'Department':<15}{'Date Added'}\n\n")
        for name, info in sorted(students.items(), key=lambda item: item[1]["roll_no"]):
            file.write(
                f"{info['roll_no']:<8}{name:<15}{info['gpa']:<7}{info['dept']:<15}{info['date_added']}\n"
            )

    print("Class report generated to class_report.txt.")


def get_department_students(dept_name):
    if dept_name == "Other":
        return {n: i for n, i in students.items() if i["dept"] not in KNOWN_DEPARTMENTS}
    return {n: i for n, i in students.items() if i["dept"] == dept_name}


def generate_department_report(dept_name):
    dept_students = get_department_students(dept_name)
    if not dept_students:
        print(f"No students found in {dept_name}.")
        return

    average_gpa = sum(info["gpa"] for info in dept_students.values()) / len(dept_students)
    fields = [
        ("Roll", "roll_no"),
        ("Name", "name"),
        ("Age", "age"),
        ("Department", "dept"),
        ("GPA", "gpa"),
        ("Date Added", "date_added"),
    ]

    with open(DEPARTMENT_REPORT_FILE, "w") as file:
        write_section_header(file, f"{dept_name.upper()} REPORT")
        file.write("Generated On:\n")
        file.write(f"{datetime.now().strftime(DATE_FORMAT)}\n\n")
        file.write("Total Students:\n")
        file.write(f"{len(dept_students)}\n\n")
        file.write("Average GPA:\n")
        file.write(f"{average_gpa:.2f}\n\n")
        file.write("--------------------------------\n\n")
        for name, info in sorted(dept_students.items(), key=lambda item: item[1]["roll_no"]):
            for label, key in fields:
                value = name if key == "name" else info[key]
                file.write(f"{label}: {value}\n")
            file.write("\n")

    print(f"{dept_name} report generated to department_report.txt.")


def department_reports_menu():
    while True:
        choice = input(
            f"\n{format_header('Department Reports')}\n\n"
            "1. CSE AI\n"
            "2. CSE Core\n"
            "3. ECE\n"
            "4. Other\n"
            "5. Return\n\n"
            "Enter your choice: "
        )

        if choice in DEPARTMENT_CHOICES:
            generate_department_report(DEPARTMENT_CHOICES[choice])
        elif choice == "5":
            break
        else:
            print("Invalid Choice. Please pick 1-5.")


def recent_students():
    if not students:
        print("Student Profile Manager is empty.\n")
        return
    recent = sorted(students.items(), key=lambda item: item[1]["date_added"], reverse=True)[:RECENT_STUDENTS_COUNT]
    for name, info in recent:
        print(f"Roll: {info['roll_no']}")
        print(f"Name: {name}")
        print(f"Department: {info['dept']}")
        print(f"Date Added: {info['date_added']}")
        print("-----------------")


while True:
    choice = input(
        f"{format_header('Student Profile Manager')}\n"
        "1. Add Student\n"
        "2. View Students\n"
        "3. Search Student\n"
        "4. Edit Student\n"
        "5. Delete Student\n"
        "6. Sort by GPA\n"
        "7. Sort Alphabetically\n"
        "8. Generate Class Report\n"
        "9. Statistics\n"
        "10. Backup Data\n"
        "11. Restore Backup\n"
        "12. Department Reports\n"
        "13. Recent Students\n"
        "14. Exit\n\n"
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
        statistics_menu()
    elif choice == "10":
        backup_data()
    elif choice == "11":
        restore_backup()
    elif choice == "12":
        department_reports_menu()
    elif choice == "13":
        recent_students()
    elif choice == "14":
        print("Thank you for using the Student Profile Manager.")
        break
    else:
        print("Invalid Choice. Please pick 1-14.")

    print()
