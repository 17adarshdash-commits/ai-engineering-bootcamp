"""
joins_practice.py

Creates Students and Enrollments tables (a one-to-many relationship -
one student can have many enrollments) and practices INNER JOIN and
LEFT JOIN to display combined student and enrollment information.
"""

import sqlite3

CREATE_STUDENTS_SQL = """
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
"""

CREATE_ENROLLMENTS_SQL = """
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id)
)
"""

STUDENTS = [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie"),
    (4, "Diana"),  # has no enrollments - demonstrates LEFT JOIN
]

ENROLLMENTS = [
    (1, 1, "Computer Science"),
    (2, 1, "Mathematics"),
    (3, 2, "Mechanical"),
    (4, 3, "Electrical"),
    (5, 3, "Physics"),
]


def setup(conn):
    """Create both tables and seed them with related sample data."""
    conn.execute(CREATE_STUDENTS_SQL)
    conn.execute(CREATE_ENROLLMENTS_SQL)
    conn.executemany(
        "INSERT INTO students (student_id, name) VALUES (?, ?)", STUDENTS
    )
    conn.executemany(
        "INSERT INTO enrollments (enrollment_id, student_id, course) VALUES (?, ?, ?)",
        ENROLLMENTS,
    )
    conn.commit()


def print_rows(title, rows):
    print(f"\n-- {title} --")
    for row in rows:
        print(row)


def demo_inner_join(conn):
    """Only students who have at least one enrollment - Diana is excluded."""
    cursor = conn.execute(
        """
        SELECT students.name, enrollments.course
        FROM students
        INNER JOIN enrollments ON students.student_id = enrollments.student_id
        ORDER BY students.name
        """
    )
    print_rows("INNER JOIN (students with enrollments only)", cursor.fetchall())


def demo_left_join(conn):
    """Every student, with NULL course for students who haven't enrolled - Diana appears."""
    cursor = conn.execute(
        """
        SELECT students.name, enrollments.course
        FROM students
        LEFT JOIN enrollments ON students.student_id = enrollments.student_id
        ORDER BY students.name
        """
    )
    print_rows("LEFT JOIN (every student, unmatched -> NULL)", cursor.fetchall())


def main():
    conn = sqlite3.connect(":memory:")
    try:
        setup(conn)
        demo_inner_join(conn)
        demo_left_join(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
