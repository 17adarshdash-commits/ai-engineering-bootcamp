def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2

while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    
    try:
        choice = int(input("\nEnter choice (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue

    if choice == 5:
        print("Program Complete!")
        break

    if choice not in [1, 2, 3, 4]:
        print("Invalid Choice. Please pick 1, 2, 3, 4, or 5.\n")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid numeric value. Restarting menu.\n")
        continue

    if choice == 1:
        print(f"Sum: {add(num1, num2)}\n")
    elif choice == 2:
        print(f"Difference: {subtract(num1, num2)}\n")
    elif choice == 3:
        print(f"Product: {multiply(num1, num2)}\n")
    elif choice == 4:
        print(f"Quotient: {divide(num1, num2)}\n")
