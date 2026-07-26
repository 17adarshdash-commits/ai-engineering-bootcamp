def is_palindrome(text):
    if len(text) == 0:
        return ""
    else:
        return text[-1] + is_palindrome(text[:len(text) - 1])

text = "madam"
reverse_string = is_palindrome(text)   
print(reverse_string == text)

def sum_digits(number):
    if 0 <= number <= 9:
        return number
    else:
        return (number % 10) + sum_digits(number//10)
    
print(sum_digits(12345))

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print(gcd(24,18))

def count_vowels(text):
    
    if not text:
        return 0
   
    is_vowel = 1 if text[-1].lower() in "aeiou" else 0
    
    return is_vowel + count_vowels(text[:-1])

print(count_vowels("OpenAI"))
