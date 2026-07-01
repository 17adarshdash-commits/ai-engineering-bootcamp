a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"Before: a={a}, b={b}")

a, b = b, a
print(f"After: a={a}, b={b}")