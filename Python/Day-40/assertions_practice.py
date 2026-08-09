"""
assertions_practice.py

Practice using `assert` statements to check assumptions: positive numbers,
division, list length, and string comparison. Includes examples that pass
and examples that intentionally fail, with the failure handled so the
script keeps running.
"""


def check_positive(number):
    """Assert that a number is positive."""
    assert number > 0, f"Expected a positive number, got {number}"
    return number


def check_division(numerator, denominator):
    """Assert that the denominator is not zero, then divide."""
    assert denominator != 0, "Cannot divide by zero"
    return numerator / denominator


def check_list_length(items, expected_length):
    """Assert that a list has the expected number of elements."""
    assert len(items) == expected_length, (
        f"Expected {expected_length} items, got {len(items)}"
    )
    return items


def check_string_equal(actual, expected):
    """Assert that two strings are equal."""
    assert actual == expected, f"Expected {expected!r}, got {actual!r}"
    return actual


def run_assertion(description, func, *args):
    """Run an assertion-based check and report whether it passed or failed."""
    try:
        func(*args)
        print(f"[PASS] {description}")
    except AssertionError as e:
        print(f"[FAIL] {description} -> {e}")


if __name__ == "__main__":
    print("=" * 50)
    print("Positive number checks")
    print("=" * 50)
    run_assertion("5 is positive", check_positive, 5)
    run_assertion("-3 is positive (should fail)", check_positive, -3)

    print()
    print("=" * 50)
    print("Division checks")
    print("=" * 50)
    run_assertion("10 / 2 is valid", check_division, 10, 2)
    run_assertion("10 / 0 is valid (should fail)", check_division, 10, 0)

    print()
    print("=" * 50)
    print("List length checks")
    print("=" * 50)
    run_assertion("[1, 2, 3] has length 3", check_list_length, [1, 2, 3], 3)
    run_assertion("[1, 2, 3] has length 5 (should fail)", check_list_length, [1, 2, 3], 5)

    print()
    print("=" * 50)
    print("String comparison checks")
    print("=" * 50)
    run_assertion("'hello' equals 'hello'", check_string_equal, "hello", "hello")
    run_assertion("'hello' equals 'world' (should fail)", check_string_equal, "hello", "world")
