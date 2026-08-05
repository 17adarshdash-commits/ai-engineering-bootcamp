import os

from exceptions import LibraryError
from library import Library

DATA_FILE = os.path.join(os.path.dirname(__file__), "library_data.json")

MENU = """
1. Add Book
2. Update Book
3. Delete Book
4. Search Book
5. Borrow Book
6. Return Book
7. Display Books
8. Save Library
9. Load Library
0. Exit
"""


def main():
    library = Library()

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                book_id = input("Book ID: ").strip()
                title = input("Title: ").strip()
                author = input("Author: ").strip()
                library.add_book(book_id, title, author)
                print("Book added.")

            elif choice == "2":
                book_id = input("Book ID: ").strip()
                title = input("New title (blank to skip): ").strip() or None
                author = input("New author (blank to skip): ").strip() or None
                library.update_book(book_id, title=title, author=author)
                print("Book updated.")

            elif choice == "3":
                book_id = input("Book ID: ").strip()
                library.delete_book(book_id)
                print("Book deleted.")

            elif choice == "4":
                keyword = input("Search keyword: ").strip()
                results = library.search_book(keyword)
                if results:
                    for book in results:
                        print(book)
                else:
                    print("No matches found.")

            elif choice == "5":
                book_id = input("Book ID: ").strip()
                library.borrow_book(book_id)
                print("Book borrowed.")

            elif choice == "6":
                book_id = input("Book ID: ").strip()
                library.return_book(book_id)
                print("Book returned.")

            elif choice == "7":
                library.display_books()

            elif choice == "8":
                library.save_json(DATA_FILE)
                print(f"Library saved to {DATA_FILE}")

            elif choice == "9":
                library.load_json(DATA_FILE)
                print(f"Library loaded from {DATA_FILE}")

            elif choice == "0":
                print("Goodbye.")
                break

            else:
                print("Invalid option.")

        except LibraryError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
