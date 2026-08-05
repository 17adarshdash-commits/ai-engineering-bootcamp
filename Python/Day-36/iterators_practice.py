"""
Iterators Practice
==================
Demonstrates:
- Converting an iterable to an iterator with iter()
- Manually advancing an iterator with next()
- Catching StopIteration once the iterator is exhausted
- Manual iteration using a while True loop with try/except
"""


def demo_manual_next_calls():
    print("=== 1. Manual next() calls ===")

    numbers = [10, 20, 30, 40, 50]
    print(f"Original iterable: {numbers}")

    numbers_iter = iter(numbers)
    print(f"Iterator created: {numbers_iter}")

    print(f"next() -> {next(numbers_iter)}")
    print(f"next() -> {next(numbers_iter)}")
    print(f"next() -> {next(numbers_iter)}")
    print(f"next() -> {next(numbers_iter)}")
    print(f"next() -> {next(numbers_iter)}")

    try:
        next(numbers_iter)
    except StopIteration:
        print("next() -> StopIteration raised: iterator is exhausted")

    print()


def demo_while_true_loop():
    print("=== 2. while True loop with try/except StopIteration ===")

    numbers = [10, 20, 30, 40, 50]
    print(f"Original iterable: {numbers}")

    numbers_iter = iter(numbers)
    print(f"Iterator created: {numbers_iter}")

    while True:
        try:
            value = next(numbers_iter)
            print(f"next() -> {value}")
        except StopIteration:
            print("StopIteration raised: exiting loop, iterator exhausted")
            break

    print()


if __name__ == "__main__":
    demo_manual_next_calls()
    demo_while_true_loop()
