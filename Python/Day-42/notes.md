1. Databases
Learn:
What is a database?
Why databases exist
Relational vs Non-relational databases
Tables
Rows
Columns
Primary Key
    - A database is an organized, persistent collection of data that can be reliably stored, queried, and updated without loading the whole dataset into memory or hand-parsing a file. Databases exist because plain files (JSON, CSV, text) don't scale: they have no built-in way to enforce structure, query efficiently, handle concurrent access, or guarantee that a write either fully happens or doesn't happen at all (a crash mid-write can leave a JSON file corrupted). A relational database organizes data into tables with a fixed schema and relationships between tables (via keys), and is queried with SQL - it enforces structure up front, which is ideal when the data is naturally tabular and consistency matters (e.g. a students table where every row must have a name and age). A non-relational (NoSQL) database - document stores like MongoDB, key-value stores like Redis - stores data with a flexible or absent schema, which trades some consistency guarantees for flexibility and horizontal scalability; it suits data that doesn't fit neatly into rows/columns or whose shape varies from record to record. A table is a named collection of records sharing the same structure (e.g. `Students`). A row (record) is one entry in a table - one student. A column (field) is one named attribute every row has - `name`, `age`, `course`. A primary key is a column (or set of columns) whose value uniquely identifies each row - no two rows can share one, and it's what other tables reference to establish relationships; `id` is the conventional primary key for a `Students` table.

2. SQLite
Understand:
What is SQLite?
Why SQLite is useful
Creating a database
Connecting to a database
Closing a connection
import sqlite3
    - SQLite is a lightweight, serverless, file-based relational database engine - the entire database (schema, tables, rows, indexes) lives in a single `.db` file on disk, and there's no separate database server process to install, configure, or keep running. It's useful for exactly this reason: zero setup, the whole engine ships built into Python's standard library (`import sqlite3`, no `pip install` needed), and a `.db` file can be copied, moved, or version-controlled like any other file - ideal for small-to-medium applications, prototypes, and learning SQL without the overhead of a client-server database like PostgreSQL or MySQL. `sqlite3.connect("students.db")` both creates the database file (if it doesn't exist yet) and opens a connection to it - creating and connecting are the same call. That connection object is used to obtain a cursor (`conn.cursor()`), which is what actually executes SQL statements and fetches results. A connection must be closed with `conn.close()` when done, releasing the file lock and flushing any pending state - leaving it open leaks resources and, in a long-running program, can eventually exhaust available file handles or block other connections from writing.

3. SQL Basics
Study:
CREATE TABLE
INSERT
SELECT
UPDATE
DELETE
Understand what each command does.
    - `CREATE TABLE` defines a new table's structure - its name and the name/type/constraints of every column, e.g. `CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)`. It runs once; running it again on an existing table raises an error unless guarded with `IF NOT EXISTS`. `INSERT INTO table (columns) VALUES (values)` adds a new row. `SELECT columns FROM table WHERE condition` reads rows back - `SELECT *` reads every column, and `WHERE` filters which rows come back (omitting it returns all rows). `UPDATE table SET column = value WHERE condition` modifies existing rows in place - critically, without a `WHERE` clause it updates every row in the table, so the condition is what scopes the change to the intended row(s). `DELETE FROM table WHERE condition` removes rows - same danger: no `WHERE` clause deletes the entire table's contents. After any `INSERT`, `UPDATE`, or `DELETE`, the change must be persisted with `conn.commit()` - until then it exists only in the current transaction and is lost if the connection closes without committing.

4. Parameterized Queries
Learn:
Why never write:
cursor.execute(
    f"SELECT * FROM students WHERE name='{name}'"
)
Instead use:
cursor.execute(
    "SELECT * FROM students WHERE name=?",
    (name,)
)
Understand SQL Injection at a high level.
    - Building a SQL string by directly interpolating a variable (f-string, `%`, `.format()`, string concatenation) means whatever that variable contains becomes literal SQL. If `name` comes from user input and someone enters `' OR '1'='1`, the query becomes `SELECT * FROM students WHERE name='' OR '1'='1'` - a condition that's always true, so it returns every row instead of matching a name. Worse, a name like `x'; DROP TABLE students; --` can inject an entirely separate destructive statement. This class of attack is SQL injection: user-controlled input is allowed to change the *structure* of a query rather than just supplying a *value* within it. The fix is a parameterized query: `cursor.execute("SELECT * FROM students WHERE name=?", (name,))` passes `name` as a bound parameter rather than splicing it into the SQL string - the database driver treats it strictly as a data value, never as SQL syntax, so no input can alter the query's structure no matter what characters it contains. The `?` placeholder (SQLite's paramstyle) marks where a value goes, and the tuple passed as the second argument to `execute()` supplies the values in order - one placeholder per tuple element.

5. Best Practices
Always close database connections.
Commit after changes.
Use parameterized queries.
Keep database logic separate from UI.
Don't duplicate SQL statements.
    - Always close a connection when done (`conn.close()`), ideally via a `try/finally` or a `with` block, so a connection isn't leaked if an exception is raised mid-operation. Always `conn.commit()` after an `INSERT`/`UPDATE`/`DELETE` - reads (`SELECT`) don't need it, but any write that isn't committed is invisible to other connections and can be lost. Always use `?` placeholders for any value that comes from outside the literal SQL string, even values that "seem safe" - it costs nothing and closes off SQL injection entirely. Keep database logic (connecting, executing SQL, committing) in its own module (e.g. `database.py`) separate from the UI/CLI layer that just calls functions like `add_student(...)` - this mirrors the manager/CLI split used in earlier projects, and means the database code can be tested, reused, or swapped (e.g. for a different database) without touching the CLI. Avoid writing the same SQL statement in multiple places - one function per operation (`create_student`, `read_students`, `update_student`, `delete_student`) means a schema change only needs updating in one place instead of hunting down every copy-pasted query.
