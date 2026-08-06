"""
Day 37: Built-in Modules Practice
Demonstrates: math, random, datetime, os
"""

import math
import random
import datetime
import os


# ---------------------------------------------------------------------------
# math module
# ---------------------------------------------------------------------------
def math_demo():
    print("\n--- math module ---")

    number = 25
    print(f"sqrt({number}) = {math.sqrt(number)}")

    base, exponent = 2, 10
    print(f"pow({base}, {exponent}) = {math.pow(base, exponent)}")

    value = 4.2
    print(f"ceil({value}) = {math.ceil(value)}")
    print(f"floor({value}) = {math.floor(value)}")


# ---------------------------------------------------------------------------
# random module
# ---------------------------------------------------------------------------
def random_demo():
    print("\n--- random module ---")

    low, high = 1, 100
    print(f"randint({low}, {high}) = {random.randint(low, high)}")

    fruits = ["apple", "banana", "cherry", "mango", "orange"]
    print(f"choice(fruits) = {random.choice(fruits)}")

    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print(f"shuffle(numbers) -> {numbers}")


# ---------------------------------------------------------------------------
# datetime module
# ---------------------------------------------------------------------------
def datetime_demo():
    print("\n--- datetime module ---")

    today = datetime.date.today()
    print(f"Current date: {today}")

    current_time = datetime.datetime.now().time()
    print(f"Current time: {current_time}")

    now = datetime.datetime.now()
    print(f"Current date & time: {now}")

    formatted = now.strftime("%A, %d %B %Y - %I:%M:%S %p")
    print(f"Formatted date (strftime): {formatted}")


# ---------------------------------------------------------------------------
# os module
# ---------------------------------------------------------------------------
def os_demo():
    print("\n--- os module ---")

    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")

    files = os.listdir(cwd)
    print(f"Files in current directory: {files}")

    file_to_check = __file__
    exists = os.path.exists(file_to_check)
    print(f"Does '{os.path.basename(file_to_check)}' exist? {exists}")


if __name__ == "__main__":
    math_demo()
    random_demo()
    datetime_demo()
    os_demo()
