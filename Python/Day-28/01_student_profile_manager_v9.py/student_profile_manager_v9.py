import os
import csv
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(SCRIPT_DIR, "students.txt")
REPORT_FILE = os.path.join(SCRIPT_DIR, "class_report.txt")
BACKUP_FILE = os.path.join(SCRIPT_DIR, "students_backup.txt")
DEPARTMENT_REPORT_FILE = os.path.join(SCRIPT_DIR, "department_report.txt")
CSV_FILE = os.path.join(SCRIPT_DIR, "students_export.csv")
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
TOP_PERFORMERS_COUNT = 5

GPA_DISTRIBUTION_BANDS = [
    ("Outstanding", 9.0),
    ("Excellent", 8.0),
    ("Good", 7.0),
    ("Average", 6.0),
    ("Poor", 0.0),
]


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


def find_student_by_roll(roll_no):
    for name, info in students.items():
        if info["roll_no"] == roll_no:
            return name, info
    return None, None


def notify_if_empty():
    if not students:
        print("Student Profile Manager is empty.\n")
        return True
    return False


def display_student(name, info):
    print(f"Name: {name}\nAge: {info['age']}\nRoll Number: {info['roll_no']}\nDepartment: {info['dept']}\nGPA: {info['gpa']}\nDate Added: {info['date_added']}")
    print("-----------------")


def display_student_labeled(title, name, info):
    print(f"\n{format_header(title, 10)}\n")
    print(f"Roll Number : {info['roll_no']}")
    print(f"Name        : {name}")
    print(f"Department  : {info['dept']}")
    print(f"Age         : {info['age']}")
    print(f"GPA         : {info['gpa']}")


def display_student_card(name, info):
    print("-" * 30 + "\n")
    print(f"Name : {name}")
    print(f"Roll : {info['roll_no']}")
    print(f"Department : {info['dept']}")
    print(f"GPA : {info['gpa']}")
    print()


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
            print("Roll number already exists.")
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


def get_gpa_threshold():
    while True:
        try:
            return float(input("Enter minimum GPA: "))
        except ValueError:
            print("GPA must be a number.")


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
    if notify_if_empty():
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


def get_grouped_department_counts():
    departments = {}
    for info in students.values():
        dept = info["dept"] if info["dept"] in KNOWN_DEPARTMENTS else "Other"
        departments[dept] = departments.get(dept, 0) + 1
    return departments


def get_gpa_distribution():
    distribution = {band: 0 for band, _ in GPA_DISTRIBUTION_BANDS}
    for info in students.values():
        gpa = info["gpa"]
        for band, threshold in GPA_DISTRIBUTION_BANDS:
            if gpa >= threshold:
                distribution[band] += 1
                break
    return distribution


def get_department_average_gpa():
    totals = {}
    counts = {}
    for info in students.values():
        dept = info["dept"]
        totals[dept] = totals.get(dept, 0) + info["gpa"]
        counts[dept] = counts.get(dept, 0) + 1
    return {dept: totals[dept] / counts[dept] for dept in totals}


def search_by_roll():
    if notify_if_empty():
        return
    try:
        roll_no = int(input("Enter Roll Number: ").strip())
    except ValueError:
        print("Roll Number must be an integer.")
        return
    name, info = find_student_by_roll(roll_no)
    if info is not None:
        display_student(name, info)
    else:
        print("Student not found.")


def search_by_name():
    if notify_if_empty():
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
    if notify_if_empty():
        return
    dept_query = input("Enter department: ").strip().lower()
    matches = [(name, info) for name, info in students.items() if info["dept"].lower() == dept_query]
    if not matches:
        print("No students found.")
        return
    for name, info in sorted(matches, key=lambda item: item[1]["roll_no"]):
        display_student_card(name, info)


def search_student():
    while True:
        choice = input(
            f"\n{format_header('Search Student')}\n"
            "1. Search by Roll Number\n"
            "2. Search by Name\n"
            "3. Search by Department\n"
            "4. Return\n\n"
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
            "5. GPA Distribution\n"
            "6. Department Average GPA\n"
            "7. Return\n\n"
            "Enter your choice: "
        )

        if choice in ("1", "2", "3", "4", "5", "6") and notify_if_empty():
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
            display_gpa_distribution()
        elif choice == "6":
            display_department_average_gpa()
        elif choice == "7":
            break
        else:
            print("Invalid Choice. Please pick 1-7.")


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
            print("Roll number already exists.")
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
    if notify_if_empty():
        return
    ranked = sorted(students.items(), key=lambda item: item[1]["gpa"], reverse=True)
    for name, info in ranked:
        print(f"{name:<9}{info['gpa']}\n")


def sort_alphabetically():
    if notify_if_empty():
        return
    for name, _ in sorted(students.items()):
        print(f"{name}\n")


def generate_class_report():
    if notify_if_empty():
        return

    highest_name, highest_info = get_highest_gpa_student()
    lowest_name, lowest_info = get_lowest_gpa_student()
    average_gpa = get_average_gpa()
    newest_name = max(students, key=lambda n: students[n]["date_added"])
    newest_info = students[newest_name]
    oldest_name, oldest_info = get_oldest_student()
    youngest_name, youngest_info = get_youngest_student()

    departments = get_grouped_department_counts()
    distribution = get_gpa_distribution()

    width = 30
    label_width = max(
        [len("Total Students"), len("Average GPA"), len("Highest GPA"), len("Lowest GPA")]
        + [len(dept) for dept in departments]
    )

    with open(REPORT_FILE, "w") as file:
        file.write("=" * width + "\n\n")
        file.write("CLASS REPORT\n\n")
        file.write("=" * width + "\n\n")

        file.write(f"{'Total Students':<{label_width}} : {len(students)}\n\n")
        file.write(f"{'Average GPA':<{label_width}} : {average_gpa:.2f}\n\n")
        file.write(f"{'Highest GPA':<{label_width}} : {highest_info['gpa']:.2f}\n\n")
        file.write(f"{'Lowest GPA':<{label_width}} : {lowest_info['gpa']:.2f}\n\n")

        file.write("Departments\n\n")
        for dept, count in sorted(departments.items()):
            file.write(f"{dept:<{label_width}} : {count}\n\n")

        file.write("GPA Distribution\n\n")
        for band, _ in GPA_DISTRIBUTION_BANDS:
            file.write(f"{band:<{label_width}} : {distribution[band]}\n\n")

        file.write("=" * width + "\n\n")

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
    if notify_if_empty():
        return
    recent = sorted(students.items(), key=lambda item: item[1]["date_added"], reverse=True)[:RECENT_STUDENTS_COUNT]
    for name, info in recent:
        print(f"Roll: {info['roll_no']}")
        print(f"Name: {name}")
        print(f"Department: {info['dept']}")
        print(f"Date Added: {info['date_added']}")
        print("-----------------")


def export_to_csv():
    if notify_if_empty():
        return
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll", "Name", "Age", "Department", "GPA", "Date Added"])
        for name, info in sorted(students.items(), key=lambda item: item[1]["roll_no"]):
            writer.writerow([info["roll_no"], name, info["age"], info["dept"], info["gpa"], info["date_added"]])
    print("Student data exported successfully.")


def display_gpa_filter_results(min_gpa):
    matches = [(name, info) for name, info in students.items() if info["gpa"] >= min_gpa]
    if not matches:
        print("No students found.")
        return
    print(f"{'Roll':<7}{'Name':<9}{'GPA'}")
    for name, info in sorted(matches, key=lambda item: item[1]["gpa"], reverse=True):
        print(f"{info['roll_no']:<7}{name:<9}{info['gpa']}")


def gpa_filter_menu():
    while True:
        choice = input(
            f"\n{format_header('GPA Filter')}\n\n"
            "1. GPA >= 9.0\n"
            "2. GPA >= 8.0\n"
            "3. GPA >= 7.0\n"
            "4. Custom GPA\n"
            "5. Return\n\n"
            "Enter your choice: "
        )

        if choice in ("1", "2", "3", "4") and notify_if_empty():
            continue

        if choice == "1":
            display_gpa_filter_results(9.0)
        elif choice == "2":
            display_gpa_filter_results(8.0)
        elif choice == "3":
            display_gpa_filter_results(7.0)
        elif choice == "4":
            min_gpa = get_gpa_threshold()
            display_gpa_filter_results(min_gpa)
        elif choice == "5":
            break
        else:
            print("Invalid Choice. Please pick 1-5.")


def top_performers():
    if notify_if_empty():
        return
    top = sorted(students.items(), key=lambda item: item[1]["gpa"], reverse=True)[:TOP_PERFORMERS_COUNT]
    print(f"\n{format_header(f'TOP {len(top)} STUDENTS')}\n")
    for rank, (name, info) in enumerate(top, start=1):
        print(f"{rank}. {name:<10}{info['gpa']}")


def dashboard_highest_gpa():
    if notify_if_empty():
        return
    name, info = get_highest_gpa_student()
    display_student_labeled("Highest GPA Student", name, info)


def dashboard_lowest_gpa():
    if notify_if_empty():
        return
    name, info = get_lowest_gpa_student()
    display_student_labeled("Lowest GPA Student", name, info)


def dashboard_average_gpa():
    if not students:
        print("No students available.")
        return
    print(f"Average GPA : {get_average_gpa():.2f}")


def dashboard_department_statistics():
    if not students:
        print("No students available.")
        return
    print(f"{'Department':<20}{'Students'}\n")
    for dept, count in sorted(get_grouped_department_counts().items()):
        print(f"{dept:<20}{count:>5}")


def display_gpa_distribution():
    if notify_if_empty():
        return
    print(f"\n{format_header('GPA Distribution')}\n")
    for band, count in get_gpa_distribution().items():
        print(f"{band:<12}: {count}")


def display_department_average_gpa():
    if notify_if_empty():
        return
    print(f"\n{format_header('Department Average GPA')}\n")
    print(f"{'Department':<20}{'Average GPA'}\n")
    for dept, avg in sorted(get_department_average_gpa().items()):
        print(f"{dept:<20}{avg:.2f}")


def student_dashboard():
    while True:
        choice = input(
            f"\n{format_header('Student Dashboard')}\n\n"
            "1. Highest GPA\n"
            "2. Lowest GPA\n"
            "3. Average GPA\n"
            "4. Department Statistics\n"
            "5. GPA Distribution\n"
            "6. Department Average GPA\n"
            "7. Return\n\n"
            "Enter your choice: "
        )

        if choice == "1":
            dashboard_highest_gpa()
        elif choice == "2":
            dashboard_lowest_gpa()
        elif choice == "3":
            dashboard_average_gpa()
        elif choice == "4":
            dashboard_department_statistics()
        elif choice == "5":
            display_gpa_distribution()
        elif choice == "6":
            display_department_average_gpa()
        elif choice == "7":
            break
        else:
            print("Invalid Choice. Please pick 1-7.")


while True:
    choice = input(
        f"{format_header('Student Profile Manager')}\n"
        "1. Add Student\n"
        "2. View Students\n"
        "3. Search by Department\n"
        "4. Update Student\n"
        "5. Delete Student\n"
        "6. Sort by GPA\n"
        "7. Sort Alphabetically\n"
        "8. Search Student (Roll/Name/Department)\n"
        "9. Statistics\n"
        "10. Generate Class Report\n"
        "11. Backup Data\n"
        "12. Restore Backup\n"
        "13. Department Reports\n"
        "14. Recent Students\n"
        "15. Export to CSV\n"
        "16. GPA Filter\n"
        "17. Top Performers\n"
        "18. Student Dashboard\n"
        "19. GPA Distribution\n"
        "20. Department Average GPA\n"
        "21. Exit\n\n"
        "Enter your choice: "
    )

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_by_department()
    elif choice == "4":
        edit_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        sort_by_gpa()
    elif choice == "7":
        sort_alphabetically()
    elif choice == "8":
        search_student()
    elif choice == "9":
        statistics_menu()
    elif choice == "10":
        generate_class_report()
    elif choice == "11":
        backup_data()
    elif choice == "12":
        restore_backup()
    elif choice == "13":
        department_reports_menu()
    elif choice == "14":
        recent_students()
    elif choice == "15":
        export_to_csv()
    elif choice == "16":
        gpa_filter_menu()
    elif choice == "17":
        top_performers()
    elif choice == "18":
        student_dashboard()
    elif choice == "19":
        display_gpa_distribution()
    elif choice == "20":
        display_department_average_gpa()
    elif choice == "21":
        print("Thank you for using the Student Profile Manager.")
        break
    else:
        print("Invalid Choice. Please pick 1-21.")

    print()
