class Student:
    def __init__(self, name, age, branch, cgpa):
        self.name = name
        self.age = age
        self.branch = branch
        self.cgpa = cgpa

    def display_info(self):
        print(f"{self.name} is {self.age} years old majoring in {self.branch} with a CGPA of {self.cgpa}.")

student1 = Student("Adarsh Dash",19,"CSE-AI",8.9)
student2 = Student("Ritvik Kumar",19,"IT",8.75)

student1.display_info()
student2.display_info()