import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "attendance.txt")
REPORT_FILE = os.path.join(SCRIPT_DIR, "attendance_report.txt")


def load_records():
    records = []
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, status, date = [part.strip() for part in line.split(",")]
                records.append({"name": name, "status": status, "date": date})
    except FileNotFoundError:
        pass
    except ValueError:
        print("Warning: Data file is corrupted or contains invalid formats.")
    return records


def save_records():
    with open(DATA_FILE, "w") as file:
        for record in records:
            file.write(f"{record['name']}, {record['status']}, {record['date']}\n")


records = load_records()


def get_valid_name():
    while True:
        name = input("Student Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        return name


def get_valid_status():
    while True:
        status = input("Attendance (Present/Absent): ").strip().capitalize()
        if status not in ("Present", "Absent"):
            print("Attendance must be only Present or Absent.")
            continue
        return status


def mark_attendance():
    name = get_valid_name()
    status = get_valid_status()
    date = datetime.now().strftime("%Y-%m-%d")

    records.append({"name": name, "status": status, "date": date})
    save_records()
    print("Attendance marked successfully.")


def view_attendance():
    if not records:
        print("Attendance Manager is empty.\n")
        return
    for record in records:
        print("------------------------------\n")
        print(f"Name:\n{record['name']}\n")
        print(f"Status:\n{record['status']}\n")
        print(f"Date:\n{record['date']}\n")
    print("------------------------------")


def search_student():
    name = input("Search: ").strip().lower()
    matches = [record for record in records if record["name"].lower() == name]
    if not matches:
        print("Student not found.")
        return
    for record in matches:
        print("------------------------------\n")
        print(f"Name:\n{record['name']}\n")
        print(f"Status:\n{record['status']}\n")
        print(f"Date:\n{record['date']}\n")
    print("------------------------------")


def generate_report():
    if not records:
        print("Attendance Manager is empty.\n")
        return

    total = len(records)
    present = sum(1 for record in records if record["status"] == "Present")
    absent = total - present
    percentage = (present / total) * 100

    with open(REPORT_FILE, "w") as file:
        file.write("========== ATTENDANCE REPORT ==========\n\n")
        file.write("Generated On:\n")
        file.write(f"{datetime.now().strftime('%Y-%m-%d')}\n\n")
        file.write("Total Records:\n")
        file.write(f"{total}\n\n")
        file.write("Present:\n")
        file.write(f"{present}\n\n")
        file.write("Absent:\n")
        file.write(f"{absent}\n\n")
        file.write("Attendance Percentage:\n")
        file.write(f"{percentage:.2f}%\n\n")
        file.write("-----------------------\n\n")
        file.write("Student Records\n\n")
        for record in records:
            file.write(f"{record['name']}\n{record['status']}\n{record['date']}\n\n")

    print("Attendance report generated to attendance_report.txt.")


while True:
    choice = input(
        "===== Attendance Manager =====\n"
        "1. Mark Attendance\n"
        "2. View Attendance\n"
        "3. Search Student\n"
        "4. Generate Report\n"
        "5. Exit\n\n"
        "Enter your choice: "
    )

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        search_student()
    elif choice == "4":
        generate_report()
    elif choice == "5":
        print("Thank you for using the Attendance Manager.")
        break
    else:
        print("Invalid Choice. Please pick 1-5.")

    print()
