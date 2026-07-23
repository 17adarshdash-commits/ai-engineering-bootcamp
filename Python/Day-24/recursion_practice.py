"""
===========================================
Recursion Practice
Day 24
===========================================

Topics:
1. Factorial
2. Sum of first n numbers
3. Print numbers from 1 to n
4. Print numbers from n to 1
"""

# -----------------------------------------
# 1. Factorial
# -----------------------------------------

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


# -----------------------------------------
# 2. Sum of first n numbers
# -----------------------------------------

def sum_n(n):
    if n == 1:
        return 1

    return n + sum_n(n - 1)


# -----------------------------------------
# 3. Print numbers from 1 to n
# -----------------------------------------

def print_1_to_n(n):
    if n == 1:
        print(1)
        return

    print_1_to_n(n - 1)
    print(n)


# -----------------------------------------
# 4. Print numbers from n to 1
# -----------------------------------------

def print_n_to_1(n):
    if n == 1:
        print(1)
        return

    print(n)
    print_n_to_1(n - 1)


# -----------------------------------------
# Testing
# -----------------------------------------

print("Factorial of 5:", factorial(5))
print()

print("Sum of first 5 numbers:", sum_n(5))
print()

print("Numbers from 1 to 5:")
print_1_to_n(5)
print()

print("Numbers from 5 to 1:")
print_n_to_1(5)