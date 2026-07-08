try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    x = num1 / num2
except ValueError:
    print("Invalid input. Please enter integers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(x)
finally:
    print("Program finished.")