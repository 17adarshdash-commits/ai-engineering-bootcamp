"""
exceptions.py

Custom exceptions used across the employee management system.
"""


class EmployeeError(Exception):
    """Base exception for all employee-related errors."""


class DuplicateEmployeeIDError(EmployeeError):
    """Raised when an employee ID already exists."""


class InvalidNameError(EmployeeError):
    """Raised when an employee name is empty/blank."""


class InvalidDepartmentError(EmployeeError):
    """Raised when a department is empty/blank."""


class InvalidPositionError(EmployeeError):
    """Raised when a position is empty/blank."""


class InvalidSalaryError(EmployeeError):
    """Raised when a salary is not a positive number."""


class InvalidJoiningDateError(EmployeeError):
    """Raised when a joining date is not in YYYY-MM-DD format."""


class EmployeeNotFoundError(EmployeeError):
    """Raised when an employee ID cannot be found."""
