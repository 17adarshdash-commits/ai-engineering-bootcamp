# Employee Management System

A command-line employee management system built as a multi-module Python
package, demonstrating module/package organization, custom exceptions,
and JSON persistence.

## Project Structure

```
01_employee_management_system/
├── employee.py           # Employee data class (to_dict/from_dict for JSON)
├── employee_manager.py   # EmployeeManager - CRUD, search, summary, persistence
├── exceptions.py         # Custom exception hierarchy
├── main.py               # CLI entry point
├── employees.json        # Default data file
└── README.md
```

## Employee Fields

- Employee ID
- Name
- Department
- Position
- Salary
- Joining Date (`YYYY-MM-DD`)

## Features

- Add Employee
- Update Employee
- Delete Employee
- Search Employee (by ID, name, department, or position)
- Display Employees
- Salary Summary (total, average, minimum, maximum)
- Employees by Department
- Save to JSON
- Load from JSON

## Validation

- Employee IDs must be unique (`DuplicateEmployeeIDError`)
- Name cannot be empty (`InvalidNameError`)
- Department cannot be empty (`InvalidDepartmentError`)
- Position cannot be empty (`InvalidPositionError`)
- Salary must be a positive number (`InvalidSalaryError`)
- Joining date must match `YYYY-MM-DD` (`InvalidJoiningDateError`)
- Operating on a missing employee ID raises `EmployeeNotFoundError`

All custom exceptions derive from a common `EmployeeError` base, so the
CLI can catch a single exception type for user-facing error messages.

## Usage

```bash
cd 01_employee_management_system
python main.py
```

Follow the on-screen menu to add, update, delete, search, and display
employees, view the salary summary and department breakdown, and
save/load data to/from JSON.
