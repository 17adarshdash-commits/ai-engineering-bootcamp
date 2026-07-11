class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        area_of_rectangle = self.length * self.width
        return area_of_rectangle
    
    def perimeter(self):
        perimeter_of_rectangle = 2 * (self.length + self.width)
        return perimeter_of_rectangle
    
rect1 = Rectangle(20, 10)

print(f"Area of rectangle: {rect1.area()}")
print(f"Perimeter of rectangle: {rect1.perimeter()}")