class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}, Course: {self.course}")

    def update_course(self, new_course):
        self.course = new_course
        print(f"{self.name}'s course updated to {new_course}")


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}")

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine has started.")


class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print(f"Deposit failed: amount ({amount}) cannot be negative.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal failed: amount ({amount}) exceeds balance ({self.balance}).")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account {self.account_number} ({self.owner}) balance: {self.balance}")


if __name__ == "__main__":
    print("--- Student Tests ---")
    student1 = Student("Alice", 21, "Computer Science")
    student2 = Student("Bob", 23, "Mathematics")

    student1.display_info()
    student2.display_info()

    student1.update_course("Data Science")
    student1.display_info()

    print("\n--- Car Tests ---")
    car1 = Car("Toyota", "Corolla", 2022)
    car2 = Car("Tesla", "Model 3", 2024)

    car1.display_info()
    car1.start_engine()

    car2.display_info()
    car2.start_engine()

    print("\n--- BankAccount Tests ---")
    account1 = BankAccount("ACC001", "Alice", 1000)
    account1.display_balance()

    # Valid deposit
    account1.deposit(500)

    # Invalid deposit (negative amount)
    account1.deposit(-200)

    # Valid withdrawal
    account1.withdraw(300)

    # Invalid withdrawal (more than balance)
    account1.withdraw(5000)

    account1.display_balance()

    account2 = BankAccount("ACC002", "Bob")
    account2.display_balance()
    account2.deposit(100)
    account2.withdraw(50)
    account2.withdraw(1000)
    account2.display_balance()
