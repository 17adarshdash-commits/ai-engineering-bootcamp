"""
aggregate_functions.py

Creates a Students table with sample CGPA values and demonstrates
COUNT(), SUM(), AVG(), MIN(), MAX(), and GROUP BY.
"""

import sqlite3

CREATE_STUDENTS_SQL = """
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    cgpa REAL NOT NULL
)
"""

STUDENTS = [
    (1, "Alice", "Computer Science", 9.1),
    (2, "Bob", "Mechanical", 7.4),
    (3, "Charlie", "Computer Science", 8.6),
    (4, "Diana", "Electrical", 6.9),
    (5, "Aaron", "Computer Science", 8.2),
    (6, "Ethan", "Mechanical", 7.9),
    (7, "Amy", "Electrical", 9.4),
    (8, "Fiona", "Computer Science", 5.8),
]


def setup(conn):
    """Create the students table and seed it with sample CGPA data."""
    conn.execute(CREATE_STUDENTS_SQL)
    conn.executemany(
        "INSERT INTO students (student_id, name, course, cgpa) VALUES (?, ?, ?, ?)",
        STUDENTS,
    )
    conn.commit()


def print_rows(title, rows):
    print(f"\n-- {title} --")
    for row in rows:
        print(row)


def demo_count(conn):
    """Count how many students there are in total."""
    cursor = conn.execute("SELECT COUNT(*) FROM students")
    print_rows("COUNT(*) (total students)", cursor.fetchall())


def demo_sum(conn):
    """Sum every student's CGPA (not meaningful on its own, but shows the mechanics)."""
    cursor = conn.execute("SELECT SUM(cgpa) FROM students")
    print_rows("SUM(cgpa)", cursor.fetchall())


def demo_avg(conn):
    """Average CGPA across all students."""
    cursor = conn.execute("SELECT AVG(cgpa) FROM students")
    print_rows("AVG(cgpa)", cursor.fetchall())


def demo_min_max(conn):
    """Lowest and highest CGPA across all students."""
    cursor = conn.execute("SELECT MIN(cgpa), MAX(cgpa) FROM students")
    print_rows("MIN(cgpa), MAX(cgpa)", cursor.fetchall())


def demo_group_by_course(conn):
    """Per-course student count and average CGPA."""
    cursor = conn.execute(
        """
        SELECT course, COUNT(*), AVG(cgpa)
        FROM students
        GROUP BY course
        ORDER BY course
        """
    )
    print_rows("GROUP BY course -> COUNT(*), AVG(cgpa)", cursor.fetchall())


def demo_group_by_having(conn):
    """Courses whose average CGPA exceeds 8.0."""
    cursor = conn.execute(
        """
        SELECT course, AVG(cgpa) AS avg_cgpa
        FROM students
        GROUP BY course
        HAVING avg_cgpa > 8.0
        """
    )
    print_rows("GROUP BY course HAVING AVG(cgpa) > 8.0", cursor.fetchall())


def main():
    conn = sqlite3.connect(":memory:")
    try:
        setup(conn)
        demo_count(conn)
        demo_sum(conn)
        demo_avg(conn)
        demo_min_max(conn)
        demo_group_by_course(conn)
        demo_group_by_having(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
