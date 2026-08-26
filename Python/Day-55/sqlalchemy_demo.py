"""
Day 55 - SQLAlchemy Introduction Demo

Goal: walk through the full flow -
    Python -> SQLAlchemy -> SQLite
by creating a database, defining a Student model, and doing basic
create / read / update / delete operations against it.

Install:
    pip install sqlalchemy

Run:
    python sqlalchemy_demo.py

This creates a `students.db` SQLite file in the same directory.
"""

from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Engine - the entry point to the database.
#    "sqlite:///students.db" -> a local SQLite file called students.db.
engine = create_engine("sqlite:///students.db", echo=False)

# 2. Base - every model class inherits from this so SQLAlchemy knows
#    which classes map to tables.
Base = declarative_base()


# 3. Model - a Python class that maps to a database table.
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)  # primary key, auto-increments
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    cgpa = Column(Float, nullable=False)

    def __repr__(self):
        return (
            f"Student(id={self.id}, name={self.name!r}, "
            f"department={self.department!r}, cgpa={self.cgpa})"
        )


# 4. Create the table(s) in the database if they don't already exist.
Base.metadata.create_all(engine)

# 5. Session - the workspace for talking to the database.
Session = sessionmaker(bind=engine)


def create_student(name: str, department: str, cgpa: float) -> Student:
    """Insert a new student."""
    with Session() as session:
        student = Student(name=name, department=department, cgpa=cgpa)
        session.add(student)
        session.commit()
        session.refresh(student)  # pull back the auto-generated id
        print(f"Created: {student}")
        return student


def read_students() -> list[Student]:
    """Read all students."""
    with Session() as session:
        students = session.query(Student).all()
        print("\nAll students:")
        for s in students:
            print(" ", s)
        return students


def update_student_cgpa(student_id: int, new_cgpa: float) -> None:
    """Update one student's cgpa by id."""
    with Session() as session:
        student = session.get(Student, student_id)
        if student is None:
            print(f"No student with id={student_id}")
            return
        student.cgpa = new_cgpa
        session.commit()
        print(f"\nUpdated id={student_id} -> cgpa={new_cgpa}")


def delete_student(student_id: int) -> None:
    """Delete one student by id."""
    with Session() as session:
        student = session.get(Student, student_id)
        if student is None:
            print(f"No student with id={student_id}")
            return
        session.delete(student)
        session.commit()
        print(f"\nDeleted id={student_id}")


def main():
    # Create a couple of students.
    s1 = create_student("Adarsh", "AI Engineering", 8.7)
    s2 = create_student("Priya", "Computer Science", 9.1)

    # Read them back.
    read_students()

    # Update one.
    update_student_cgpa(s1.id, 9.0)
    read_students()

    # Delete one.
    delete_student(s2.id)
    read_students()


if __name__ == "__main__":
    main()
