balance = 0

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))

    if amount < 0:
        print("Cannot deposit negative money.\n")
    
    else:
        balance += amount
        print(f"₹{amount} added.\n")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print(f"₹{amount} withdrawn.\n")

    else:
        print("Insufficient Balance\n")

def check_balance():
    global balance
    print(f"Balance: ₹{balance}\n")

while True:

    choice = int(input("1. Deposit Money\n2. Withdraw Money\n3. Check Balance Amount\n4. Exit\n\nEnter Choice: "))

    if choice == 1:
        deposit()
        continue

    elif choice == 2:
        withdraw()
        continue

    elif choice == 3:
        check_balance()
        continue

    elif choice == 4:
        print("Thank you for your time. Hope you have a great day!")
        break

    else:
        print("Invalid Choice")
        continue

