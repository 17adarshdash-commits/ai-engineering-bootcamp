import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

    def give_raise(self, percent):
        if percent < 0:
            raise ValueError("Raise percent cannot be negative")
        self.monthly_salary += self.monthly_salary * (percent / 100)
        print(f"{self.name}'s new monthly salary: {self.monthly_salary:.2f}")


if __name__ == "__main__":
    print("--- Rectangle ---")
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(10, 2)
    print(f"rect1 area: {rect1.area()}, perimeter: {rect1.perimeter()}")
    print(f"rect2 area: {rect2.area()}, perimeter: {rect2.perimeter()}")

    print("\n--- Circle ---")
    circle1 = Circle(3)
    circle2 = Circle(7.5)
    print(f"circle1 area: {circle1.area():.2f}, circumference: {circle1.circumference():.2f}")
    print(f"circle2 area: {circle2.area():.2f}, circumference: {circle2.circumference():.2f}")

    print("\n--- Employee ---")
    emp1 = Employee("Alice", 5000)
    emp2 = Employee("Bob", 4000)

    print(f"{emp1.name} annual salary: {emp1.annual_salary()}")
    print(f"{emp2.name} annual salary: {emp2.annual_salary()}")

    emp1.give_raise(10)
    print(f"{emp1.name} annual salary after raise: {emp1.annual_salary()}")

    emp2.give_raise(0)

    print("\nTesting invalid raise (negative percent):")
    try:
        emp1.give_raise(-5)
    except ValueError as e:
        print(f"Error: {e}")
