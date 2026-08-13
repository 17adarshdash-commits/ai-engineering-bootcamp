1. Database Transactions
Learn:
What is a transaction?
Why transactions exist
ACID PropertiesAtomicity
Consistency
Isolation
Durability

commit()
rollback()
Understand why transactions prevent partially completed operations.
    - A transaction is a group of one or more SQL statements executed as a single, indivisible unit of work - either every statement in the group succeeds and is saved, or none of them are. SQLite starts an implicit transaction the moment a write statement runs, and it stays open until `commit()` (make every change in the group permanent) or `rollback()` (discard every change in the group as if none of it happened) is called. Transactions exist because real operations are often made of several dependent steps (e.g. transferring money means withdrawing from one account and depositing into another), and if the program crashes, an error is raised, or a constraint is violated partway through, an operation that isn't wrapped in a transaction can leave the database in a state where the withdrawal happened but the deposit didn't - money that simply vanished. ACID names the four guarantees a transaction provides: **Atomicity** - the group of statements is all-or-nothing, matching the "single indivisible unit" definition above. **Consistency** - a transaction can only move the database from one valid state to another valid state, never violating a constraint (`CHECK`, `FOREIGN KEY`, `NOT NULL`) partway through and leaving it there. **Isolation** - concurrently running transactions don't see each other's uncommitted, in-progress changes, so one transaction can't read half-finished work from another. **Durability** - once `commit()` returns, the change is permanently saved (written to disk), and survives even a crash immediately afterward. `commit()` and `rollback()` are the two ways a transaction ends: `commit()` is called after every step in the group has succeeded, writing all the changes permanently; `rollback()` is called (typically from an `except` block) the moment any step fails, undoing every change made since the transaction began - which is exactly why transactions prevent partially completed operations: the failure of one step is caught before `commit()` is ever reached, so `rollback()` restores the database to exactly the state it was in before the operation started, with no partial write left behind.

2. Database Normalization
Study:
What is normalization?
First Normal Form (1NF)
Second Normal Form (2NF)
Third Normal Form (3NF)
Understand:
Removing duplicate data
Splitting related information into tables
Why normalization improves maintainability
    - Normalization is the process of organizing a database's tables and columns to reduce redundancy and eliminate data anomalies (insert/update/delete anomalies caused by the same fact being stored in more than one place). It's applied as a series of increasingly strict rules called "normal forms." **First Normal Form (1NF)** requires every column to hold a single, atomic value - no repeating groups and no comma-separated lists crammed into one cell (e.g. a `Students` table with `Course1`, `Course2`, `Course3` columns violates 1NF, because "which courses does this student take" is really a multi-valued fact being forced into a fixed number of columns instead of one row per fact). **Second Normal Form (2NF)** requires 1NF, plus every non-key column must depend on the *whole* primary key, not just part of it - this only matters for tables with a composite (multi-column) primary key; a column that depends on only one part of that key belongs in a separate table keyed by that part alone. **Third Normal Form (3NF)** requires 2NF, plus no non-key column may depend on another non-key column (no "transitive" dependencies) - e.g. if a `course_name` in an enrollment table is really determined by a `course_id` in that same row rather than by the row's own primary key, it belongs in a separate `Courses` table instead. In practice, applying these rules means removing duplicate data (a course's name is stored once, in a `Courses` table, instead of being repeated in every row that references it) and splitting related information into separate tables linked by foreign keys (`Students`, `Courses`, and a junction table `Enrollments` instead of one wide `Students` table with a fixed number of course columns). This improves maintainability because every fact lives in exactly one place: renaming a course means updating one row in `Courses`, not hunting down every student row that happens to mention it, and it removes structural limits like "a student can take at most 3 courses" that a fixed-column design silently imposes.

3. Indexes
Learn:
What is an index?
Why indexes improve performance
CREATE INDEX
When not to use indexes
Understand the trade-off between faster reads and slower writes.
    - An index is a separate, sorted data structure that SQLite maintains alongside a table, mapping a column's values to the rows that contain them - conceptually similar to a book's index, which lets you jump straight to a page instead of reading the whole book to find a topic. Without an index, looking up rows by a column's value requires a full table scan (checking every row one by one); with an index on that column, SQLite can instead do a fast lookup (roughly O(log n) instead of O(n)) directly to the matching rows. This is why indexes improve performance dramatically for lookups, `WHERE` filters, and `JOIN` conditions on large tables - the gain scales with table size, so it's negligible on a table with a handful of rows and significant on one with hundreds of thousands. An index is created with `CREATE INDEX idx_student_name ON Students(name)` - this doesn't change any query's SQL, it just gives SQLite's query planner the option to use the index automatically whenever it decides that's faster than a full scan. The trade-off is that an index isn't free: it takes extra disk space, and every `INSERT`/`UPDATE`/`DELETE` on that table now has to also update the index (or indexes) on top of the table itself, which makes writes slower. Indexes are *not* worth adding on columns that are rarely searched/filtered/joined on, on small tables where a full scan is already fast, or on columns that change very frequently (since every change re-updates the index) - adding an index "just in case" on every column trades write performance for a read benefit that may never materialize.

4. Advanced SQL JOINs
Study:
CROSS JOIN
SELF JOIN
Review:
INNER JOIN
LEFT JOIN
Understand when each join is appropriate.
    - `CROSS JOIN` produces the Cartesian product of two tables - every row from the first table paired with every row from the second table, with no matching condition at all. If table A has 3 rows and table B has 4 rows, `A CROSS JOIN B` produces 12 rows. It's appropriate when every possible combination genuinely needs to be generated (e.g. every product paired with every size to build a catalog of variants) - it's rarely used for combining related data, since an unrelated pairing usually isn't meaningful. `SELF JOIN` isn't a distinct SQL keyword - it's an ordinary `JOIN` where a table is joined to itself, using two different aliases to treat it as if it were two separate tables. This is appropriate when rows in a table reference other rows in that *same* table, most commonly an "employees and managers" relationship: `SELECT e.name AS employee, m.name AS manager FROM employees e JOIN employees m ON e.manager_id = m.employee_id` treats one aliased copy (`e`) as the employee side and the other (`m`) as the manager side of the same underlying table. Reviewing the earlier joins: `INNER JOIN` returns only rows with a match in both tables (a row without a match is silently excluded), and `LEFT JOIN` returns every row from the left table regardless of a match, filling unmatched right-side columns with `NULL`. Choosing the right join comes down to what relationship is being expressed: `INNER JOIN`/`LEFT JOIN` for two genuinely related tables where the question is "matched" vs. "all of the left table anyway"; `SELF JOIN` for a table that references itself; `CROSS JOIN` for generating every combination of two independent sets.

5. Best Practices
Use transactions for multi-step updates.
Normalize before optimizing.
Index frequently searched columns.
Keep business logic outside SQL.
Continue using parameterized queries.
    - Use transactions for multi-step updates: any operation made of more than one write that must succeed or fail together (a money transfer, borrowing a book while decrementing its stock) belongs inside a transaction, so a failure partway through never leaves the database half-updated. Normalize before optimizing: get the table structure right first (one fact in one place, related data split across linked tables) before reaching for performance tools like indexes - optimizing a poorly normalized schema just makes the redundant, error-prone version of the schema faster, it doesn't fix the underlying design problem. Index frequently searched columns: add `CREATE INDEX` to columns that are actually filtered, searched, or joined on often (like a foreign key column or a name column used in lookups), not defensively on every column. Keep business logic outside SQL: validation rules (a price must be positive, an email must look valid, a quantity can't go negative) belong in the application/manager layer in Python, not buried in triggers or ad hoc SQL, so the rules are visible, testable, and easy to change in one place - SQL-level constraints (`CHECK`, `NOT NULL`, `FOREIGN KEY`) are still worth keeping as a last line of defense, but the primary validation and its error messages live in Python. Continue using parameterized queries: every value that comes from outside the program (user input, external data) is passed via `?` placeholders, never with f-strings or string concatenation, so it's always treated as data and never as SQL syntax - closing off SQL injection regardless of what the value contains.
</content>
