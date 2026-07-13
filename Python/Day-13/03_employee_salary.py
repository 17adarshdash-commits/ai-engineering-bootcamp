class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def set_salary(self, salary_entered):
        if salary_entered < 0:
            print("Salary can't be negative.")
        else:
            self.__salary = salary_entered
            print("Updated salary.")

    def get_salary(self):
        return self.__salary
    
employee = Employee(10000)
employee.set_salary(1500000)
print(f"Salary: {employee.get_salary()}")