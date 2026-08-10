"""
course.py

Defines the Department enum and the Course dataclass - a single course with
an ID, name, instructor, credits, department, and capacity, plus conversion
to/from a plain dict so it can be (de)serialized to JSON.
"""

from dataclasses import dataclass
from enum import Enum


class Department(Enum):
    COMPUTER_SCIENCE = "Computer Science"
    MATHEMATICS = "Mathematics"
    PHYSICS = "Physics"
    BUSINESS = "Business"
    ARTS = "Arts"


@dataclass
class Course:
    """Represents a single course."""

    course_id: str
    course_name: str
    instructor: str
    credits: float
    department: str
    capacity: int

    def to_dict(self):
        """Convert the Course instance into a plain dictionary."""
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "instructor": self.instructor,
            "credits": self.credits,
            "department": self.department,
            "capacity": self.capacity,
        }

    @classmethod
    def from_dict(cls, data):
        """Build a Course instance from a plain dictionary."""
        return cls(
            course_id=data["course_id"],
            course_name=data["course_name"],
            instructor=data["instructor"],
            credits=data["credits"],
            department=data["department"],
            capacity=data["capacity"],
        )

    def __str__(self):
        return (
            f"ID: {self.course_id} | {self.course_name} | Instructor: {self.instructor} | "
            f"Credits: {self.credits} | Dept: {self.department} | Capacity: {self.capacity}"
        )
