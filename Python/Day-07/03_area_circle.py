import math
def area(radius):
    r = radius
    return math.pi * (r ** 2)
radius = float(input("Enter radius: "))
print(f"Area: {area(radius):.2f}")