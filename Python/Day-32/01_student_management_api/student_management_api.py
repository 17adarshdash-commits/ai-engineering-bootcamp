import json
import os

STUDENTS_FILE = "students.json"

GRADES = ("A", "B", "C", "D", "F")

students = {}


def load_students():
    """Load students from STUDENTS_FILE into the students dict, if it exists."""
    if not os.path.exists(STUDENTS_FILE):
        return

    with open(STUDENTS_FILE, "r") as f:
        data = json.load(f)

    for student in data:
        students[int(student["id"])] = student


def save_students():
    """Write all students to STUDENTS_FILE."""
    with open(STUDENTS_FILE, "w") as f:
        json.dump(list(students.values()), f, indent=4)


def add_student():
    try:
        student_id = int(input("Enter Student ID: ").strip())
    except ValueError:
        print("Student ID must be a number.")
        return

    if student_id in students:
        print("ID already exists.")
        return

    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter Age: ").strip())
    except ValueError:
        print("Age must be a number.")
        return

    grade = input(f"Enter Grade {GRADES}: ").strip().upper()
    if grade not in GRADES:
        print("Invalid grade.")
        return

    students[student_id] = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade,
    }
    save_students()
    print("Student added successfully.")


def update_student():
    try:
        student_id = int(input("Enter Student ID to update: ").strip())
    except ValueError:
        print("Student ID must be a number.")
        return

    if student_id not in students:
        print("No student found with that ID.")
        return

    student = students[student_id]

    name = input(f"Enter new Name [{student['name']}]: ").strip()
    if name:
        student["name"] = name

    age = input(f"Enter new Age [{student['age']}]: ").strip()
    if age:
        try:
            student["age"] = int(age)
        except ValueError:
            print("Invalid age. Update to age skipped.")

    grade = input(f"Enter new Grade {GRADES} [{student['grade']}]: ").strip().upper()
    if grade:
        if grade not in GRADES:
            print("Invalid grade. Update to grade skipped.")
        else:
            student["grade"] = grade

    save_students()
    print("Student updated successfully.")


def delete_student():
    try:
        student_id = int(input("Enter Student ID to delete: ").strip())
    except ValueError:
        print("Student ID must be a number.")
        return

    if student_id not in students:
        print("No student found with that ID.")
        return

    del students[student_id]
    save_students()
    print("Student deleted successfully.")


def print_student(student):
    print("--------------------------------")
    print(f"ID    : {student['id']}")
    print(f"Name  : {student['name']}")
    print(f"Age   : {student['age']}")
    print(f"Grade : {student['grade']}")
    print("--------------------------------")


def print_students(student_list):
    if not student_list:
        print("No students to display.")
        return

    for student in student_list:
        print_student(student)


def display_students():
    print_students(students.values())


def search_by_id():
    try:
        student_id = int(input("Enter Student ID to search: ").strip())
    except ValueError:
        print("Student ID must be a number.")
        return

    student = students.get(student_id)
    if student is None:
        print("No student found with that ID.")
        return

    print_student(student)


def search_by_name():
    query = input("Search by Name: ").strip().lower()
    found = [s for s in students.values() if query in s["name"].lower()]
    print_students(found)


def menu():
    print("========== Student Management API ==========")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search by ID")
    print("5. Search by Name")
    print("6. Display All Students")
    print("7. Exit")
    print("==============================================")


def main():
    load_students()

    actions = {
        "1": add_student,
        "2": update_student,
        "3": delete_student,
        "4": search_by_id,
        "5": search_by_name,
        "6": display_students,
    }

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action()


if __name__ == "__main__":
    main()
