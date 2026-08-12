1. SQL Constraints
Learn:
PRIMARY KEY
FOREIGN KEY
UNIQUE
NOT NULL
CHECK
DEFAULT
Understand why constraints maintain data integrity.
    - A constraint is a rule attached to a column (or table) that SQLite enforces on every write, rejecting any `INSERT`/`UPDATE` that would violate it - constraints move validation from "the application remembers to check" to "the database refuses to store bad data," which matters because every path that writes to the table (a bug, a script, a future feature) is protected, not just the one path someone remembered to guard. `PRIMARY KEY` marks the column that uniquely identifies each row - SQLite rejects a duplicate or NULL primary key, and it's what other tables reference to link rows together. `FOREIGN KEY` declares that a column's value must match an existing primary key in another table (e.g. `BorrowedBooks.member_id` must reference a real `Members.member_id`) - it prevents "orphan" rows that point at a member or book that doesn't exist; SQLite only enforces this when `PRAGMA foreign_keys = ON` is set, since it defaults off for backward compatibility. `UNIQUE` forces every value in a column to be distinct without making it the primary key - e.g. a member's email should be unique even though `member_id` is the primary key. `NOT NULL` rejects a row where that column is left unset - e.g. a book's title can never be blank/missing. `CHECK` enforces an arbitrary boolean condition on a column's value, e.g. `CHECK (available_copies >= 0)` rejects a copy count going negative. `DEFAULT` supplies a value automatically when an `INSERT` omits that column, e.g. `DEFAULT CURRENT_DATE` for a borrow date. Together these constraints maintain data integrity: they guarantee the schema's assumptions (every book has a title, every borrowed book points at a real member and a real book, copy counts never go negative) hold for every row in the table, forever, regardless of what code writes to it.

2. Database Relationships
Study:
One-to-One
One-to-Many
Many-to-Many
Examples:
Student -> Courses
Customer -> Orders
Author -> Books
    - A relationship describes how rows in one table relate to rows in another, and it's expressed entirely through foreign keys - there's no separate "relationship" construct in SQL. One-to-One means a row in table A matches at most one row in table B, and vice versa - e.g. a person and their passport; rare in practice, usually modeled by putting the foreign key in either table with a `UNIQUE` constraint on it. One-to-Many means one row in table A can be referenced by many rows in table B, but each row in B references only one row in A - e.g. a Customer can place many Orders, but each Order belongs to exactly one Customer; the foreign key lives on the "many" side (`Orders.customer_id` references `Customers.customer_id`). Many-to-Many means rows on both sides can relate to multiple rows on the other side - e.g. a Student can enroll in many Courses, and a Course can have many Students; this can't be expressed with a single foreign key on either table, so it requires a junction (join) table in between (e.g. `Enrollments` with `student_id` and `course_id`, each a foreign key) that holds one row per pairing. The library system's `BorrowedBooks` table is itself a one-to-many-and-one-to-many junction: one Member can have many BorrowedBooks rows, and one Book can also appear in many BorrowedBooks rows over time (once returned, it can be borrowed again).

3. Advanced SQL Queries
Learn:
ORDER BY
LIMIT
DISTINCT
WHERE
LIKE
IN
BETWEEN
    - `ORDER BY column [ASC|DESC]` sorts the result set by one or more columns - ascending is the default, `DESC` reverses it, and multiple columns (`ORDER BY course, name`) sort by the first, breaking ties with the second. `LIMIT n` caps the result set to at most `n` rows, commonly paired with `ORDER BY` to get "the top N" of something (e.g. the 5 highest CGPAs). `DISTINCT` removes duplicate rows from the result - `SELECT DISTINCT course FROM students` lists each course once no matter how many students take it. `WHERE condition` filters which rows are returned before any grouping/ordering happens - it's the general-purpose filter that `LIKE`, `IN`, and `BETWEEN` all plug into. `LIKE pattern` does pattern matching on text, where `%` matches any sequence of characters and `_` matches exactly one - `WHERE name LIKE 'A%'` finds every name starting with A. `IN (v1, v2, ...)` matches a column against a fixed list of values in one condition, equivalent to chaining several `OR column = v` comparisons but far more readable. `BETWEEN low AND high` matches a value within an inclusive range - `WHERE cgpa BETWEEN 8.0 AND 9.0` is shorthand for `cgpa >= 8.0 AND cgpa <= 9.0`.

4. Aggregate Functions
Understand:
COUNT()
SUM()
AVG()
MIN()
MAX()
Also learn:
GROUP BY
HAVING
    - Aggregate functions collapse many rows into a single summary value. `COUNT(*)` counts rows (or `COUNT(column)` counts non-NULL values in that column); `SUM(column)` totals a numeric column; `AVG(column)` averages it; `MIN(column)`/`MAX(column)` find the smallest/largest value. Used alone, an aggregate collapses the *entire* table into one row - `SELECT AVG(cgpa) FROM students` returns one overall average. `GROUP BY column` changes that: it partitions rows into buckets sharing the same value in that column, and the aggregate is then computed separately *per bucket* - `SELECT course, AVG(cgpa) FROM students GROUP BY course` returns one average CGPA per course instead of one overall average. `HAVING condition` filters *after* grouping, on the aggregated values themselves - e.g. `GROUP BY course HAVING AVG(cgpa) > 8.0` keeps only courses whose average CGPA exceeds 8.0. This is why `HAVING` exists separately from `WHERE`: `WHERE` filters individual rows *before* grouping and can't reference an aggregate (the aggregate doesn't exist yet at that point), while `HAVING` filters the grouped results *after* the aggregate has been computed.

5. SQL JOINs
Study:
INNER JOIN
LEFT JOIN
Understand when each is used.
    - A `JOIN` combines rows from two tables based on a matching condition, typically a foreign key matching a primary key. `INNER JOIN` returns only the rows that have a match in *both* tables - e.g. `SELECT * FROM Members INNER JOIN BorrowedBooks ON Members.member_id = BorrowedBooks.member_id` returns only members who have actually borrowed at least one book; a member with zero borrow records is silently excluded because there's nothing in `BorrowedBooks` to match against. `LEFT JOIN` (left outer join) returns *every* row from the left table regardless of whether a match exists, filling in `NULL` for the right table's columns when there's no match - the same query with `LEFT JOIN` instead would include every member, with `NULL` borrow columns for members who've never borrowed anything. The choice depends on the question being asked: use `INNER JOIN` when a row without a match is irrelevant to the result ("show me borrow records with their member names"), and use `LEFT JOIN` when the left table's rows all matter regardless of a match ("show me every member and what they've borrowed, including members who've borrowed nothing").

6. Best Practices
Normalize related data.
Avoid duplicate information.
Always use parameterized queries.
Close database connections.
Create indexes only when needed (introduction).
    - Normalize related data: each fact should live in exactly one place - a book's title lives only in `Books`, never copy-pasted into every `BorrowedBooks` row; `BorrowedBooks` stores a `book_id` foreign key and looks the title up via a join when needed. Avoid duplicate information for the same reason - duplication means an update (e.g. correcting a typo in a title) has to be repeated everywhere it was copied, and any place that's missed leaves the data inconsistent. Always use parameterized queries (`?` placeholders, never f-strings/concatenation) so user input is always treated as a data value, never as SQL syntax - this closes off SQL injection regardless of what the input contains. Always close database connections (via `try/finally` or a `with` block) so a connection isn't leaked if an exception interrupts an operation partway through. Create indexes only when needed: an index (`CREATE INDEX idx_name ON table(column)`) speeds up lookups/joins/filters on that column at the cost of extra disk space and slightly slower writes (the index itself must be updated on every insert/update/delete) - worth adding on columns queried or joined on frequently (like a foreign key column searched often), but adding one to every column "just in case" wastes space and slows writes for no benefit on a small dataset.
