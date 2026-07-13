class BankAccount:
    def __init__(self,balance = 1000):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Witndrawal successful.")
        else:
            print("Insufficient Balance.")
    
    def get_balance(self):
        return self.__balance 
    
account = BankAccount()
account.withdraw(500)
print(f"Balance: {account.get_balance()}")