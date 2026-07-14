import datetime

year_of_birth = int(input("Enter birth year: "))

current_age = datetime.datetime.now().year - year_of_birth

print(f"Age: {current_age}")