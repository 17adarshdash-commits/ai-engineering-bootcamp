"""
advanced_joins.py

Creates Employees and Departments tables and practices CROSS JOIN
(every employee paired with every department) and SELF JOIN (employees
matched to their managers, who are themselves rows in Employees).
"""

import sqlite3

CREATE_DEPARTMENTS_SQL = """
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
)
"""

CREATE_EMPLOYEES_SQL = """
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees (employee_id)
)
"""

DEPARTMENTS = [
    (1, "Engineering"),
    (2, "Sales"),
]

EMPLOYEES = [
    (1, "Grace", None),   # Grace is the top-level manager - no manager of her own
    (2, "Alice", 1),      # reports to Grace
    (3, "Bob", 1),        # reports to Grace
    (4, "Charlie", 2),    # reports to Alice
]


def setup(conn):
    """Create both tables and seed them with sample data."""
    conn.execute(CREATE_DEPARTMENTS_SQL)
    conn.execute(CREATE_EMPLOYEES_SQL)
    conn.executemany(
        "INSERT INTO departments (department_id, department_name) VALUES (?, ?)",
        DEPARTMENTS,
    )
    conn.executemany(
        "INSERT INTO employees (employee_id, name, manager_id) VALUES (?, ?, ?)",
        EMPLOYEES,
    )
    conn.commit()


def print_rows(title, rows):
    print(f"\n-- {title} --")
    for row in rows:
        print(row)


def demo_cross_join(conn):
    """Every employee paired with every department - no matching condition at all."""
    cursor = conn.execute(
        """
        SELECT employees.name, departments.department_name
        FROM employees
        CROSS JOIN departments
        ORDER BY employees.name, departments.department_name
        """
    )
    print_rows("CROSS JOIN (every employee x every department)", cursor.fetchall())


def demo_self_join(conn):
    """
    Join employees to itself - one aliased copy (e) as the employee side,
    another (m) as the manager side of the same underlying table.
    """
    cursor = conn.execute(
        """
        SELECT e.name AS employee, m.name AS manager
        FROM employees e
        LEFT JOIN employees m ON e.manager_id = m.employee_id
        ORDER BY e.name
        """
    )
    print_rows("SELF JOIN (employee -> manager)", cursor.fetchall())


def demo_inner_join_review(conn):
    """Review: INNER JOIN only makes sense here with a real matching column,
    so this demonstrates it against a department assignment table instead."""
    conn.execute(
        "CREATE TABLE assignments (employee_id INTEGER, department_id INTEGER)"
    )
    conn.executemany(
        "INSERT INTO assignments (employee_id, department_id) VALUES (?, ?)",
        [(1, 1), (2, 1), (3, 2)],  # Charlie (4) has no assignment
    )
    conn.commit()

    cursor = conn.execute(
        """
        SELECT employees.name, departments.department_name
        FROM employees
        INNER JOIN assignments ON employees.employee_id = assignments.employee_id
        INNER JOIN departments ON assignments.department_id = departments.department_id
        ORDER BY employees.name
        """
    )
    print_rows("INNER JOIN review (assigned employees only, Charlie excluded)", cursor.fetchall())


def demo_left_join_review(conn):
    """Review: LEFT JOIN keeps every employee, even Charlie who has no assignment."""
    cursor = conn.execute(
        """
        SELECT employees.name, departments.department_name
        FROM employees
        LEFT JOIN assignments ON employees.employee_id = assignments.employee_id
        LEFT JOIN departments ON assignments.department_id = departments.department_id
        ORDER BY employees.name
        """
    )
    print_rows("LEFT JOIN review (every employee, Charlie -> NULL)", cursor.fetchall())


def main():
    conn = sqlite3.connect(":memory:")
    try:
        setup(conn)
        demo_cross_join(conn)
        demo_self_join(conn)
        demo_inner_join_review(conn)
        demo_left_join_review(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
