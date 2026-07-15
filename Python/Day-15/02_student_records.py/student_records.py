def add_student():
    
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    data = f"{name} : {marks}"

    with open("students.txt","a") as file:
        file.write(f"{data}\n")
        print("Student entry added.\n")

def view_students():

    with open("students.txt","r") as file:
        content = file.read()
        print(f"{content}\n")

while True:

    choice = int(input("1. Add Student\n2. View Students\n3. Exit\nEnter choice: "))
    if choice == 1:
        add_student()
        continue

    elif choice == 2:
        view_students()
    
    elif choice == 3:
        print("Thanks for using the Student Records app!")
        break

    else:
        print("Invalid choice!")

