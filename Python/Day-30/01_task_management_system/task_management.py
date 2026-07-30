import csv
import os
from datetime import datetime

TASKS_FILE = "tasks.txt"
BACKUP_FILE = "tasks_backup.txt"
CSV_FILE = "tasks_export.csv"
REPORT_FILE = "task_report.txt"

PRIORITIES = ("High", "Medium", "Low")
PRIORITY_RANK = {"High": 0, "Medium": 1, "Low": 2}
STATUSES = ("Pending", "Completed")

tasks = {}


def load_tasks():
    """Load tasks from TASKS_FILE into the tasks dict, if it exists."""
    if not os.path.exists(TASKS_FILE):
        return

    with open(TASKS_FILE, "r", newline="") as f:
        for row in csv.reader(f):
            if not row:
                continue
            if len(row) != 5:
                continue
            task_id, title, priority, status, due_date = row
            tasks[int(task_id)] = {
                "id": int(task_id),
                "title": title,
                "priority": priority,
                "status": status,
                "due_date": due_date,
            }


def save_tasks():
    """Write all tasks to TASKS_FILE."""
    with open(TASKS_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for task in tasks.values():
            writer.writerow(
                [task["id"], task["title"], task["priority"],
                 task["status"], task["due_date"]]
            )


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def add_task():
    try:
        task_id = int(input("Enter Task ID: ").strip())
    except ValueError:
        print("Task ID must be a number.")
        return

    if task_id in tasks:
        print("ID already exists.")
        return

    title = input("Enter Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    priority = input(f"Enter Priority {PRIORITIES}: ").strip().title()
    if priority not in PRIORITIES:
        print("Invalid priority.")
        return

    status = input(f"Enter Status {STATUSES}: ").strip().title()
    if status not in STATUSES:
        print("Invalid status.")
        return

    due_date = input("Enter Due Date (YYYY-MM-DD): ").strip()
    if not validate_due_date(due_date):
        print("Invalid due date.")
        return

    tasks[task_id] = {
        "id": task_id,
        "title": title,
        "priority": priority,
        "status": status,
        "due_date": due_date,
    }
    save_tasks()
    print("Task added successfully.")


def delete_task():
    try:
        task_id = int(input("Enter Task ID to delete: ").strip())
    except ValueError:
        print("Task ID must be a number.")
        return

    if task_id not in tasks:
        print("No task found with that ID.")
        return

    del tasks[task_id]
    save_tasks()
    print("Task deleted successfully.")


def update_task():
    try:
        task_id = int(input("Enter Task ID to update: ").strip())
    except ValueError:
        print("Task ID must be a number.")
        return

    if task_id not in tasks:
        print("No task found with that ID.")
        return

    task = tasks[task_id]

    title = input(f"Enter new Title [{task['title']}]: ").strip()
    if title:
        task["title"] = title

    priority = input(f"Enter new Priority {PRIORITIES} [{task['priority']}]: ").strip().title()
    if priority:
        if priority not in PRIORITIES:
            print("Invalid priority. Update to priority skipped.")
        else:
            task["priority"] = priority

    status = input(f"Enter new Status {STATUSES} [{task['status']}]: ").strip().title()
    if status:
        if status not in STATUSES:
            print("Invalid status. Update to status skipped.")
        else:
            task["status"] = status

    due_date = input(f"Enter new Due Date [{task['due_date']}]: ").strip()
    if due_date:
        if not validate_due_date(due_date):
            print("Invalid due date. Update to due date skipped.")
        else:
            task["due_date"] = due_date

    save_tasks()
    print("Task updated successfully.")


def print_task(task):
    print("--------------------------------")
    print(f"ID       : {task['id']}")
    print(f"Title    : {task['title']}")
    print(f"Priority : {task['priority']}")
    print(f"Status   : {task['status']}")
    print(f"Due Date : {task['due_date']}")
    print("--------------------------------")


def print_tasks(task_list):
    if not task_list:
        print("No tasks to display.")
        return

    for task in task_list:
        print_task(task)


def display_tasks():
    print_tasks(tasks.values())


def search_by_id():
    try:
        task_id = int(input("Enter Task ID to search: ").strip())
    except ValueError:
        print("Task ID must be a number.")
        return

    task = tasks.get(task_id)
    if task is None:
        print("No task found with that ID.")
        return

    print_task(task)


def search_by_title():
    query = input("Search by Title: ").strip().lower()
    found = [t for t in tasks.values() if query in t["title"].lower()]
    print_tasks(found)


def search_by_status():
    status = input(f"Enter Status {STATUSES}: ").strip().title()
    if status not in STATUSES:
        print("Invalid status.")
        return

    found = [t for t in tasks.values() if t["status"] == status]
    print_tasks(found)


def filter_pending():
    print_tasks([t for t in tasks.values() if t["status"] == "Pending"])


def filter_completed():
    print_tasks([t for t in tasks.values() if t["status"] == "Completed"])


def filter_high_priority():
    print_tasks([t for t in tasks.values() if t["priority"] == "High"])


def sort_by_due_date():
    print_tasks(sorted(tasks.values(), key=lambda t: t["due_date"]))


def sort_by_priority():
    print_tasks(sorted(tasks.values(), key=lambda t: PRIORITY_RANK[t["priority"]]))


def sort_by_title():
    print_tasks(sorted(tasks.values(), key=lambda t: t["title"].lower()))


def export_csv():
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "Priority", "Status", "Due Date"])
        for task in tasks.values():
            writer.writerow(
                [task["id"], task["title"], task["priority"],
                 task["status"], task["due_date"]]
            )
    print(f"Tasks exported to {CSV_FILE}.")


def backup_tasks():
    with open(BACKUP_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for task in tasks.values():
            writer.writerow(
                [task["id"], task["title"], task["priority"],
                 task["status"], task["due_date"]]
            )
    print(f"Backup created at {BACKUP_FILE}.")


def generate_report():
    status_counts = {}
    priority_counts = {}
    for task in tasks.values():
        status_counts[task["status"]] = status_counts.get(task["status"], 0) + 1
        priority_counts[task["priority"]] = priority_counts.get(task["priority"], 0) + 1

    with open(REPORT_FILE, "w") as f:
        f.write(f"Total Tasks: {len(tasks)}\n\n")

        f.write("By Status:\n")
        for status in STATUSES:
            f.write(f"{status.ljust(10)} : {status_counts.get(status, 0)}\n")

        f.write("\nBy Priority:\n")
        for priority in PRIORITIES:
            f.write(f"{priority.ljust(10)} : {priority_counts.get(priority, 0)}\n")

    print(f"Report generated at {REPORT_FILE}.")


def menu():
    print("========== Task Management System ==========")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Display All Tasks")
    print("5. Search by ID")
    print("6. Search by Title")
    print("7. Search by Status")
    print("8. Filter Pending Tasks")
    print("9. Filter Completed Tasks")
    print("10. Filter High Priority Tasks")
    print("11. Sort by Due Date")
    print("12. Sort by Priority")
    print("13. Sort by Title")
    print("14. Backup Tasks")
    print("15. Export CSV")
    print("16. Generate Report")
    print("17. Exit")
    print("==============================================")


def main():
    load_tasks()

    actions = {
        "1": add_task,
        "2": update_task,
        "3": delete_task,
        "4": display_tasks,
        "5": search_by_id,
        "6": search_by_title,
        "7": search_by_status,
        "8": filter_pending,
        "9": filter_completed,
        "10": filter_high_priority,
        "11": sort_by_due_date,
        "12": sort_by_priority,
        "13": sort_by_title,
        "14": backup_tasks,
        "15": export_csv,
        "16": generate_report,
    }

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "17":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action()


if __name__ == "__main__":
    main()
