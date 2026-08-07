"""
Context Managers Practice
Implementing a custom Timer context manager using __enter__() and __exit__().
"""

import time


class Timer:
    """Context manager that records and prints the elapsed time of a code block."""

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {self.elapsed_time:.6f} seconds")
        # Returning False (or None) lets any exception propagate normally.
        return False


if __name__ == "__main__":
    # 1. Summing a large range
    print("Summing a large range:")
    with Timer():
        total = sum(range(1_000_000))
    print(f"Total: {total}\n")

    # 2. Building a list with a loop
    print("Building a list with a loop:")
    with Timer():
        squares = []
        for i in range(100_000):
            squares.append(i ** 2)
    print(f"List length: {len(squares)}\n")

    # 3. Sleeping for one second
    print("Sleeping for one second:")
    with Timer():
        time.sleep(1)
    print()

    # 4. Bonus: a block that raises an exception, showing __exit__ still runs
    print("Handling an exception inside the context:")
    try:
        with Timer():
            raise ValueError("Something went wrong")
    except ValueError as e:
        print(f"Caught exception: {e}")
