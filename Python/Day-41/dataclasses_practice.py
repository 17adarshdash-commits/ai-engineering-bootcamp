"""
dataclasses_practice.py

Demonstrates the @dataclass decorator: automatic __init__, __repr__, and
__eq__, plus field() with default_factory for mutable defaults.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Student:
    id: int
    name: str
    course: str
    cgpa: float


@dataclass
class Book:
    title: str
    author: str
    pages: int
    tags: List[str] = field(default_factory=list)


def main():
    # --- Object creation ---
    student1 = Student(id=1, name="Adarsh", course="AI Engineering", cgpa=9.2)
    student2 = Student(id=2, name="Priya", course="Data Science", cgpa=8.7)
    print("Created students:")
    print(student1)
    print(student2)

    # --- Automatic __repr__ ---
    # print(student1) above already used the generated __repr__ (dataclasses
    # don't define __str__, so print() falls back to __repr__).
    print("\nrepr(student1):", repr(student1))

    # --- Equality comparison ---
    student1_copy = Student(id=1, name="Adarsh", course="AI Engineering", cgpa=9.2)
    print("\nstudent1 == student1_copy:", student1 == student1_copy)  # True (same field values)
    print("student1 == student2:", student1 == student2)  # False

    # --- Updating attributes ---
    student1.cgpa = 9.5
    print("\nAfter updating cgpa:", student1)
    print("student1 == student1_copy now:", student1 == student1_copy)  # False, cgpa diverged

    # --- Book dataclass ---
    print("\n--- Books ---")
    book1 = Book(title="Clean Code", author="Robert C. Martin", pages=464)
    book2 = Book(
        title="Fluent Python",
        author="Luciano Ramalho",
        pages=792,
        tags=["python", "reference"],
    )
    print(book1)
    print(book2)
    print("book1 == book2:", book1 == book2)  # False

    # default_factory in action: each Book gets its own independent list.
    book1.tags.append("classic")
    print("\nbook1.tags:", book1.tags)
    print("book2.tags:", book2.tags)  # unaffected by book1's append


if __name__ == "__main__":
    main()
