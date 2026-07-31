def reverse_string(text):

    if len(text) == 0:
        return ""
    else:
        return text[-1] + reverse_string(text[:-1])

def is_palindrome(text):
    if len(text) < 2:
        return True

    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
        
    return False

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

if __name__ == "__main__":
    print("--- reverse_string ---")
    print(reverse_string("hello"))
    print(reverse_string("Python"))
    print(reverse_string(""))
    print(reverse_string("a"))

    print("--- is_palindrome ---")
    print(is_palindrome("racecar"))
    print(is_palindrome("madam"))
    print(is_palindrome("hello"))
    print(is_palindrome(""))
    print(is_palindrome("a"))

    print("--- binary_search_recursive ---")
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    for target in [1, 7, 15, 4, 20, -1]:
        result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
        print(f"target={target} -> index={result}")

    print("--- fibonacci ---")
    for n in [0, 1, 5, 10]:
        print(f"fibonacci({n}) = {fibonacci(n)}")
