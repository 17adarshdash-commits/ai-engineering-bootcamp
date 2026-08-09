"""
debugging_practice.py

Examples of common Python errors (ZeroDivisionError, IndexError, KeyError,
TypeError), how to read the traceback each one produces, and how to fix
them. Also demonstrates breakpoint() for interactive debugging.
"""


def buggy_divide(a, b):
    """
    BUG: called with b=0, this raises ZeroDivisionError.

    Traceback would point at the `a / b` line with:
        ZeroDivisionError: division by zero
    Fix: check the denominator before dividing (see safe_divide below).
    """
    return a / b


def safe_divide(a, b):
    """Fixed version: validate before dividing instead of letting it crash."""
    if b == 0:
        return None
    return a / b


def buggy_get_third_item(items):
    """
    BUG: called with a list shorter than 3 items, this raises IndexError.

    Traceback would point at `items[2]` with:
        IndexError: list index out of range
    Fix: check the list's length before indexing (see safe version below).
    """
    return items[2]


def safe_get_third_item(items):
    """Fixed version: check length before indexing instead of guessing."""
    if len(items) < 3:
        return None
    return items[2]


def buggy_get_age(person):
    """
    BUG: called with a dict missing the "age" key, this raises KeyError.

    Traceback would point at `person["age"]` with:
        KeyError: 'age'
    Fix: use .get() with a default, or check `"age" in person` first.
    """
    return person["age"]


def safe_get_age(person):
    """Fixed version: use dict.get() with a default instead of [] indexing."""
    return person.get("age")


def buggy_add_values(a, b):
    """
    BUG: called with mismatched types (e.g. int + str), this raises TypeError.

    Traceback would point at `a + b` with:
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
    Fix: validate/convert types before combining them.
    """
    return a + b


def safe_add_values(a, b):
    """Fixed version: coerce both values to the same type before adding."""
    return float(a) + float(b)


def debug_with_breakpoint(numbers):
    """
    Demonstrates breakpoint(): pauses execution here and drops into pdb,
    an interactive debugger. From the (Pdb) prompt you can inspect
    variables (e.g. type `numbers` or `total`), step line-by-line with
    `n` (next), resume with `c` (continue), or quit with `q`.
    Commented out by default so the script runs non-interactively.
    """
    total = 0
    for number in numbers:
        # breakpoint()  # uncomment to pause here and inspect `number`/`total`
        total += number
    return total


if __name__ == "__main__":
    print("=" * 50)
    print("ZeroDivisionError")
    print("=" * 50)
    try:
        buggy_divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Caught: {e}")
    print(f"Fixed with safe_divide(10, 0): {safe_divide(10, 0)}")

    print()
    print("=" * 50)
    print("IndexError")
    print("=" * 50)
    try:
        buggy_get_third_item([1, 2])
    except IndexError as e:
        print(f"Caught: {e}")
    print(f"Fixed with safe_get_third_item([1, 2]): {safe_get_third_item([1, 2])}")

    print()
    print("=" * 50)
    print("KeyError")
    print("=" * 50)
    try:
        buggy_get_age({"name": "Adarsh"})
    except KeyError as e:
        print(f"Caught: {e}")
    print(f"Fixed with safe_get_age({{'name': 'Adarsh'}}): {safe_get_age({'name': 'Adarsh'})}")

    print()
    print("=" * 50)
    print("TypeError")
    print("=" * 50)
    try:
        buggy_add_values(5, "3")
    except TypeError as e:
        print(f"Caught: {e}")
    print(f"Fixed with safe_add_values(5, '3'): {safe_add_values(5, '3')}")

    print()
    print("=" * 50)
    print("breakpoint() demo")
    print("=" * 50)
    result = debug_with_breakpoint([1, 2, 3, 4, 5])
    print(f"Sum: {result} (uncomment breakpoint() above to step through interactively)")
