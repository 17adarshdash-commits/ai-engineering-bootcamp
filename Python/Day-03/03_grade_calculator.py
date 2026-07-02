marks = float(input("Enter marks: "))
if marks > 100 or marks < 0:
    print("Invalid Entry")
else:
    if 90 <= marks <= 100:
        print("A")
    elif 80 <= marks <= 89:
        print("B")
    elif 70 <= marks <= 79:
        print("C")
    elif 60 <= marks <= 69:
        print("D")
    else:
        print("F") 