import os
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "library_data.txt")
REPORT_FILE = os.path.join(BASE_DIR, "library_report.txt")


def load_books():
    books = []
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                book_id, title, author, category, available, date_added = [
                    part.strip() for part in line.split(",")
                ]
                books.append({
                    "book_id": book_id,
                    "title": title,
                    "author": author,
                    "category": category,
                    "available": available == "True",
                    "date_added": date_added,
                })
    except FileNotFoundError:
        pass
    return books


def save_books():
    with open(DATA_FILE, "w") as file:
        for book in books:
            file.write(
                f"{book['book_id']}, {book['title']}, {book['author']}, "
                f"{book['category']}, {book['available']}, {book['date_added']}\n"
            )


books = load_books()


def find_book_by_id(book_id):
    for book in books:
        if book["book_id"] == book_id:
            return book
    return None


def add_book():
    book_id = input("Book ID: ").strip()
    if not book_id:
        print("Book ID cannot be empty.")
        return
    if find_book_by_id(book_id):
        print("Book ID already exists.")
        return

    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    author = input("Author: ").strip()
    if not author:
        print("Author cannot be empty.")
        return

    category = input("Category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "available": True,
        "date_added": date.today().isoformat(),
    })
    save_books()
    print("Book added successfully.")


def print_book_row(book):
    print(f"ID: {book['book_id']}")
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Category: {book['category']}")
    print(f"Available: {book['available']}")
    print(f"Date Added: {book['date_added']}")
    print("-----------------")


def view_books():
    if not books:
        print("Library is empty.")
        return
    for book in books:
        print_book_row(book)


def search_book():
    query = input("Search by (1) Book ID or (2) Title: ").strip()

    if query == "1":
        book_id = input("Enter Book ID: ").strip()
        book = find_book_by_id(book_id)
        if book:
            print_book_row(book)
        else:
            print("Book not found.")
    elif query == "2":
        term = input("Enter Title (partial match allowed): ").strip().lower()
        results = [book for book in books if term in book["title"].lower()]
        if results:
            for book in results:
                print_book_row(book)
        else:
            print("No matching books found.")
    else:
        print("Invalid choice.")


def borrow_book():
    book_id = input("Enter Book ID: ").strip()
    book = find_book_by_id(book_id)
    if not book:
        print("Book not found.")
        return

    if not book["available"]:
        print("Book already borrowed.")
        return

    book["available"] = False
    save_books()
    print("Book borrowed successfully.")


def return_book():
    book_id = input("Enter Book ID: ").strip()
    book = find_book_by_id(book_id)
    if not book:
        print("Book not found.")
        return

    if book["available"]:
        print("Book is already available.")
        return

    book["available"] = True
    save_books()
    print("Book returned successfully.")


def delete_book():
    book_id = input("Enter Book ID: ").strip()
    book = find_book_by_id(book_id)
    if not book:
        print("Book not found.")
        return

    books.remove(book)
    save_books()
    print("Book deleted successfully.")


def generate_report():
    total_books = len(books)
    borrowed_books = sum(1 for book in books if not book["available"])
    available_books = total_books - borrowed_books

    categories = {}
    for book in books:
        categories[book["category"]] = categories.get(book["category"], 0) + 1

    with open(REPORT_FILE, "w") as file:
        file.write("========== LIBRARY REPORT ==========\n")
        file.write(f"Generated On: {date.today().isoformat()}\n")
        file.write(f"Total Books: {total_books}\n")
        file.write(f"Borrowed Books: {borrowed_books}\n")
        file.write(f"Available Books: {available_books}\n\n")

        file.write("Books Per Category:\n")
        for category, count in categories.items():
            file.write(f"  {category} : {count}\n")

        file.write("\n--------------------------------\n")
        file.write("Complete Catalogue\n\n")
        for book in books:
            file.write(f"ID: {book['book_id']}\n")
            file.write(f"Title: {book['title']}\n")
            file.write(f"Author: {book['author']}\n")
            file.write(f"Category: {book['category']}\n")
            file.write(f"Available: {book['available']}\n")
            file.write(f"Date Added: {book['date_added']}\n")
            file.write("-----------------\n")

    print(f"Report generated: {REPORT_FILE}")


while True:
    choice = input(
        "\n===== Library Manager =====\n"
        "1. Add Book\n"
        "2. View Books\n"
        "3. Search Book\n"
        "4. Borrow Book\n"
        "5. Return Book\n"
        "6. Delete Book\n"
        "7. Generate Report\n"
        "8. Exit\n\n"
        "Enter your choice: "
    )

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        generate_report()
    elif choice == "8":
        print("Thank you for using Library Manager.")
        break
    else:
        print("Invalid Choice. Please pick 1-8.")
