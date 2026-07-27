def product_digits(num):
    if 0 <= num <= 9:
        return num
    else:
        return (num % 10) * product_digits(num // 10)
    
print(product_digits(234))

def decimal_to_binary(n):
    
    if n == 0:
        return 0
    
    else:
        return (n % 2) + 10 * decimal_to_binary(n // 2)

print(decimal_to_binary(10)) 

def count_uppercase(text):
    cnt = 0
    if len(text) == 0:
        return 0
    else:
        if text[-1].isupper():
            cnt += 1
        else:
            cnt += 0
        return cnt + count_uppercase(text[:len(text)- 1])
    
print(count_uppercase("HeLLo"))

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[-1] + sum_list(numbers[:-1])
    
print(sum_list([2,4,6,8]))