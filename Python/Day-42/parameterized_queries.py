"""
parameterized_queries.py

Practice writing every query with '?' placeholders instead of interpolating
values into the SQL string - search by name, search by course, update with
parameters, and delete with parameters.
"""

import sqlite3

DB_FILE = "students.db"


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def search_by_name(name):
    """Find students whose name contains the given text (case-insensitive)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        (f"%{name}%",),
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


def search_by_course(course):
    """Find every student enrolled in an exact course."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE course = ?",
        (course,),
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_course_by_id(student_id, new_course):
    """Change a single student's course, matched by id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET course = ? WHERE id = ?",
        (new_course, student_id),
    )
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated


def delete_by_name(name):
    """Delete every student with an exact name match."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted


def main():
    print("Search by name containing 'a':")
    for row in search_by_name("a"):
        print(f"  {row}")

    print("\nSearch by course 'Computer Science':")
    for row in search_by_course("Computer Science"):
        print(f"  {row}")

    print("\nUpdate course for id 1 -> 'Mathematics':")
    updated = update_course_by_id(1, "Mathematics")
    print(f"  Rows updated: {updated}")

    print("\nDelete student named 'Nonexistent Student':")
    deleted = delete_by_name("Nonexistent Student")
    print(f"  Rows deleted: {deleted}")


if __name__ == "__main__":
    main()
