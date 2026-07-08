while True:
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Invalid input.")
    else:
        print(age)
        break