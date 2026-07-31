import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "books.txt")

books = []


def load_books():
    if not os.path.exists(DATA_FILE):
        return

    with open(DATA_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            book_id, title, author, available = line.split("|")
            books.append({
                "id": int(book_id),
                "title": title,
                "author": author,
                "available": available == "True"
            })


def save_books():
    with open(DATA_FILE, "w") as f:
        for book in books:
            f.write(f"{book['id']}|{book['title']}|{book['author']}|{book['available']}\n")

    print("Books saved successfully.")


def find_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def add_book():
    id_input = input("Enter Book ID: ").strip()
    if not id_input.isdigit():
        print("Invalid Book ID.")
        return

    book_id = int(id_input)
    if find_book_by_id(book_id):
        print("Duplicate Book ID.")
        return

    title = input("Enter Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    author = input("Enter Author: ").strip()
    if not author:
        print("Author cannot be empty.")
        return

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    })
    print("Book added successfully.")


def remove_book():
    id_input = input("Enter Book ID: ").strip()
    if not id_input.isdigit():
        print("Invalid Book ID.")
        return

    book = find_book_by_id(int(id_input))
    if not book:
        print("Book not found.")
        return

    books.remove(book)
    print("Book removed successfully.")


def borrow_book():
    id_input = input("Enter Book ID: ").strip()
    if not id_input.isdigit():
        print("Invalid Book ID.")
        return

    book = find_book_by_id(int(id_input))
    if not book:
        print("Book not found.")
        return

    if not book["available"]:
        print("Book is already borrowed.")
        return

    book["available"] = False
    print("Book borrowed successfully.")


def return_book():
    id_input = input("Enter Book ID: ").strip()
    if not id_input.isdigit():
        print("Invalid Book ID.")
        return

    book = find_book_by_id(int(id_input))
    if not book:
        print("Book not found.")
        return

    if book["available"]:
        print("Book is already available.")
        return

    book["available"] = True
    print("Book returned successfully.")


def search_title():
    title = input("Enter Title: ").strip().lower()
    for book in books:
        if book["title"].lower() == title:
            print(f"ID       : {book['id']}")
            print(f"Title    : {book['title']}")
            print(f"Author   : {book['author']}")
            print(f"Available: {'Yes' if book['available'] else 'No'}")
            return

    print("Book not found.")


def search_author():
    author = input("Enter Author: ").strip().lower()
    matches = [book for book in books if book["author"].lower() == author]

    if not matches:
        print("No books found for this author.")
        return

    for book in matches:
        print(f"ID       : {book['id']}")
        print(f"Title    : {book['title']}")
        print(f"Author   : {book['author']}")
        print(f"Available: {'Yes' if book['available'] else 'No'}")
        print("-" * 20)


def display_books():
    if not books:
        print("No books in the library.")
        return

    for book in books:
        print(f"ID       : {book['id']}")
        print(f"Title    : {book['title']}")
        print(f"Author   : {book['author']}")
        print(f"Available: {'Yes' if book['available'] else 'No'}")
        print("-" * 20)


def menu():
    print("\n========= Library =========")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search by Title")
    print("6. Search by Author")
    print("7. Display All Books")
    print("8. Save")
    print("9. Exit")


def main():
    load_books()

    actions = {
        "1": add_book,
        "2": remove_book,
        "3": borrow_book,
        "4": return_book,
        "5": search_title,
        "6": search_author,
        "7": display_books,
        "8": save_books,
    }

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "9":
            save_books()
            print("Goodbye!")
            break

        action = actions.get(choice)
        if not action:
            print("Invalid menu option.")
            continue

        action()


if __name__ == "__main__":
    main()
