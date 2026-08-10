"""
main.py

Command-line interface for the Course Management System.
"""

from course_manager import CourseManager
from exceptions import CourseError

DATA_FILE = "courses.json"

MENU = """
============ Course Management System ============
1. Add Course
2. Update Course
3. Delete Course
4. Search Course
5. Display Courses
6. Filter by Department
7. Save Courses to JSON
8. Load Courses from JSON
9. Exit
====================================================
"""


def add_course(manager):
    course_id = input("Enter course ID: ").strip()
    course_name = input("Enter course name: ").strip()
    instructor = input("Enter instructor name: ").strip()
    credits = input("Enter credits: ").strip()
    department = input("Enter department: ").strip()
    capacity = input("Enter capacity: ").strip()

    try:
        manager.add_course(course_id, course_name, instructor, credits, department, capacity)
        print("Course added successfully.")
    except CourseError as e:
        print(f"Error: {e}")


def update_course(manager):
    course_id = input("Enter course ID to update: ").strip()
    print("Leave a field blank to keep its current value.")
    course_name = input("New course name: ").strip()
    instructor = input("New instructor name: ").strip()
    credits = input("New credits: ").strip()
    department = input("New department: ").strip()
    capacity = input("New capacity: ").strip()

    updates = {}
    if course_name:
        updates["course_name"] = course_name
    if instructor:
        updates["instructor"] = instructor
    if credits:
        updates["credits"] = credits
    if department:
        updates["department"] = department
    if capacity:
        updates["capacity"] = capacity

    try:
        course = manager.update_course(course_id, **updates)
        print(f"Course updated: {course}")
    except CourseError as e:
        print(f"Error: {e}")


def delete_course(manager):
    course_id = input("Enter course ID to delete: ").strip()
    try:
        manager.delete_course(course_id)
        print("Course deleted successfully.")
    except CourseError as e:
        print(f"Error: {e}")


def search_course(manager):
    keyword = input("Enter search keyword (ID/name/instructor): ").strip()
    results = manager.search_course(keyword)
    if not results:
        print("No matching courses found.")
        return

    for course in results:
        print(course)


def display_courses(manager):
    manager.display_courses()


def filter_by_department(manager):
    department = input("Enter department: ").strip()
    results = manager.filter_by_department(department)
    if not results:
        print("No courses found in that department.")
        return

    for course in results:
        print(course)


def save_courses(manager):
    filepath = input(f"Enter filepath to save [{DATA_FILE}]: ").strip() or DATA_FILE
    manager.save_to_json(filepath)
    print(f"Courses saved to '{filepath}'.")


def load_courses(manager):
    filepath = input(f"Enter filepath to load [{DATA_FILE}]: ").strip() or DATA_FILE
    try:
        manager.load_from_json(filepath)
        print(f"Courses loaded from '{filepath}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")


def main():
    manager = CourseManager()

    actions = {
        "1": add_course,
        "2": update_course,
        "3": delete_course,
        "4": search_course,
        "5": display_courses,
        "6": filter_by_department,
        "7": save_courses,
        "8": load_courses,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "9":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action(manager)


if __name__ == "__main__":
    main()
