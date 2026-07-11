class BankAccount:
    def __init__(self, accountholder, balance):
        self.accountholder = accountholder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} deposited to account!")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn!")
        else:
            print("Insufficient Balance.")
    
    def display_balance(self):
        print(f"Current Balance: {self.balance}")

account1 = BankAccount("Adarsh" , 500)
account1.deposit(500)
account1.display_balance()
account1.withdraw(1250)
account1.display_balance()