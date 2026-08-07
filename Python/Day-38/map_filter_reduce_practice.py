from functools import reduce

# 1. map() - square each number
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

# 2. filter() - keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 3. reduce() - product of all numbers
product_of_numbers = reduce(lambda x, y: x * y, numbers)

# 4. Extra Practice
names = ["alice", "bob", "charlie", "dave"]
uppercase_names = list(map(lambda name: name.upper(), names))

words = ["cat", "elephant", "dog", "giraffe", "ant", "butterfly"]
filtered_words = list(filter(lambda word: len(word) > 5, words))

# Testing Section
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Even numbers:", even_numbers)
print("Product of all numbers:", product_of_numbers)

print("Original names:", names)
print("Uppercase names:", uppercase_names)

print("Original words:", words)
print("Filtered words:", filtered_words)
