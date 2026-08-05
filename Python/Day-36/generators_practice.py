"""
Generators Practice
--------------------
Demonstrates:
1. A generator function that counts up to a limit.
2. A generator function that yields only even numbers.
3. A generator expression for squares.
4. That generators are exhausted after one complete iteration.
"""


def count_up(limit):
    """Yield numbers from 1 to limit (inclusive)."""
    for number in range(1, limit + 1):
        yield number


def even_numbers(limit):
    """Yield only even numbers from 1 to limit (inclusive)."""
    for number in range(1, limit + 1):
        if number % 2 == 0:
            yield number


if __name__ == "__main__":
    print("count_up(5):")
    for number in count_up(5):
        print(number)

    print("\neven_numbers(10):")
    for number in even_numbers(10):
        print(number)

    print("\nGenerator expression (squares of 0-9):")
    squares = (x * x for x in range(10))
    for square in squares:
        print(square)

    print("\nDemonstrating generator exhaustion:")
    numbers = count_up(3)

    print("First iteration:")
    for number in numbers:
        print(number)

    print("Second iteration over the same generator object:")
    for number in numbers:
        print(number)
    print("(Nothing printed above because the generator is exhausted.)")
