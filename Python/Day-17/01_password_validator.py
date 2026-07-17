password = input("Enter Password: ")

has_upper = False
has_lower = False
has_number = False

if len(password) < 8:
    print("Length of password is lesser than 8 characters. Invalid password.")

else:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isnumeric():
            has_num = True

    if not has_upper:
        print("Password doesn't contain an uppercase character. Invalid password.")
    elif not has_lower:
        print("Password doesn't contain a lowercase character. Invalid password.")
    elif not has_num:
        print("Password doesn't contain a number. Invalid password.")
    else:
        print("Password is valid.")

        
            