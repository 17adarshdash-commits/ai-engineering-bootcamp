import os
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EMPLOYEES_FILE = os.path.join(BASE_DIR, "employees.txt")
REPORT_FILE = os.path.join(BASE_DIR, "employee_report.txt")
DELIMITER = "|"


def load_employees():
    if not os.path.exists(EMPLOYEES_FILE):
        return []
    employees = []
    with open(EMPLOYEES_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            employee_id, name, department, salary, date_added = line.split(DELIMITER)
            employees.append({
                "employee_id": employee_id,
                "name": name,
                "department": department,
                "salary": float(salary),
                "date_added": date_added,
            })
    return employees


def save_employees(employees):
    with open(EMPLOYEES_FILE, "w") as f:
        for emp in employees:
            f.write(DELIMITER.join([
                emp["employee_id"],
                emp["name"],
                emp["department"],
                str(emp["salary"]),
                emp["date_added"],
            ]) + "\n")


def add_employee(employees):
    employee_id = input("Employee ID: ").strip()
    if any(emp["employee_id"] == employee_id for emp in employees):
        print("Error: Employee ID already exists.")
        return

    name = input("Name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    department = input("Department: ").strip()

    salary_input = input("Salary: ").strip()
    try:
        salary = float(salary_input)
    except ValueError:
        print("Error: Salary must be a number.")
        return
    if salary <= 0:
        print("Error: Salary must be greater than 0.")
        return

    employee = {
        "employee_id": employee_id,
        "name": name,
        "department": department,
        "salary": salary,
        "date_added": date.today().isoformat(),
    }
    employees.append(employee)
    save_employees(employees)
    print(f"Employee '{name}' added successfully.")


def view_employees(employees):
    if not employees:
        print("No employees found.")
        return

    print(f"\n{'ID':<8}{'Name':<20}{'Department':<15}{'Salary':<12}{'Date Added':<12}")
    print("-" * 67)
    for emp in employees:
        print(
            f"{emp['employee_id']:<8}{emp['name']:<20}{emp['department']:<15}"
            f"{emp['salary']:<12.2f}{emp['date_added']:<12}"
        )


def search_employee(employees):
    if not employees:
        print("No employees found.")
        return

    print("1. Search by Employee ID")
    print("2. Search by Name")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        employee_id = input("Employee ID: ").strip()
        results = [emp for emp in employees if emp["employee_id"] == employee_id]
    elif choice == "2":
        name_query = input("Name (partial match): ").strip().lower()
        results = [emp for emp in employees if name_query in emp["name"].lower()]
    else:
        print("Invalid option.")
        return

    if not results:
        print("No matching employees found.")
        return

    for emp in results:
        print(
            f"ID: {emp['employee_id']} | Name: {emp['name']} | "
            f"Department: {emp['department']} | Salary: {emp['salary']:.2f} | "
            f"Date Added: {emp['date_added']}"
        )


def update_salary(employees):
    employee_id = input("Employee ID: ").strip()
    employee = next((emp for emp in employees if emp["employee_id"] == employee_id), None)
    if not employee:
        print("Error: Employee not found.")
        return

    salary_input = input("New Salary: ").strip()
    try:
        new_salary = float(salary_input)
    except ValueError:
        print("Error: Salary must be a number.")
        return
    if new_salary <= 0:
        print("Error: Salary must be greater than 0.")
        return

    employee["salary"] = new_salary
    save_employees(employees)
    print(f"Salary updated for '{employee['name']}'.")


def delete_employee(employees):
    employee_id = input("Employee ID: ").strip()
    employee = next((emp for emp in employees if emp["employee_id"] == employee_id), None)
    if not employee:
        print("Error: Employee not found.")
        return

    employees.remove(employee)
    save_employees(employees)
    print(f"Employee '{employee['name']}' deleted.")


def generate_report(employees):
    if not employees:
        print("No employees found. Report not generated.")
        return

    total_employees = len(employees)
    average_salary = sum(emp["salary"] for emp in employees) / total_employees
    highest_paid = max(employees, key=lambda emp: emp["salary"])

    departments = {}
    for emp in employees:
        departments[emp["department"]] = departments.get(emp["department"], 0) + 1

    lines = []
    lines.append("========== EMPLOYEE REPORT ==========\n")
    lines.append(f"Generated On: {date.today().isoformat()}\n")
    lines.append(f"Total Employees: {total_employees}\n")
    lines.append(f"Average Salary: {average_salary:.2f}\n")
    lines.append("Highest Paid Employee\n")
    lines.append(f"Name: {highest_paid['name']}\n")
    lines.append(f"Salary: {highest_paid['salary']:.2f}\n")
    lines.append("-" * 33 + "\n")
    lines.append("Employees Per Department\n")
    for dept, count in sorted(departments.items()):
        lines.append(f"{dept} : {count}\n")
    lines.append("-" * 33 + "\n")
    lines.append("Complete Employee List\n")
    for emp in employees:
        lines.append(
            f"{emp['employee_id']} | {emp['name']} | {emp['department']} | "
            f"{emp['salary']:.2f} | {emp['date_added']}\n"
        )

    with open(REPORT_FILE, "w") as f:
        f.writelines(lines)

    print(f"Report generated: {REPORT_FILE}")


def main():
    employees = load_employees()

    menu = (
        "\n===== Employee Manager =====\n"
        "1. Add Employee\n"
        "2. View Employees\n"
        "3. Search Employee\n"
        "4. Update Salary\n"
        "5. Delete Employee\n"
        "6. Generate Report\n"
        "7. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            view_employees(employees)
        elif choice == "3":
            search_employee(employees)
        elif choice == "4":
            update_salary(employees)
        elif choice == "5":
            delete_employee(employees)
        elif choice == "6":
            generate_report(employees)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
