"""
Day 38: Lambda Functions Practice
Demonstrates lambda usage with sorted(), max(), and min().
"""

students = [
    ("Alice", 88),
    ("Bob", 75),
    ("Charlie", 95),
    ("David", 82)
]

employees = [
    {"name": "Alice", "salary": 70000},
    {"name": "Bob", "salary": 50000},
    {"name": "Charlie", "salary": 90000},
]


def sort_by_name(data):
    """Sort a list of (name, marks) tuples alphabetically by name."""
    return sorted(data, key=lambda student: student[0])


def sort_by_marks(data):
    """Sort a list of (name, marks) tuples by marks, ascending."""
    return sorted(data, key=lambda student: student[1])


def highest_scorer(data):
    """Return the student tuple with the highest marks."""
    return max(data, key=lambda student: student[1])


def lowest_scorer(data):
    """Return the student tuple with the lowest marks."""
    return min(data, key=lambda student: student[1])


def sort_employees_by_salary(data):
    """Sort a list of employee dicts by salary, ascending."""
    return sorted(data, key=lambda employee: employee["salary"])


if __name__ == "__main__":
    print("=== Original Data ===")
    print("Students:", students)
    print("Employees:", employees)

    print("\n=== 1. Sorting with key=lambda ===")
    print("Sorted by name :", sort_by_name(students))
    print("Sorted by marks:", sort_by_marks(students))

    print("\n=== 2. max() with lambda ===")
    print("Highest scorer:", highest_scorer(students))

    print("\n=== 3. min() with lambda ===")
    print("Lowest scorer :", lowest_scorer(students))

    print("\n=== 4. sorted() with lambda (dictionaries) ===")
    print("Employees sorted by salary:", sort_employees_by_salary(employees))
