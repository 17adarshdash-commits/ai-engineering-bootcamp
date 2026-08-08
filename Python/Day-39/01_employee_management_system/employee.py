"""
employee.py

Defines the Employee class - a single employee record with an ID, name,
department, position, salary, and joining date, plus conversion to/from
a plain dict so it can be (de)serialized to JSON.
"""


class Employee:
    """Represents a single employee."""

    def __init__(self, employee_id, name, department, position, salary, joining_date):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary
        self.joining_date = joining_date

    def to_dict(self):
        """Convert the Employee instance into a plain dictionary."""
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "position": self.position,
            "salary": self.salary,
            "joining_date": self.joining_date,
        }

    @classmethod
    def from_dict(cls, data):
        """Build an Employee instance from a plain dictionary."""
        return cls(
            employee_id=data["employee_id"],
            name=data["name"],
            department=data["department"],
            position=data["position"],
            salary=data["salary"],
            joining_date=data["joining_date"],
        )

    def __str__(self):
        return (
            f"ID: {self.employee_id} | Name: {self.name} | "
            f"Department: {self.department} | Position: {self.position} | "
            f"Salary: {self.salary:.2f} | Joined: {self.joining_date}"
        )

    def __repr__(self):
        return (
            f"Employee(employee_id={self.employee_id!r}, name={self.name!r}, "
            f"department={self.department!r}, position={self.position!r}, "
            f"salary={self.salary!r}, joining_date={self.joining_date!r})"
        )
