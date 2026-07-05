numbers = [4, 7, 1, 20, 15]

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number

second_largest = numbers[0]
for number in numbers:
    if number < largest and number > second_largest:
        second_largest = number

print(second_largest)