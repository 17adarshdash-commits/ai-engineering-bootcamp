"""
main.py

Command-line interface for the Student Database System.
"""

from database import Database
from student_manager import StudentError, StudentManager

MENU = """
============ Student Database System ============
1. Add Student
2. Update Student
3. Delete Student
4. Search Student
5. Display Students
6. Exit
===================================================
"""


def add_student(manager):
    student_id = input("Enter student ID: ").strip()
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()
    cgpa = input("Enter CGPA (0-10): ").strip()

    try:
        manager.add_student(student_id, name, age, course, cgpa)
        print("Student added successfully.")
    except StudentError as e:
        print(f"Error: {e}")


def update_student(manager):
    student_id = input("Enter student ID to update: ").strip()
    print("Leave a field blank to keep its current value.")
    name = input("New name: ").strip()
    age = input("New age: ").strip()
    course = input("New course: ").strip()
    cgpa = input("New CGPA: ").strip()

    updates = {}
    if name:
        updates["name"] = name
    if age:
        updates["age"] = age
    if course:
        updates["course"] = course
    if cgpa:
        updates["cgpa"] = cgpa

    try:
        student = manager.update_student(student_id, **updates)
        print(f"Student updated: {student}")
    except StudentError as e:
        print(f"Error: {e}")


def delete_student(manager):
    student_id = input("Enter student ID to delete: ").strip()
    try:
        manager.delete_student(student_id)
        print("Student deleted successfully.")
    except StudentError as e:
        print(f"Error: {e}")


def search_student(manager):
    keyword = input("Enter search keyword (ID/name/course): ").strip()
    results = manager.search_student(keyword)
    if not results:
        print("No matching students found.")
        return

    for student in results:
        print(student)


def display_students(manager):
    students = manager.display_students()
    if not students:
        print("No students to display.")
        return

    for student in students:
        print(student)


def main():
    database = Database()
    manager = StudentManager(database)

    actions = {
        "1": add_student,
        "2": update_student,
        "3": delete_student,
        "4": search_student,
        "5": display_students,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "6":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action(manager)


if __name__ == "__main__":
    main()
