import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library.txt")


def load_books():
    books = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                title, author, status = [part.strip() for part in line.split(",")]
                books[title] = {"author": author, "status": status}
    except FileNotFoundError:
        pass
    return books


def save_books():
    with open(DATA_FILE, "w") as file:
        for title, info in books.items():
            file.write(f"{title}, {info['author']}, {info['status']}\n")


books = load_books()


def add_book():
    title = input("Enter Title: ")
    if title in books:
        print("Book already exists.")
        return

    author = input("Enter Author: ")
    books[title] = {"author": author, "status": "Available"}
    save_books()
    print("Book added successfully.")


def view_books():
    if not books:
        print("Library is empty.\n")
        return
    for title, info in books.items():
        print(f"Title: {title}\nAuthor: {info['author']}\nStatus: {info['status']}")
        print("-----------------")


def borrow_book():
    title = input("Enter Title: ")
    if title not in books:
        print("Book not found.")
        return

    info = books[title]
    if info["status"] == "Borrowed":
        print("Book is already borrowed.")
        return

    info["status"] = "Borrowed"
    save_books()
    print("Book borrowed successfully.")


def return_book():
    title = input("Enter Title: ")
    if title not in books:
        print("Book not found.")
        return

    info = books[title]
    if info["status"] == "Available":
        print("Book was not borrowed.")
        return

    info["status"] = "Available"
    save_books()
    print("Book returned successfully.")


def search_book():
    title = input("Enter Title: ")
    if title in books:
        info = books[title]
        print(f"Title: {title}\nAuthor: {info['author']}\nStatus: {info['status']}")
    else:
        print("Book not found.")


while True:
    choice = input(
        "===== Library Manager =====\n"
        "1. Add Book\n"
        "2. View Books\n"
        "3. Borrow Book\n"
        "4. Return Book\n"
        "5. Search Book\n"
        "6. Exit\n\n"
        "Enter your choice: "
    )

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        print("Thank you for using Library Manager.")
        break
    else:
        print("Invalid Choice. Please pick 1-6.")

    print()
