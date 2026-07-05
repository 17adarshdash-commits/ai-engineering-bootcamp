numbers = [4, 7, 1, 20, 15]

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)