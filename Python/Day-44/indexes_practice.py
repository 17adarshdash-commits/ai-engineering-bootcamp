"""
indexes_practice.py

Creates a Students table, adds an index on the name column
(idx_student_name), and demonstrates searching students by name.
Also explains, in comments, when indexes are beneficial and when they
add unnecessary overhead.
"""

import sqlite3

CREATE_STUDENTS_SQL = """
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT NOT NULL
)
"""

CREATE_INDEX_SQL = """
CREATE INDEX idx_student_name
ON students(name)
"""

STUDENTS = [
    (1, "Alice", "Computer Science"),
    (2, "Bob", "Mechanical"),
    (3, "Charlie", "Electrical"),
    (4, "Amy", "Physics"),
    (5, "Aaron", "Computer Science"),
]


def setup(conn):
    """Create the students table, seed it, then add an index on name."""
    conn.execute(CREATE_STUDENTS_SQL)
    conn.executemany(
        "INSERT INTO students (student_id, name, course) VALUES (?, ?, ?)",
        STUDENTS,
    )
    conn.execute(CREATE_INDEX_SQL)
    conn.commit()


def search_by_name(conn, name):
    """
    Look up a student by exact name. Once idx_student_name exists,
    SQLite's query planner can use it to jump straight to matching rows
    instead of scanning every row in the table - the query itself doesn't
    change at all, only how SQLite executes it underneath.
    """
    cursor = conn.execute(
        "SELECT student_id, name, course FROM students WHERE name = ?", (name,)
    )
    return cursor.fetchall()


def show_query_plan(conn, name):
    """Print SQLite's EXPLAIN QUERY PLAN output to show the index being used."""
    cursor = conn.execute(
        "EXPLAIN QUERY PLAN SELECT student_id, name, course FROM students WHERE name = ?",
        (name,),
    )
    print(f"\n-- Query plan for WHERE name = '{name}' --")
    for row in cursor.fetchall():
        print(row)


def main():
    conn = sqlite3.connect(":memory:")
    try:
        setup(conn)

        print("\n-- Searching for 'Charlie' --")
        for row in search_by_name(conn, "Charlie"):
            print(row)

        show_query_plan(conn, "Charlie")
    finally:
        conn.close()


# When indexes are beneficial:
# - Large tables where a column is searched/filtered/joined on frequently
#   (e.g. WHERE name = ?, or a foreign key column used in every JOIN) -
#   the index turns an O(n) full table scan into a fast, roughly O(log n)
#   lookup, and the gain grows with table size.
# - Columns used in ORDER BY on large result sets, since a matching index
#   can let SQLite avoid a separate sort step.
#
# When indexes add unnecessary overhead:
# - Small tables (a few dozen rows, like this example) - a full scan is
#   already fast enough that the index barely helps reads, while still
#   costing space and write overhead.
# - Columns that are rarely used in WHERE/JOIN/ORDER BY - the index just
#   sits there, unused, but is still updated on every write.
# - Columns that change very frequently (e.g. a counter updated on every
#   transaction) - every INSERT/UPDATE/DELETE on the table now also has
#   to update the index, so write-heavy columns pay a real ongoing cost.
# - Tables with far more writes than reads - the read speedup from an
#   index may not be worth the slower writes it causes.


if __name__ == "__main__":
    main()
