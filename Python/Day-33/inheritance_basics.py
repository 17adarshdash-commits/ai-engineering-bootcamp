class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name} is {self.age} years old")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_info(self):
        print(f"Student's name is {self.name}, {self.age} years old, enrolled in {self.course}")

    def study(self):
        print(f"{self.name} is studying {self.course}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        print(f"Teacher's name is {self.name}, {self.age} years old, teaches {self.subject}")

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")


if __name__ == "__main__":
    s = Student("Alice", 20, "Computer Science")
    t = Teacher("Bob", 45, "Mathematics")

    s.display_info()
    s.study()

    t.display_info()
    t.teach()
