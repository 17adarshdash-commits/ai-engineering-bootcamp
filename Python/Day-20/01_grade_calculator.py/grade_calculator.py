DATA_FILE = "grades.txt"


def load_students():
    students = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, math, science, english = [part.strip() for part in line.split(",")]

                students[name] = {
                    "math": float(math),
                    "science": float(science),
                    "english": float(english),
                }
    except FileNotFoundError:
        pass
    except ValueError:
        print("Warning: Data file is corrupted or contains invalid formats.")
    return students


def save_students():
    with open(DATA_FILE, "w") as file:
        for name, info in students.items():
            file.write(f"{name}, {info['math']}, {info['science']}, {info['english']}\n")


students = load_students()


def get_valid_name():
    while True:
        name = input("Enter Student Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        return name


def get_valid_marks(subject):
    while True:
        marks = input(f"Enter {subject} Marks: ").strip()
        try:
            marks = float(marks)
        except ValueError:
            print("Marks must be a number.")
            continue
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            continue
        return marks


def add_student():
    name = get_valid_name()
    math = get_valid_marks("Math")
    science = get_valid_marks("Science")
    english = get_valid_marks("English")

    students[name] = {'math': math, 'science': science, 'english': english}
    save_students()
    print("Student added successfully.")


def calculate_average(info):
    total = info['math'] + info['science'] + info['english']
    return total / 3


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def show_grades():
    if not students:
        print("No students found.\n")
        return

    for name, info in students.items():
        average = calculate_average(info)
        grade = calculate_grade(average)
        print(f"{name} - Average: {average:.2f}, Grade: {grade}")
    print()


def view_report():
    if not students:
        print("No students found.\n")
        return

    for name, info in students.items():
        total = info['math'] + info['science'] + info['english']
        average = calculate_average(info)
        grade = calculate_grade(average)

        print("-" * 32)
        print(f"\nName: {name}\n")
        print(f"Math: {info['math']:g}")
        print(f"Science: {info['science']:g}")
        print(f"English: {info['english']:g}\n")
        print(f"Total: {total:g}\n")
        print(f"Average: {average:.2f}\n")
        print(f"Grade: {grade}\n")
    print("-" * 32)


def display_menu():
    print(
        "\n===== Grade Calculator =====\n"
        "1. Add Student\n"
        "2. Calculate Grades\n"
        "3. View Report\n"
        "4. Exit\n"
    )


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_grades()
        elif choice == "3":
            view_report()
        elif choice == "4":
            print("Thank you for using the Grade Calculator.")
            break
        else:
            print("Invalid Choice. Please pick 1-4.")


if __name__ == "__main__":
    main()
