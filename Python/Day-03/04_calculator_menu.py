num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
operation = int(input("Choose\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n"))

if operation == 1:
    print(num1+num2)
elif operation == 2:
    print(num1-num2)
elif operation == 3:
    print(num1*num2)
elif operation == 4:
    print(num1/num2)
else:
    print("Invalid Choice")