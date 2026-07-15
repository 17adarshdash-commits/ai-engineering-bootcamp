def add_task():
    task = input("Add task: ")
    with open("todo.txt","a") as file:
        file.write(f"{task}\n")
        print("Task added.\n")

def view_tasks():
    with open("todo.txt","r") as file:
        print(file.read())
        print()

while True:

    choice = int(input("1. Add Task\n2. View Tasks\n3. Exit\nEnter choice: "))

    if choice == 1:
        add_task()
        continue

    elif choice == 2:
        view_tasks()
    
    elif choice == 3:
        print("Thanks for using the todo list app!")
        break

    else:
        print("Invalid choice!")