"""
main.py

Command-line interface for the Library Database System.
"""

from database import Database
from library_manager import LibraryError, LibraryManager

MENU = """
================ Library Database System ================
 Books
  1. Add Book
  2. Update Book
  3. Delete Book
  4. Search Book
  5. Display Books
 Members
  6. Add Member
  7. Update Member
  8. Delete Member
  9. Display Members
 Borrowing
  10. Borrow Book
  11. Return Book
  12. Show Borrowed Books
  13. Show Books Borrowed by a Member
  14. Exit
============================================================
"""


# ------------------------------------------------------------------
# Books
# ------------------------------------------------------------------
def add_book(manager):
    book_id = input("Enter book ID: ").strip()
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    category = input("Enter category: ").strip()
    available_copies = input("Enter available copies: ").strip()

    try:
        manager.add_book(book_id, title, author, category, available_copies)
        print("Book added successfully.")
    except LibraryError as e:
        print(f"Error: {e}")


def update_book(manager):
    book_id = input("Enter book ID to update: ").strip()
    print("Leave a field blank to keep its current value.")
    title = input("New title: ").strip()
    author = input("New author: ").strip()
    category = input("New category: ").strip()
    available_copies = input("New available copies: ").strip()

    updates = {}
    if title:
        updates["title"] = title
    if author:
        updates["author"] = author
    if category:
        updates["category"] = category
    if available_copies:
        updates["available_copies"] = available_copies

    try:
        book = manager.update_book(book_id, **updates)
        print(f"Book updated: {book}")
    except LibraryError as e:
        print(f"Error: {e}")


def delete_book(manager):
    book_id = input("Enter book ID to delete: ").strip()
    try:
        manager.delete_book(book_id)
        print("Book deleted successfully.")
    except LibraryError as e:
        print(f"Error: {e}")


def search_book(manager):
    keyword = input("Enter search keyword (ID/title/author/category): ").strip()
    results = manager.search_book(keyword)
    if not results:
        print("No matching books found.")
        return
    for book in results:
        print(book)


def display_books(manager):
    books = manager.display_books()
    if not books:
        print("No books to display.")
        return
    for book in books:
        print(book)


# ------------------------------------------------------------------
# Members
# ------------------------------------------------------------------
def add_member(manager):
    member_id = input("Enter member ID: ").strip()
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()

    try:
        manager.add_member(member_id, name, email)
        print("Member added successfully.")
    except LibraryError as e:
        print(f"Error: {e}")


def update_member(manager):
    member_id = input("Enter member ID to update: ").strip()
    print("Leave a field blank to keep its current value.")
    name = input("New name: ").strip()
    email = input("New email: ").strip()

    updates = {}
    if name:
        updates["name"] = name
    if email:
        updates["email"] = email

    try:
        member = manager.update_member(member_id, **updates)
        print(f"Member updated: {member}")
    except LibraryError as e:
        print(f"Error: {e}")


def delete_member(manager):
    member_id = input("Enter member ID to delete: ").strip()
    try:
        manager.delete_member(member_id)
        print("Member deleted successfully.")
    except LibraryError as e:
        print(f"Error: {e}")


def display_members(manager):
    members = manager.display_members()
    if not members:
        print("No members to display.")
        return
    for member in members:
        print(member)


# ------------------------------------------------------------------
# Borrowing
# ------------------------------------------------------------------
def borrow_book(manager):
    member_id = input("Enter member ID: ").strip()
    book_id = input("Enter book ID: ").strip()
    try:
        manager.borrow_book(member_id, book_id)
        print("Book borrowed successfully.")
    except LibraryError as e:
        print(f"Error: {e}")


def return_book(manager):
    member_id = input("Enter member ID: ").strip()
    book_id = input("Enter book ID: ").strip()
    try:
        manager.return_book(member_id, book_id)
        print("Book returned successfully.")
    except LibraryError as e:
        print(f"Error: {e}")


def show_borrowed_books(manager):
    records = manager.show_borrowed_books()
    if not records:
        print("No books are currently borrowed.")
        return
    for borrow_id, member_name, title, borrow_date in records:
        print(f"Borrow ID: {borrow_id} | {member_name} borrowed '{title}' on {borrow_date}")


def show_books_borrowed_by_member(manager):
    member_id = input("Enter member ID: ").strip()
    try:
        records = manager.show_books_borrowed_by_member(member_id)
    except LibraryError as e:
        print(f"Error: {e}")
        return

    if not records or records[0][0] is None:
        print("This member has not borrowed any books.")
        return

    for title, borrow_date, return_date in records:
        status = f"returned on {return_date}" if return_date else "still borrowed"
        print(f"'{title}' | borrowed on {borrow_date} | {status}")


def main():
    database = Database()
    manager = LibraryManager(database)

    actions = {
        "1": add_book,
        "2": update_book,
        "3": delete_book,
        "4": search_book,
        "5": display_books,
        "6": add_member,
        "7": update_member,
        "8": delete_member,
        "9": display_members,
        "10": borrow_book,
        "11": return_book,
        "12": show_borrowed_books,
        "13": show_books_borrowed_by_member,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "14":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action(manager)


if __name__ == "__main__":
    main()
