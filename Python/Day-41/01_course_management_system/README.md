# Course Management System

A command-line course management system built as a multi-module Python
package, demonstrating dataclasses, enums, custom exceptions, validation
helpers, and JSON persistence.

## Project Structure

```
01_course_management_system/
├── course.py          # Department enum + Course dataclass (to_dict/from_dict for JSON)
├── course_manager.py  # CourseManager - add/update/delete/search/filter/display, persistence
├── exceptions.py      # Custom exception hierarchy
├── main.py            # CLI entry point
├── courses.json        # Default data file
└── README.md
```

## Course Fields

- Course ID
- Course Name
- Instructor
- Credits
- Department
- Capacity

## Features

- Add Course
- Update Course
- Delete Course
- Search Course (by ID, name, or instructor)
- Display Courses
- Filter by Department
- Save to JSON
- Load from JSON

## Validation

- Course IDs must be unique (`DuplicateCourseIDError`)
- Course name cannot be empty (`InvalidCourseNameError`)
- Instructor name cannot be empty (`InvalidInstructorError`)
- Credits must be greater than 0 (`InvalidCreditsError`)
- Capacity must be greater than 0 (`InvalidCapacityError`)
- Department must be one of the valid `Department` enum values
  (`InvalidDepartmentError`)
- Operating on a missing course ID raises `CourseNotFoundError`

Valid departments: `Computer Science`, `Mathematics`, `Physics`, `Business`,
`Arts` (defined in the `Department` enum in `course.py`).

All custom exceptions derive from a common `CourseError` base, so the CLI
can catch a single exception type for user-facing error messages.

## Usage

```bash
cd 01_course_management_system
python main.py
```

Follow the on-screen menu to add courses, update them, delete them, search,
display all courses, filter by department, and save/load data to/from
JSON.
