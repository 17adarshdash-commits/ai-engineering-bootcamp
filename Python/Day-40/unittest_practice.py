"""
unittest_practice.py

A small calculator (add, subtract, multiply, divide) with unittest
coverage for normal cases, edge cases, and division by zero.

Run with:
    python -m unittest unittest_practice.py
"""

import unittest


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


class TestCalculator(unittest.TestCase):
    """Unit tests for the calculator functions."""

    # ------------------------------------------------------------------
    # add
    # ------------------------------------------------------------------
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    # ------------------------------------------------------------------
    # subtract
    # ------------------------------------------------------------------
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_results_in_negative(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)

    # ------------------------------------------------------------------
    # multiply
    # ------------------------------------------------------------------
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(4, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    # ------------------------------------------------------------------
    # divide
    # ------------------------------------------------------------------
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_results_in_float(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_zero_by_number(self):
        self.assertEqual(divide(0, 5), 0)

    # ------------------------------------------------------------------
    # truthiness checks (assertTrue / assertFalse practice)
    # ------------------------------------------------------------------
    def test_add_is_commutative(self):
        self.assertTrue(add(2, 3) == add(3, 2))

    def test_subtract_is_not_commutative(self):
        self.assertFalse(subtract(2, 3) == subtract(3, 2))


if __name__ == "__main__":
    unittest.main()
