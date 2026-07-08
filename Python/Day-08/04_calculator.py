try:
    num1 = float(input("Enter number 1: "))
    operator = input("Enter operator (+,-,*,/): ")
    num2 = float(input("Enter number 2: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2 
    else:
        result = "Invalid operator entered."

except ValueError:
    print("Error: Invalid number entered.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(result)
finally:
    print("Calculator program ended.")