"""
employee_manager.py

Defines the EmployeeManager class - handles CRUD operations, search,
display, salary summary, department grouping, and JSON persistence for
a collection of Employee objects.
"""

import json
import os
from datetime import datetime

from employee import Employee
from exceptions import (
    DuplicateEmployeeIDError,
    InvalidNameError,
    InvalidDepartmentError,
    InvalidPositionError,
    InvalidSalaryError,
    InvalidJoiningDateError,
    EmployeeNotFoundError,
)

DATE_FORMAT = "%Y-%m-%d"


class EmployeeManager:
    """Manages a collection of Employee objects."""

    def __init__(self):
        self.employees = {}  # employee_id -> Employee

    # ------------------------------------------------------------------
    # Validation helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _validate_name(name):
        if not name or not name.strip():
            raise InvalidNameError("Name cannot be empty.")

    @staticmethod
    def _validate_department(department):
        if not department or not department.strip():
            raise InvalidDepartmentError("Department cannot be empty.")

    @staticmethod
    def _validate_position(position):
        if not position or not position.strip():
            raise InvalidPositionError("Position cannot be empty.")

    @staticmethod
    def _validate_salary(salary):
        try:
            salary = float(salary)
        except (TypeError, ValueError):
            raise InvalidSalaryError("Salary must be a number.")
        if salary <= 0:
            raise InvalidSalaryError("Salary must be greater than 0.")
        return salary

    @staticmethod
    def _validate_joining_date(joining_date):
        try:
            datetime.strptime(joining_date, DATE_FORMAT)
        except (TypeError, ValueError):
            raise InvalidJoiningDateError(
                f"Joining date must be in YYYY-MM-DD format, got: '{joining_date}'."
            )

    # ------------------------------------------------------------------
    # CRUD operations
    # ------------------------------------------------------------------
    def add_employee(self, employee_id, name, department, position, salary, joining_date):
        """Add a new employee after validating all fields."""
        if employee_id in self.employees:
            raise DuplicateEmployeeIDError(f"Employee ID '{employee_id}' already exists.")

        self._validate_name(name)
        self._validate_department(department)
        self._validate_position(position)
        salary = self._validate_salary(salary)
        self._validate_joining_date(joining_date)

        employee = Employee(
            employee_id,
            name.strip(),
            department.strip(),
            position.strip(),
            salary,
            joining_date,
        )
        self.employees[employee_id] = employee
        return employee

    def update_employee(
        self,
        employee_id,
        name=None,
        department=None,
        position=None,
        salary=None,
        joining_date=None,
    ):
        """Update fields of an existing employee. Only provided fields change."""
        employee = self._get_employee_or_raise(employee_id)

        if name is not None:
            self._validate_name(name)
            employee.name = name.strip()

        if department is not None:
            self._validate_department(department)
            employee.department = department.strip()

        if position is not None:
            self._validate_position(position)
            employee.position = position.strip()

        if salary is not None:
            employee.salary = self._validate_salary(salary)

        if joining_date is not None:
            self._validate_joining_date(joining_date)
            employee.joining_date = joining_date

        return employee

    def delete_employee(self, employee_id):
        """Delete an employee by ID."""
        self._get_employee_or_raise(employee_id)
        del self.employees[employee_id]

    def search_employee(self, keyword):
        """Search employees by ID, name, department, or position (case-insensitive substring match)."""
        keyword = str(keyword).strip().lower()
        results = [
            employee
            for employee in self.employees.values()
            if keyword in str(employee.employee_id).lower()
            or keyword in employee.name.lower()
            or keyword in employee.department.lower()
            or keyword in employee.position.lower()
        ]
        return results

    def display_employees(self):
        """Print all employees to the console."""
        if not self.employees:
            print("No employees to display.")
            return

        for employee in self.employees.values():
            print(employee)

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------
    def salary_summary(self):
        """Return total, average, minimum, and maximum salary across all employees."""
        if not self.employees:
            return {"total": 0, "average": 0, "minimum": 0, "maximum": 0}

        salaries = [employee.salary for employee in self.employees.values()]
        return {
            "total": sum(salaries),
            "average": sum(salaries) / len(salaries),
            "minimum": min(salaries),
            "maximum": max(salaries),
        }

    def employees_by_department(self):
        """Return a dict mapping department -> list of Employee objects."""
        grouped = {}
        for employee in self.employees.values():
            grouped.setdefault(employee.department, []).append(employee)
        return grouped

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def save_to_json(self, filepath):
        """Save all employees to a JSON file."""
        data = [employee.to_dict() for employee in self.employees.values()]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filepath):
        """Load employees from a JSON file, replacing the current collection."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"No such file: '{filepath}'")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.employees = {}
        for item in data:
            employee = Employee.from_dict(item)
            self.employees[employee.employee_id] = employee

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _get_employee_or_raise(self, employee_id):
        if employee_id not in self.employees:
            raise EmployeeNotFoundError(f"Employee ID '{employee_id}' not found.")
        return self.employees[employee_id]
