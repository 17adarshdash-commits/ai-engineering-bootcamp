"""
main.py

Command-line interface for the Banking System V2.
"""

from bank import Bank
from exceptions import BankError

DATA_FILE = "accounts.json"

MENU = """
============= Banking System V2 =============
1. Create Account
2. Deposit
3. Withdraw
4. Transfer Between Accounts
5. Search Account
6. Display Accounts
7. Save Accounts to JSON
8. Load Accounts from JSON
9. Exit
===============================================
"""


def create_account(bank):
    account_number = input("Enter account number: ").strip()
    holder_name = input("Enter account holder name: ").strip()
    account_type = input("Enter account type (Savings/Current): ").strip()
    opening_date = input("Enter opening date (YYYY-MM-DD): ").strip()
    balance = input("Enter opening balance [0]: ").strip() or 0

    try:
        bank.create_account(account_number, holder_name, account_type, opening_date, balance)
        print("Account created successfully.")
    except BankError as e:
        print(f"Error: {e}")


def deposit(bank):
    account_number = input("Enter account number: ").strip()
    amount = input("Enter deposit amount: ").strip()

    try:
        account = bank.deposit(account_number, amount)
        print(f"Deposit successful. New balance: {account.balance:.2f}")
    except BankError as e:
        print(f"Error: {e}")


def withdraw(bank):
    account_number = input("Enter account number: ").strip()
    amount = input("Enter withdrawal amount: ").strip()

    try:
        account = bank.withdraw(account_number, amount)
        print(f"Withdrawal successful. New balance: {account.balance:.2f}")
    except BankError as e:
        print(f"Error: {e}")


def transfer(bank):
    from_account_number = input("Enter source account number: ").strip()
    to_account_number = input("Enter destination account number: ").strip()
    amount = input("Enter transfer amount: ").strip()

    try:
        from_account, to_account = bank.transfer(from_account_number, to_account_number, amount)
        print(
            f"Transfer successful. {from_account.account_number} balance: "
            f"{from_account.balance:.2f} | {to_account.account_number} balance: "
            f"{to_account.balance:.2f}"
        )
    except BankError as e:
        print(f"Error: {e}")


def search_account(bank):
    keyword = input("Enter search keyword (account number/holder/type): ").strip()
    results = bank.search_account(keyword)
    if not results:
        print("No matching accounts found.")
        return

    for account in results:
        print(account)


def display_accounts(bank):
    bank.display_accounts()


def save_accounts(bank):
    filepath = input(f"Enter filepath to save [{DATA_FILE}]: ").strip() or DATA_FILE
    bank.save_to_json(filepath)
    print(f"Accounts saved to '{filepath}'.")


def load_accounts(bank):
    filepath = input(f"Enter filepath to load [{DATA_FILE}]: ").strip() or DATA_FILE
    try:
        bank.load_from_json(filepath)
        print(f"Accounts loaded from '{filepath}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")


def main():
    bank = Bank()

    actions = {
        "1": create_account,
        "2": deposit,
        "3": withdraw,
        "4": transfer,
        "5": search_account,
        "6": display_accounts,
        "7": save_accounts,
        "8": load_accounts,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "9":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action(bank)


if __name__ == "__main__":
    main()
