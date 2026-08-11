"""
sqlite_basics.py

Introductory practice with sqlite3: create a database file, create a
Students table, insert a few rows, print every row, then close the
connection.
"""

import sqlite3

DB_FILE = "students.db"


def main():
    # Connecting also creates the file if it doesn't exist yet.
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
        """
    )

    # Only seed the table the first time this script runs against a fresh
    # database, so re-running it doesn't insert duplicate rows.
    cursor.execute("SELECT COUNT(*) FROM students")
    (row_count,) = cursor.fetchone()

    if row_count == 0:
        cursor.executemany(
            "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
            [
                ("Alice Johnson", 21, "Computer Science"),
                ("Bilal Ahmed", 23, "Mathematics"),
                ("Chen Wei", 20, "Physics"),
            ],
        )
        conn.commit()

    print("All students:")
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

    conn.close()


if __name__ == "__main__":
    main()
