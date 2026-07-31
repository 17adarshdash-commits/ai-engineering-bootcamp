def factorial(n):

    if n <= 1:
        return n

    else:
        return n * factorial(n-1)

def sum_of_numbers(n):

    if n == 1:
        return 1

    else:
        return n + sum_of_numbers(n-1)

def countdown(n):

    if n == 1:
        print(1)
        return

    else:
        print(n)
        countdown(n-1)

def countup(n):

    if n == 1:
        print(1)
        return

    else:
        countup(n-1)
        print(n)

def power(base, exponent):

    if exponent <= 0:
        return 1

    else:
        return base * power(base, exponent-1)


if __name__ == "__main__":

    print("--- factorial ---")
    for value in [0, 1, 2, 5, 7]:
        print(f"factorial({value}) = {factorial(value)}")

    print("\n--- sum_of_numbers ---")
    for value in [1, 2, 5, 10]:
        print(f"sum_of_numbers({value}) = {sum_of_numbers(value)}")

    print("\n--- countdown ---")
    for value in [1, 3, 5]:
        print(f"countdown({value}):")
        countdown(value)

    print("\n--- countup ---")
    for value in [1, 3, 5]:
        print(f"countup({value}):")
        countup(value)

    print("\n--- power ---")
    for base, exponent in [(2, 0), (2, 5), (3, 4), (5, 1), (10, 3)]:
        print(f"power({base}, {exponent}) = {power(base, exponent)}")
