def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

def reverse_string(text):
    if len(text) == 0:
        return ""
    else:
        return text[-1] + reverse_string(text[:len(text) - 1])
    
def count_digits(number):
    if 0 <= number <= 9:
        return 1
    else:
        return 1 + count_digits(number//10)

print("Fibonacci(6):", fibonacci(6))
print("Power(2, 5):", power(2, 5))
print("Reverse:", reverse_string("python"))
print("Digits:", count_digits(123456))