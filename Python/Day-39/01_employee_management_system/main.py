"""
main.py

Command-line interface for the Employee Management System.
"""

from employee_manager import EmployeeManager
from exceptions import EmployeeError

DATA_FILE = "employees.json"

MENU = """
========== Employee Management System ==========
1. Add Employee
2. Update Employee
3. Delete Employee
4. Search Employee
5. Display All Employees
6. Salary Summary
7. Employees by Department
8. Save Employees to JSON
9. Load Employees from JSON
10. Exit
==================================================
"""


def add_employee(manager):
    employee_id = input("Enter employee ID: ").strip()
    name = input("Enter name: ").strip()
    department = input("Enter department: ").strip()
    position = input("Enter position: ").strip()
    salary = input("Enter salary: ").strip()
    joining_date = input("Enter joining date (YYYY-MM-DD): ").strip()

    try:
        manager.add_employee(employee_id, name, department, position, salary, joining_date)
        print("Employee added successfully.")
    except EmployeeError as e:
        print(f"Error: {e}")


def update_employee(manager):
    employee_id = input("Enter employee ID to update: ").strip()
    print("Leave a field blank to keep it unchanged.")
    name = input("New name: ").strip() or None
    department = input("New department: ").strip() or None
    position = input("New position: ").strip() or None
    salary = input("New salary: ").strip() or None
    joining_date = input("New joining date (YYYY-MM-DD): ").strip() or None

    try:
        manager.update_employee(
            employee_id,
            name=name,
            department=department,
            position=position,
            salary=salary,
            joining_date=joining_date,
        )
        print("Employee updated successfully.")
    except EmployeeError as e:
        print(f"Error: {e}")


def delete_employee(manager):
    employee_id = input("Enter employee ID to delete: ").strip()
    try:
        manager.delete_employee(employee_id)
        print("Employee deleted successfully.")
    except EmployeeError as e:
        print(f"Error: {e}")


def search_employee(manager):
    keyword = input("Enter search keyword (ID/name/department/position): ").strip()
    results = manager.search_employee(keyword)
    if not results:
        print("No matching employees found.")
        return

    for employee in results:
        print(employee)


def display_employees(manager):
    manager.display_employees()


def salary_summary(manager):
    summary = manager.salary_summary()
    print(f"Total salary:   {summary['total']:.2f}")
    print(f"Average salary: {summary['average']:.2f}")
    print(f"Minimum salary: {summary['minimum']:.2f}")
    print(f"Maximum salary: {summary['maximum']:.2f}")


def employees_by_department(manager):
    grouped = manager.employees_by_department()
    if not grouped:
        print("No employees to summarize.")
        return

    for department, employees in grouped.items():
        print(f"\n{department} ({len(employees)}):")
        for employee in employees:
            print(f"  {employee}")


def save_employees(manager):
    filepath = input(f"Enter filepath to save [{DATA_FILE}]: ").strip() or DATA_FILE
    manager.save_to_json(filepath)
    print(f"Employees saved to '{filepath}'.")


def load_employees(manager):
    filepath = input(f"Enter filepath to load [{DATA_FILE}]: ").strip() or DATA_FILE
    try:
        manager.load_from_json(filepath)
        print(f"Employees loaded from '{filepath}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")


def main():
    manager = EmployeeManager()

    actions = {
        "1": add_employee,
        "2": update_employee,
        "3": delete_employee,
        "4": search_employee,
        "5": display_employees,
        "6": salary_summary,
        "7": employees_by_department,
        "8": save_employees,
        "9": load_employees,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "10":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action(manager)


if __name__ == "__main__":
    main()
