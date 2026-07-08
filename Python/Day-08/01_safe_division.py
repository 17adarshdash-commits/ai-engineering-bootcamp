num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

try:
    x = num1 / num2
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print(x)
finally:
    print("Program done!")