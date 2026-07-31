DATA_FILE = "tasks.txt"
VALID_PRIORITIES = ("High", "Medium", "Low")


def load_tasks():
    tasks = []
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                title, priority, status = [part.strip() for part in line.split(",")]
                tasks.append({"title": title, "priority": priority, "status": status})
    except FileNotFoundError:
        pass
    except ValueError:
        print("Warning: Data file is corrupted or contains invalid formats.")
    return tasks


def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['title']}, {task['priority']}, {task['status']}\n")


def get_valid_title():
    while True:
        title = input("Task Title: ").strip()
        if not title:
            print("Title cannot be empty.")
            continue
        return title


def get_valid_priority():
    while True:
        priority = input("Priority (High/Medium/Low): ").strip().capitalize()
        if priority not in VALID_PRIORITIES:
            print("Priority must be High, Medium, or Low.")
            continue
        return priority


def add_task(tasks):
    title = get_valid_title()
    priority = get_valid_priority()

    tasks.append({"title": title, "priority": priority, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print("========================\n")
        print(f"Task #{index}\n")
        print(f"Title: {task['title']}")
        print(f"Priority: {task['priority']}")
        print(f"Status: {task['status']}\n")
    print("========================")


def choose_task_number(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']}")

    choice = input("Enter task number: ").strip()
    try:
        number = int(choice)
    except ValueError:
        print("Task number must be an integer.")
        return None

    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return None

    return number - 1


def mark_complete(tasks):
    if not tasks:
        print("No tasks available.")
        return

    index = choose_task_number(tasks)
    if index is None:
        return

    tasks[index]["status"] = "Completed"
    save_tasks(tasks)
    print("Task marked as complete.")


def delete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    index = choose_task_number(tasks)
    if index is None:
        return

    del tasks[index]
    save_tasks(tasks)
    print("Task deleted successfully.")


def search_task(tasks):
    keyword = input("Enter keyword: ").strip().lower()
    matches = [task for task in tasks if keyword in task["title"].lower()]

    if not matches:
        print("No matching tasks found.")
        return

    for index, task in enumerate(matches, start=1):
        print("========================\n")
        print(f"Task #{index}\n")
        print(f"Title: {task['title']}")
        print(f"Priority: {task['priority']}")
        print(f"Status: {task['status']}\n")
    print("========================")


def display_menu():
    print(
        "===== Task Manager =====\n\n"
        "1. Add Task\n"
        "2. View Tasks\n"
        "3. Mark Task as Complete\n"
        "4. Delete Task\n"
        "5. Search Task\n"
        "6. Exit\n"
    )


def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_task(tasks)
        elif choice == "6":
            print("Thank you for using the Task Manager.")
            break
        else:
            print("Invalid Choice. Please pick 1-6.")

        print()


if __name__ == "__main__":
    main()
