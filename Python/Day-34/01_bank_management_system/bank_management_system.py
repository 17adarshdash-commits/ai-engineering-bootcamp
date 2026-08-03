import json
import os

ACCOUNTS_FILE = "accounts.json"


class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.account_number = account_number
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount

    def display_balance(self):
        print(f"Account {self.account_number} ({self.owner}): ${self.balance:.2f}")

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "owner": self.owner,
            "balance": self.balance,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["account_number"], data["owner"], data["balance"])


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, owner, balance=0.0):
        if account_number in self.accounts:
            raise ValueError(f"Account {account_number} already exists.")
        self.accounts[account_number] = BankAccount(account_number, owner, balance)
        return self.accounts[account_number]

    def delete_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError(f"Account {account_number} not found.")
        del self.accounts[account_number]

    def search_account(self, account_number):
        return self.accounts.get(account_number)

    def display_accounts(self):
        if not self.accounts:
            print("No accounts found.")
            return
        for account in self.accounts.values():
            account.display_balance()

    def save_json(self, filepath=ACCOUNTS_FILE):
        with open(filepath, "w") as f:
            json.dump([acc.to_dict() for acc in self.accounts.values()], f, indent=4)

    def load_json(self, filepath=ACCOUNTS_FILE):
        if not os.path.exists(filepath):
            return
        with open(filepath, "r") as f:
            data = json.load(f)
        for item in data:
            account = BankAccount.from_dict(item)
            self.accounts[account.account_number] = account


def show_menu():
    print("\n--- Bank Management System ---")
    print("1. Add Account")
    print("2. Delete Account")
    print("3. Search Account")
    print("4. Display Accounts")
    print("5. Deposit")
    print("6. Withdraw")
    print("7. Exit")


def main():
    bank = Bank()
    bank.load_json()

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            account_number = input("Enter Account Number: ").strip()
            owner = input("Enter Owner Name: ").strip()
            if not owner:
                print("Owner name cannot be empty.")
                continue
            try:
                balance = float(input("Enter Initial Balance (default 0): ").strip() or 0)
                bank.add_account(account_number, owner, balance)
                print("Account added.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            account_number = input("Enter Account Number: ").strip()
            try:
                bank.delete_account(account_number)
                print("Account deleted.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            account_number = input("Enter Account Number: ").strip()
            account = bank.search_account(account_number)
            if account:
                account.display_balance()
            else:
                print("Account not found.")

        elif choice == "4":
            bank.display_accounts()

        elif choice == "5":
            account_number = input("Enter Account Number: ").strip()
            account = bank.search_account(account_number)
            if not account:
                print("Account not found.")
                continue
            try:
                amount = float(input("Enter Deposit Amount: ").strip())
                account.deposit(amount)
                print("Deposit successful.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "6":
            account_number = input("Enter Account Number: ").strip()
            account = bank.search_account(account_number)
            if not account:
                print("Account not found.")
                continue
            try:
                amount = float(input("Enter Withdrawal Amount: ").strip())
                account.withdraw(amount)
                print("Withdrawal successful.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "7":
            bank.save_json()
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
