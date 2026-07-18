def load_students():
    students = {}
    try:
        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, age, grade = [part.strip() for part in line.split(",")]
                students[name] = {"age": int(age), "grade": grade}
    except FileNotFoundError:
        pass
    return students

students = load_students()

def add_student():
    
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")

    students[name] = {"age": age, "grade": grade}

    data = f"{name}, {age}, {grade}\n"

    with open("students.txt","a") as file:
        file.write(data)

    print("Student Record added successsfully.")

def view_students():
    try:
        with open("students.txt","r") as file:
            content = file.read()
            print(f"{content}\n")
    except FileNotFoundError:
        print("No students recorded yet.\n")

def search_student():
    name = input("Enter Student Name: ")
    if name in students:
        info = students[name]
        print(f"\nStudent Found:\nName: {name}\nAge: {info['age']}\nGrade: {info['grade']}\n")
    else:
        print("Student not found.\n")

while True:
    choice = int(input("1. Add Student\n2. View Students\n3. Search Student\n4. Exit\n\nEnter choice: "))

    if choice == 1:
        add_student()
        continue

    elif choice == 2:
        view_students()
        continue

    elif choice == 3:
        search_student()
        continue

    elif choice == 4:
        print("Thank you for using Student Database.")
        break

    else:
        print("Invalid Choice. Please pick 1, 2, 3, or 4.\n")
        continue