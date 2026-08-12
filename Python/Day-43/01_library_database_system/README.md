# Library Database System

A command-line library database system built as a multi-module Python
package, demonstrating SQLite persistence across three related tables
(with real foreign keys), JOINs, and validation - the same modular
architecture used in recent projects (`database.py` / model / manager /
`main.py`), extended to a schema with multiple linked tables instead of
one.

## Project Structure

```
01_library_database_system/
├── database.py          # Database - connection + automatic table creation (foreign keys ON)
├── book.py               # Book dataclass (to_row/from_row for SQLite rows)
├── member.py              # Member dataclass (to_row/from_row for SQLite rows)
├── library_manager.py      # LibraryManager - validated book/member/borrowing operations
├── main.py                  # CLI entry point
├── library.db                # SQLite data file (created automatically on first run)
└── README.md
```

## Database Design

**Books** - `book_id` (PK), `title`, `author`, `category`, `available_copies`
(`CHECK (available_copies >= 0)`).

**Members** - `member_id` (PK), `name`, `email` (`UNIQUE`).

**BorrowedBooks** - `borrow_id` (PK, autoincrement), `member_id` (FK ->
Members), `book_id` (FK -> Books), `borrow_date` (defaults to
`CURRENT_DATE`), `return_date` (NULL while the book is still out).

Books and Members are each one-to-many with BorrowedBooks: one member can
have many borrow records over time, and one book can be borrowed many
times by many members (once each copy is returned, it's available again).

## Features

- Create the database and all three tables automatically on startup
- **Books** - Add, Update, Delete, Search (by ID/title/author/category),
  Display
- **Members** - Add, Update, Delete, Display
- **Borrowing** - Borrow Book, Return Book, Show Borrowed Books (active
  only, via `INNER JOIN`), Show Books Borrowed by a Member (all history,
  via `LEFT JOIN` so a member with no borrows still shows up)

## Validation

- Book/Member IDs must be unique (`DuplicateBookIDError`,
  `DuplicateMemberIDError`)
- Titles, authors, categories, and names cannot be empty
  (`InvalidTitleError`, `InvalidAuthorError`, `InvalidCategoryError`,
  `InvalidNameError`)
- Available copies must be a non-negative integer (`InvalidCopiesError`,
  also enforced at the schema level with `CHECK (available_copies >= 0)`)
- Email must contain `@` and a `.` in the domain part
  (`InvalidEmailError`) and must be unique across members
  (`DuplicateEmailError`)
- Borrowing requires both the member and book to exist
  (`MemberNotFoundError`, `BookNotFoundError`) and the book to have at
  least one available copy (`BookUnavailableError`)
- Returning requires an active (unreturned) borrow record for that
  member/book pair (`BorrowRecordNotFoundError`)
- Deleting a book or member that still has borrow records referencing it
  is refused (`BookHasActiveRecordsError`, `MemberHasActiveRecordsError`)
  - the database's own foreign key constraint is what catches this

All custom exceptions derive from a common `LibraryError` base (defined
in `library_manager.py`), so the CLI can catch a single exception type
for user-facing error messages.

## SQL Concepts Used

- **Foreign Keys** - `borrowed_books.member_id` and `borrowed_books.book_id`
  reference `members` and `books`; enforced via `PRAGMA foreign_keys = ON`
  on every connection
- **INNER JOIN** - `show_borrowed_books()` joins all three tables to list
  only currently-active borrows with the member's name and book's title
- **LEFT JOIN** - `show_books_borrowed_by_member()` joins from a single
  member outward so the member still appears even with zero borrow
  history
- **ORDER BY** - books/members/borrow records are always returned in a
  stable, readable order

## SQL Safety

Every query in `library_manager.py` uses `?` placeholders for values -
never f-strings or string concatenation - so no user input can alter a
query's structure (SQL injection).

## Usage

```bash
cd 01_library_database_system
python main.py
```

Follow the on-screen menu to manage books, manage members, and borrow or
return books. `library.db` is created automatically the first time the
program runs.
