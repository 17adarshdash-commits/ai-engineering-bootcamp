import json
import os

EMPLOYEES_FILE = "employees.json"

employees = {}


def load_employees():
    """Load employees from EMPLOYEES_FILE into the employees dict, if it exists."""
    if not os.path.exists(EMPLOYEES_FILE):
        return

    with open(EMPLOYEES_FILE, "r") as f:
        data = json.load(f)

    for employee in data:
        employees[int(employee["id"])] = employee


def save_employees():
    """Write all employees to EMPLOYEES_FILE."""
    with open(EMPLOYEES_FILE, "w") as f:
        json.dump(list(employees.values()), f, indent=4)


def add_employee():
    try:
        employee_id = int(input("Enter Employee ID: ").strip())
    except ValueError:
        print("Employee ID must be a number.")
        return

    if employee_id in employees:
        print("ID already exists.")
        return

    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    department = input("Enter Department: ").strip()
    if not department:
        print("Department cannot be empty.")
        return

    position = input("Enter Position: ").strip()
    if not position:
        print("Position cannot be empty.")
        return

    try:
        salary = float(input("Enter Salary: ").strip())
    except ValueError:
        print("Salary must be a number.")
        return

    if salary <= 0:
        print("Salary must be positive.")
        return

    employees[employee_id] = {
        "id": employee_id,
        "name": name,
        "department": department,
        "position": position,
        "salary": salary,
    }
    save_employees()
    print("Employee added successfully.")


def update_employee():
    try:
        employee_id = int(input("Enter Employee ID to update: ").strip())
    except ValueError:
        print("Employee ID must be a number.")
        return

    if employee_id not in employees:
        print("No employee found with that ID.")
        return

    employee = employees[employee_id]

    name = input(f"Enter new Name [{employee['name']}]: ").strip()
    if name:
        employee["name"] = name

    department = input(f"Enter new Department [{employee['department']}]: ").strip()
    if department:
        employee["department"] = department

    position = input(f"Enter new Position [{employee['position']}]: ").strip()
    if position:
        employee["position"] = position

    salary = input(f"Enter new Salary [{employee['salary']}]: ").strip()
    if salary:
        try:
            new_salary = float(salary)
        except ValueError:
            print("Invalid salary. Update to salary skipped.")
        else:
            if new_salary <= 0:
                print("Salary must be positive. Update to salary skipped.")
            else:
                employee["salary"] = new_salary

    save_employees()
    print("Employee updated successfully.")


def delete_employee():
    try:
        employee_id = int(input("Enter Employee ID to delete: ").strip())
    except ValueError:
        print("Employee ID must be a number.")
        return

    if employee_id not in employees:
        print("No employee found with that ID.")
        return

    del employees[employee_id]
    save_employees()
    print("Employee deleted successfully.")


def print_employee(employee):
    print("--------------------------------")
    print(f"ID         : {employee['id']}")
    print(f"Name       : {employee['name']}")
    print(f"Department : {employee['department']}")
    print(f"Position   : {employee['position']}")
    print(f"Salary     : {employee['salary']}")
    print("--------------------------------")


def print_employees(employee_list):
    if not employee_list:
        print("No employees to display.")
        return

    for employee in employee_list:
        print_employee(employee)


def display_employees():
    print_employees(employees.values())


def search_by_id():
    try:
        employee_id = int(input("Enter Employee ID to search: ").strip())
    except ValueError:
        print("Employee ID must be a number.")
        return

    employee = employees.get(employee_id)
    if employee is None:
        print("No employee found with that ID.")
        return

    print_employee(employee)


def search_by_name():
    query = input("Search by Name: ").strip().lower()
    found = [e for e in employees.values() if query in e["name"].lower()]
    print_employees(found)


def menu():
    print("========== Employee Management System ==========")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Search by ID")
    print("5. Search by Name")
    print("6. Display All Employees")
    print("7. Exit")
    print("==================================================")


def main():
    load_employees()

    actions = {
        "1": add_employee,
        "2": update_employee,
        "3": delete_employee,
        "4": search_by_id,
        "5": search_by_name,
        "6": display_employees,
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
