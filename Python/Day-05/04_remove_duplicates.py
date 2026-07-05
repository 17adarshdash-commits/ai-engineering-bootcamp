numbers = [1,2,2,3,4,4,5]

numbers_without_duplicates = []
for number in numbers:
    if number not in numbers_without_duplicates:
        numbers_without_duplicates.append(number)

print(numbers_without_duplicates)