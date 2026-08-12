"""
advanced_sql_queries.py

Creates Students and Courses tables in an in-memory SQLite database and
practices ORDER BY, LIMIT, DISTINCT, LIKE, and BETWEEN. Every query result
is printed so the effect of each clause is visible.
"""

import sqlite3

CREATE_STUDENTS_SQL = """
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL,
    cgpa REAL NOT NULL
)
"""

CREATE_COURSES_SQL = """
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    credits INTEGER NOT NULL
)
"""

STUDENTS = [
    (1, "Alice", 20, "Computer Science", 9.1),
    (2, "Bob", 22, "Mechanical", 7.4),
    (3, "Charlie", 21, "Computer Science", 8.6),
    (4, "Diana", 23, "Electrical", 6.9),
    (5, "Aaron", 20, "Computer Science", 8.2),
    (6, "Ethan", 24, "Mechanical", 7.9),
    (7, "Amy", 22, "Electrical", 9.4),
    (8, "Fiona", 21, "Computer Science", 5.8),
]

COURSES = [
    (1, "Computer Science", 4),
    (2, "Mechanical", 3),
    (3, "Electrical", 3),
]


def setup(conn):
    """Create both tables and seed them with sample data."""
    conn.execute(CREATE_STUDENTS_SQL)
    conn.execute(CREATE_COURSES_SQL)
    conn.executemany(
        "INSERT INTO students (student_id, name, age, course, cgpa) VALUES (?, ?, ?, ?, ?)",
        STUDENTS,
    )
    conn.executemany(
        "INSERT INTO courses (course_id, course_name, credits) VALUES (?, ?, ?)",
        COURSES,
    )
    conn.commit()


def print_rows(title, rows):
    print(f"\n-- {title} --")
    if not rows:
        print("(no rows)")
        return
    for row in rows:
        print(row)


def demo_order_by(conn):
    """Sort students by CGPA, highest first."""
    cursor = conn.execute(
        "SELECT name, cgpa FROM students ORDER BY cgpa DESC"
    )
    print_rows("ORDER BY cgpa DESC", cursor.fetchall())


def demo_limit(conn):
    """Take only the top 3 students by CGPA."""
    cursor = conn.execute(
        "SELECT name, cgpa FROM students ORDER BY cgpa DESC LIMIT 3"
    )
    print_rows("ORDER BY cgpa DESC LIMIT 3 (top 3 students)", cursor.fetchall())


def demo_distinct(conn):
    """List every course name once, regardless of how many students take it."""
    cursor = conn.execute("SELECT DISTINCT course FROM students")
    print_rows("DISTINCT course", cursor.fetchall())


def demo_like(conn):
    """Find students whose name starts with 'A'."""
    cursor = conn.execute(
        "SELECT name FROM students WHERE name LIKE 'A%'"
    )
    print_rows("WHERE name LIKE 'A%'", cursor.fetchall())


def demo_in(conn):
    """Find students in either Mechanical or Electrical."""
    cursor = conn.execute(
        "SELECT name, course FROM students WHERE course IN (?, ?)",
        ("Mechanical", "Electrical"),
    )
    print_rows("WHERE course IN ('Mechanical', 'Electrical')", cursor.fetchall())


def demo_between(conn):
    """Find students with a CGPA between 7.0 and 9.0 inclusive."""
    cursor = conn.execute(
        "SELECT name, cgpa FROM students WHERE cgpa BETWEEN ? AND ?",
        (7.0, 9.0),
    )
    print_rows("WHERE cgpa BETWEEN 7.0 AND 9.0", cursor.fetchall())


def main():
    conn = sqlite3.connect(":memory:")
    try:
        setup(conn)
        demo_order_by(conn)
        demo_limit(conn)
        demo_distinct(conn)
        demo_like(conn)
        demo_in(conn)
        demo_between(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
