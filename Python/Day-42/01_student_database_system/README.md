# Student Database System

A command-line student database system built as a multi-module Python
package, demonstrating SQLite persistence, parameterized queries, a
dataclass model, and validation - the same modular architecture used in
recent projects, with SQLite in place of JSON as the storage layer.

## Project Structure

```
01_student_database_system/
├── database.py         # Database - connection + automatic table creation
├── student.py           # Student dataclass (to_row/from_row for SQLite rows)
├── student_manager.py    # StudentManager - validated add/update/delete/search/display
├── main.py               # CLI entry point
├── students.db           # SQLite data file (created automatically on first run)
└── README.md
```

## Student Fields

- Student ID
- Name
- Age
- Course
- CGPA

## Features

- Create database and table automatically on startup
- Add Student
- Update Student
- Delete Student
- Search Student (by ID, name, or course)
- Display Students
- All reads/writes go straight to SQLite - no in-memory copy to keep in sync

## Validation

- Student IDs must be unique (`DuplicateStudentIDError`)
- Name cannot be empty (`InvalidNameError`)
- Age must be greater than 0 (`InvalidAgeError`)
- Course cannot be empty (`InvalidCourseError`)
- CGPA must be between 0 and 10 (`InvalidCGPAError`)
- Operating on a missing student ID raises `StudentNotFoundError`

All custom exceptions derive from a common `StudentError` base (defined in
`student_manager.py`), so the CLI can catch a single exception type for
user-facing error messages.

## SQL Safety

Every query in `student_manager.py` uses `?` placeholders for values -
never f-strings or string concatenation - so no user input can alter a
query's structure (SQL injection).

## Usage

```bash
cd 01_student_database_system
python main.py
```

Follow the on-screen menu to add students, update them, delete them,
search, and display all students. `students.db` is created automatically
the first time the program runs.
