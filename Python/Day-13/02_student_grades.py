class Student:
    def __init__(self, marks= 0):
        self.__marks = marks

    def set_marks(self, marks_entered):
        if marks_entered < 0:
            print("Invalid Entry.")
        elif marks_entered > 100:
            print("Invalid Entry.")
        else:
            self.__marks = marks_entered

    def get_marks(self):
        return self.__marks
    
student = Student()
student.set_marks(101)
print(f"Marks: {student.get_marks()}")