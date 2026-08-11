"""
student_manager.py

Defines StudentManager - validates input and performs add/update/delete/
search/display operations against the students table, using a Database
instance for every connection. All SQL here uses '?' placeholders.
"""

from student import Student

MIN_CGPA = 0
MAX_CGPA = 10


class StudentError(Exception):
    """Base exception for all student-related errors."""


class DuplicateStudentIDError(StudentError):
    """Raised when a student ID already exists."""


class InvalidNameError(StudentError):
    """Raised when a student name is empty/blank."""


class InvalidAgeError(StudentError):
    """Raised when age is not a positive integer."""


class InvalidCourseError(StudentError):
    """Raised when a course name is empty/blank."""


class InvalidCGPAError(StudentError):
    """Raised when CGPA is outside the 0-10 range."""


class StudentNotFoundError(StudentError):
    """Raised when a student ID cannot be found."""


class StudentManager:
    """Performs validated CRUD operations on the students table."""

    def __init__(self, database):
        self.database = database

    # ------------------------------------------------------------------
    # Validation helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _validate_name(name):
        if not name or not name.strip():
            raise InvalidNameError("Name cannot be empty.")

    @staticmethod
    def _validate_age(age):
        try:
            age = int(age)
        except (TypeError, ValueError):
            raise InvalidAgeError("Age must be an integer.")
        if age <= 0:
            raise InvalidAgeError("Age must be greater than 0.")
        return age

    @staticmethod
    def _validate_course(course):
        if not course or not course.strip():
            raise InvalidCourseError("Course cannot be empty.")

    @staticmethod
    def _validate_cgpa(cgpa):
        try:
            cgpa = float(cgpa)
        except (TypeError, ValueError):
            raise InvalidCGPAError("CGPA must be a number.")
        if not (MIN_CGPA <= cgpa <= MAX_CGPA):
            raise InvalidCGPAError(f"CGPA must be between {MIN_CGPA} and {MAX_CGPA}.")
        return cgpa

    # ------------------------------------------------------------------
    # Create
    # ------------------------------------------------------------------
    def add_student(self, student_id, name, age, course, cgpa):
        """Add a new student after validating all fields."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT 1 FROM students WHERE student_id = ?", (student_id,)
            )
            if cursor.fetchone() is not None:
                raise DuplicateStudentIDError(f"Student ID '{student_id}' already exists.")

            self._validate_name(name)
            age = self._validate_age(age)
            self._validate_course(course)
            cgpa = self._validate_cgpa(cgpa)

            student = Student(
                student_id=student_id,
                name=name.strip(),
                age=age,
                course=course.strip(),
                cgpa=cgpa,
            )
            conn.execute(
                "INSERT INTO students (student_id, name, age, course, cgpa) VALUES (?, ?, ?, ?, ?)",
                student.to_row(),
            )
            conn.commit()
            return student
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Read
    # ------------------------------------------------------------------
    def get_student(self, student_id):
        """Fetch a single student by id, or raise StudentNotFoundError."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT student_id, name, age, course, cgpa FROM students WHERE student_id = ?",
                (student_id,),
            )
            row = cursor.fetchone()
            if row is None:
                raise StudentNotFoundError(f"Student ID '{student_id}' not found.")
            return Student.from_row(row)
        finally:
            conn.close()

    def display_students(self):
        """Return every student, ordered by student_id."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT student_id, name, age, course, cgpa FROM students ORDER BY student_id"
            )
            return [Student.from_row(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    def search_student(self, keyword):
        """Search students by ID, name, or course (case-insensitive substring match)."""
        conn = self.database.connect()
        try:
            pattern = f"%{keyword}%"
            cursor = conn.execute(
                """
                SELECT student_id, name, age, course, cgpa FROM students
                WHERE student_id LIKE ? OR name LIKE ? OR course LIKE ?
                """,
                (pattern, pattern, pattern),
            )
            return [Student.from_row(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Update
    # ------------------------------------------------------------------
    def update_student(self, student_id, **updates):
        """Update one or more fields of an existing student."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "SELECT 1 FROM students WHERE student_id = ?", (student_id,)
            )
            if cursor.fetchone() is None:
                raise StudentNotFoundError(f"Student ID '{student_id}' not found.")

            fields = {}
            if "name" in updates:
                self._validate_name(updates["name"])
                fields["name"] = updates["name"].strip()
            if "age" in updates:
                fields["age"] = self._validate_age(updates["age"])
            if "course" in updates:
                self._validate_course(updates["course"])
                fields["course"] = updates["course"].strip()
            if "cgpa" in updates:
                fields["cgpa"] = self._validate_cgpa(updates["cgpa"])

            if not fields:
                return self.get_student(student_id)

            set_clause = ", ".join(f"{column} = ?" for column in fields)
            values = list(fields.values()) + [student_id]
            conn.execute(f"UPDATE students SET {set_clause} WHERE student_id = ?", values)
            conn.commit()
            return self.get_student(student_id)
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Delete
    # ------------------------------------------------------------------
    def delete_student(self, student_id):
        """Delete a student by id."""
        conn = self.database.connect()
        try:
            cursor = conn.execute(
                "DELETE FROM students WHERE student_id = ?", (student_id,)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise StudentNotFoundError(f"Student ID '{student_id}' not found.")
        finally:
            conn.close()
