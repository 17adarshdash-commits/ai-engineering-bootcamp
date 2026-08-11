"""
student.py

Defines the Student dataclass - a single student with an ID, name, age,
course, and CGPA, plus conversion to/from a plain tuple so it can be
(de)serialized to/from a SQLite row.
"""

from dataclasses import dataclass


@dataclass
class Student:
    """Represents a single student."""

    student_id: str
    name: str
    age: int
    course: str
    cgpa: float

    def to_row(self):
        """Convert the Student instance into a tuple matching the students table's column order."""
        return (self.student_id, self.name, self.age, self.course, self.cgpa)

    @classmethod
    def from_row(cls, row):
        """Build a Student instance from a SQLite row (student_id, name, age, course, cgpa)."""
        student_id, name, age, course, cgpa = row
        return cls(
            student_id=student_id,
            name=name,
            age=age,
            course=course,
            cgpa=cgpa,
        )

    def __str__(self):
        return (
            f"ID: {self.student_id} | {self.name} | Age: {self.age} | "
            f"Course: {self.course} | CGPA: {self.cgpa}"
        )
