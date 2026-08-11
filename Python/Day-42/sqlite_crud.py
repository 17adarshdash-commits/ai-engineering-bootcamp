"""
sqlite_crud.py

Wraps the four basic SQL operations (Create, Read, Update, Delete) into
functions against the same Students table used in sqlite_basics.py, then
demonstrates each one.
"""

import sqlite3

DB_FILE = "students.db"


def get_connection():
    """Open a connection and make sure the students table exists."""
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


def create_student(name, age, course):
    """Insert a new student and return its generated id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course),
    )
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return student_id


def read_students():
    """Return every student row as a list of tuples."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_student(student_id, name=None, age=None, course=None):
    """Update the given fields (only the ones provided) for a student id."""
    updates = {}
    if name is not None:
        updates["name"] = name
    if age is not None:
        updates["age"] = age
    if course is not None:
        updates["course"] = course

    if not updates:
        return

    set_clause = ", ".join(f"{column} = ?" for column in updates)
    values = list(updates.values()) + [student_id]

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE students SET {set_clause} WHERE id = ?", values)
    conn.commit()
    conn.close()


def delete_student(student_id):
    """Delete a student by id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()


def main():
    print("Create:")
    new_id = create_student("Diana Prince", 22, "Business")
    print(f"  Inserted student with id {new_id}")

    print("\nRead (all students):")
    for row in read_students():
        print(f"  {row}")

    print(f"\nUpdate (student {new_id} -> age 23, course 'Arts'):")
    update_student(new_id, age=23, course="Arts")
    for row in read_students():
        if row[0] == new_id:
            print(f"  {row}")

    print(f"\nDelete (student {new_id}):")
    delete_student(new_id)
    remaining_ids = [row[0] for row in read_students()]
    print(f"  Remaining ids: {remaining_ids}")


if __name__ == "__main__":
    main()
