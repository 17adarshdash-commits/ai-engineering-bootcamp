from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    circle = Circle(3)

    print(f"Rectangle area: {rectangle.area()}")
    print(f"Circle area: {circle.area()}")

    try:
        shape = Shape()
    except TypeError as e:
        print(f"TypeError: {e}")
