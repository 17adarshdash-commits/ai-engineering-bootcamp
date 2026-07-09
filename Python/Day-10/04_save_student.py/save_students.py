number_of_students = int(input("Enter number of students: "))

for i in range(number_of_students):
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))

    with open("students.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Branch: {branch}\n")
        file.write(f"CGPA: {cgpa}\n")
        file.write(f"------------------------\n")

    print("Student saved successfully!")