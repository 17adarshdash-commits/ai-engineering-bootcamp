"""
exceptions.py

Custom exceptions used across the course management system.
"""


class CourseError(Exception):
    """Base exception for all course-related errors."""


class DuplicateCourseIDError(CourseError):
    """Raised when a course ID already exists."""


class InvalidCourseNameError(CourseError):
    """Raised when a course name is empty/blank."""


class InvalidInstructorError(CourseError):
    """Raised when an instructor name is empty/blank."""


class InvalidCreditsError(CourseError):
    """Raised when credits is not a positive number."""


class InvalidCapacityError(CourseError):
    """Raised when capacity is not a positive integer."""


class InvalidDepartmentError(CourseError):
    """Raised when a department is not one of the valid departments."""


class CourseNotFoundError(CourseError):
    """Raised when a course ID cannot be found."""
