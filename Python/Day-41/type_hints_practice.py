"""
type_hints_practice.py

Demonstrates function annotations using List, Dict, Tuple, and Optional
from the typing module.
"""

from typing import List, Dict, Optional, Tuple


def add(a: int, b: int) -> int:
    return a + b


def average(numbers: List[int]) -> float:
    if not numbers:
        raise ValueError("Cannot average an empty list.")
    return sum(numbers) / len(numbers)


def find_student(students: Dict[int, str], student_id: int) -> Optional[str]:
    return students.get(student_id)


def swap(values: Tuple[int, int]) -> Tuple[int, int]:
    a, b = values
    return b, a


def main():
    # --- add ---
    print("add(2, 3) =", add(2, 3))
    print("add(-5, 5) =", add(-5, 5))

    # --- average ---
    print("\naverage([1, 2, 3, 4]) =", average([1, 2, 3, 4]))
    print("average([10]) =", average([10]))
    try:
        average([])
    except ValueError as e:
        print("average([]) raised:", e)

    # --- find_student ---
    students: Dict[int, str] = {1: "Adarsh", 2: "Priya", 3: "Rahul"}
    print("\nfind_student(students, 2) =", find_student(students, 2))
    print("find_student(students, 99) =", find_student(students, 99))  # None

    # --- swap ---
    print("\nswap((1, 2)) =", swap((1, 2)))
    print("swap((0, -1)) =", swap((0, -1)))


if __name__ == "__main__":
    main()
