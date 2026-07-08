def check_age(age):
    if age < 18:
        raise ValueError("Not old enough to be granted access.")
    else:
        print("Access Granted.")
try:
    age = int(input("Enter age: "))
    check_age(age)
except ValueError as e:
    print(f"Access Denied: {e}")