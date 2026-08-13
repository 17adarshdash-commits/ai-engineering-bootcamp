"""
normalization_examples.py

Builds the same "students and courses" data two ways: a poor,
unnormalized design (one wide Students table with fixed Course1/Course2/
Course3 columns) and a normalized design (Students, Courses, and an
Enrollments junction table). Prints both, then explains in comments why
the normalized version is better.
"""

import sqlite3

# -- Poor Design ------------------------------------------------------------
# Violates 1NF: "which courses does this student take" is a multi-valued
# fact squeezed into a fixed number of columns instead of one row per fact.
CREATE_POOR_STUDENTS_SQL = """
CREATE TABLE poor_students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course1 TEXT,
    course2 TEXT,
    course3 TEXT
)
"""

POOR_STUDENTS = [
    (1, "Alice", "Computer Science", "Mathematics", None),
    (2, "Bob", "Mechanical", None, None),
    (3, "Charlie", "Electrical", "Physics", "Computer Science"),
]

# -- Normalized Design --------------------------------------------------
# Students: one row per student, no course columns at all.
CREATE_STUDENTS_SQL = """
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
"""

# Courses: each course's name is stored exactly once, here.
CREATE_COURSES_SQL = """
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL
)
"""

# Enrollments: the junction table - one row per (student, course) pairing,
# so a student can be enrolled in any number of courses (not capped at 3).
CREATE_ENROLLMENTS_SQL = """
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (course_id) REFERENCES courses (course_id)
)
"""

STUDENTS = [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie"),
]

COURSES = [
    (1, "Computer Science"),
    (2, "Mathematics"),
    (3, "Mechanical"),
    (4, "Electrical"),
    (5, "Physics"),
]

ENROLLMENTS = [
    (1, 1, 1),  # Alice - Computer Science
    (2, 1, 2),  # Alice - Mathematics
    (3, 2, 3),  # Bob - Mechanical
    (4, 3, 4),  # Charlie - Electrical
    (5, 3, 5),  # Charlie - Physics
    (6, 3, 1),  # Charlie - Computer Science
]


def setup_poor(conn):
    conn.execute(CREATE_POOR_STUDENTS_SQL)
    conn.executemany(
        "INSERT INTO poor_students (student_id, name, course1, course2, course3) "
        "VALUES (?, ?, ?, ?, ?)",
        POOR_STUDENTS,
    )
    conn.commit()


def setup_normalized(conn):
    conn.execute(CREATE_STUDENTS_SQL)
    conn.execute(CREATE_COURSES_SQL)
    conn.execute(CREATE_ENROLLMENTS_SQL)
    conn.executemany("INSERT INTO students (student_id, name) VALUES (?, ?)", STUDENTS)
    conn.executemany(
        "INSERT INTO courses (course_id, course_name) VALUES (?, ?)", COURSES
    )
    conn.executemany(
        "INSERT INTO enrollments (enrollment_id, student_id, course_id) VALUES (?, ?, ?)",
        ENROLLMENTS,
    )
    conn.commit()


def print_rows(title, rows):
    print(f"\n-- {title} --")
    for row in rows:
        print(row)


def show_poor_design(conn):
    cursor = conn.execute("SELECT * FROM poor_students")
    print_rows("Poor Design: poor_students (raw)", cursor.fetchall())
    # Renaming "Computer Science" everywhere it appears means editing
    # course1/course2/course3 across every row that happens to mention it -
    # and Charlie can't take a 4th course without adding another column.


def show_normalized_design(conn):
    cursor = conn.execute(
        """
        SELECT students.name, courses.course_name
        FROM enrollments
        INNER JOIN students ON enrollments.student_id = students.student_id
        INNER JOIN courses ON enrollments.course_id = courses.course_id
        ORDER BY students.name, courses.course_name
        """
    )
    print_rows("Normalized Design: students JOIN enrollments JOIN courses", cursor.fetchall())
    # Renaming "Computer Science" now means updating a single row in
    # `courses` - every enrollment referencing it via course_id picks up
    # the change automatically, and a student can have any number of
    # enrollments without touching the schema.


def main():
    conn = sqlite3.connect(":memory:")
    try:
        setup_poor(conn)
        setup_normalized(conn)
        show_poor_design(conn)
        show_normalized_design(conn)
    finally:
        conn.close()


# Why the normalized version is better:
# 1. No duplicate data: a course's name lives in exactly one row of
#    `courses`, instead of being retyped into course1/course2/course3
#    wherever a student happens to take it.
# 2. No structural cap: the poor design hard-codes "at most 3 courses per
#    student" into the schema itself; the normalized design lets a student
#    have any number of enrollments, since each is just another row.
# 3. Easier updates: correcting a typo in a course name is one UPDATE in
#    `courses`, instead of hunting through every student row that
#    duplicated the misspelled name.
# 4. No wasted/NULL columns: Bob's course2 and course3 are NULL in the
#    poor design purely because the table has to accommodate the busiest
#    student; the normalized design has no such waste - Bob simply has one
#    enrollments row.


if __name__ == "__main__":
    main()
