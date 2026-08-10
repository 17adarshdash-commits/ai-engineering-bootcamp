"""
course_manager.py

Defines the CourseManager class - handles course creation, updates,
deletion, search, display, department filtering, and JSON persistence for
a collection of Course objects.
"""

import json
import os

from course import Course, Department
from exceptions import (
    DuplicateCourseIDError,
    InvalidCourseNameError,
    InvalidInstructorError,
    InvalidCreditsError,
    InvalidCapacityError,
    InvalidDepartmentError,
    CourseNotFoundError,
)

VALID_DEPARTMENTS = tuple(department.value for department in Department)


class CourseManager:
    """Manages a collection of Course objects."""

    def __init__(self):
        self.courses = {}  # course_id -> Course

    # ------------------------------------------------------------------
    # Validation helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _validate_course_name(course_name):
        if not course_name or not course_name.strip():
            raise InvalidCourseNameError("Course name cannot be empty.")

    @staticmethod
    def _validate_instructor(instructor):
        if not instructor or not instructor.strip():
            raise InvalidInstructorError("Instructor name cannot be empty.")

    @staticmethod
    def _validate_credits(credits):
        try:
            credits = float(credits)
        except (TypeError, ValueError):
            raise InvalidCreditsError("Credits must be a number.")
        if credits <= 0:
            raise InvalidCreditsError("Credits must be greater than 0.")
        return credits

    @staticmethod
    def _validate_capacity(capacity):
        try:
            capacity = int(capacity)
        except (TypeError, ValueError):
            raise InvalidCapacityError("Capacity must be an integer.")
        if capacity <= 0:
            raise InvalidCapacityError("Capacity must be greater than 0.")
        return capacity

    @staticmethod
    def _validate_department(department):
        if department not in VALID_DEPARTMENTS:
            raise InvalidDepartmentError(
                f"Department must be one of {VALID_DEPARTMENTS}, got: '{department}'."
            )

    # ------------------------------------------------------------------
    # Course creation / mutation
    # ------------------------------------------------------------------
    def add_course(self, course_id, course_name, instructor, credits, department, capacity):
        """Add a new course after validating all fields."""
        if course_id in self.courses:
            raise DuplicateCourseIDError(f"Course ID '{course_id}' already exists.")

        self._validate_course_name(course_name)
        self._validate_instructor(instructor)
        credits = self._validate_credits(credits)
        self._validate_department(department)
        capacity = self._validate_capacity(capacity)

        course = Course(
            course_id=course_id,
            course_name=course_name.strip(),
            instructor=instructor.strip(),
            credits=credits,
            department=department,
            capacity=capacity,
        )
        self.courses[course_id] = course
        return course

    def update_course(self, course_id, **updates):
        """Update one or more fields of an existing course."""
        course = self._get_course_or_raise(course_id)

        if "course_name" in updates:
            self._validate_course_name(updates["course_name"])
            course.course_name = updates["course_name"].strip()
        if "instructor" in updates:
            self._validate_instructor(updates["instructor"])
            course.instructor = updates["instructor"].strip()
        if "credits" in updates:
            course.credits = self._validate_credits(updates["credits"])
        if "department" in updates:
            self._validate_department(updates["department"])
            course.department = updates["department"]
        if "capacity" in updates:
            course.capacity = self._validate_capacity(updates["capacity"])

        return course

    def delete_course(self, course_id):
        """Delete a course by its ID."""
        self._get_course_or_raise(course_id)
        del self.courses[course_id]

    # ------------------------------------------------------------------
    # Search / display
    # ------------------------------------------------------------------
    def search_course(self, keyword):
        """Search courses by ID, name, or instructor (case-insensitive substring match)."""
        keyword = str(keyword).strip().lower()
        return [
            course
            for course in self.courses.values()
            if keyword in str(course.course_id).lower()
            or keyword in course.course_name.lower()
            or keyword in course.instructor.lower()
        ]

    def filter_by_department(self, department):
        """Return all courses belonging to the given department."""
        return [course for course in self.courses.values() if course.department == department]

    def display_courses(self):
        """Print all courses to the console."""
        if not self.courses:
            print("No courses to display.")
            return

        for course in self.courses.values():
            print(course)

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def save_to_json(self, filepath):
        """Save all courses to a JSON file."""
        data = [course.to_dict() for course in self.courses.values()]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filepath):
        """Load courses from a JSON file, replacing the current collection."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"No such file: '{filepath}'")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.courses = {}
        for item in data:
            course = Course.from_dict(item)
            self.courses[course.course_id] = course

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _get_course_or_raise(self, course_id):
        if course_id not in self.courses:
            raise CourseNotFoundError(f"Course ID '{course_id}' not found.")
        return self.courses[course_id]
