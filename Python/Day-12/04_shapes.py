import math
class Shape:
    def area(self):
        print("Area cannot be calculated.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"Rectangle Area: {area}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * math.pow(self.radius, 2)
        print(f"Circle Area: {area}")

rectangle = Rectangle(10, 50)
circle = Circle(25)

rectangle.area()
circle.area()