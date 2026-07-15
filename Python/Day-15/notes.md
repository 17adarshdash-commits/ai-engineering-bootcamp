1. Why is file handling important for CLI applications? Give two real-world examples.
    - File handling is critical for CLI applications because it allows them to permanently save user configurations, automate bulk data processing, and handle inputs too large to fit into runtime memory.
    Real World Examples:
    Git CLI: Reads and writes .gitconfig files to permanently save user identities and repository settings across system reboots.
    Log Parsers (like Grep): Opens and scans massive server log files to extract error patterns without overloading the computer's memory.

2. Explain the difference between:

* Temporary data (variables)
* Persistent data (files)
    - The main difference is lifespan: temporary data disappears the moment the program stops running, while persistent data remains saved on the computer's storage drive permanently.

3. Why is with open() considered safer than open()?
    - The with open() statement is safer because it guarantees the file closes automatically, preventing memory leaks, data corruption, and file locking bugs.

4. When would you use each mode?

* r
* w
* a

Give one practical example for each.
    - r (Read): Use this mode to view or extract data from an existing file without modifying it, such as reading an application's settings.json file to load user preferences.
    w (Write): Use this mode to create a new file or completely overwrite an existing one with fresh content, such as exporting a brand-new invoice.pdf at checkout.
    a (Append): Use this mode to add new data onto the very end of an existing file without erasing its history, such as recording timestamped security alerts to a system.log file.

5. Suppose you’re building a simple Expense Tracker.

Which file mode would be used when:

* Reading previous expenses?
* Adding a new expense?
* Creating a new expense file?

Explain why.
    - Reading Previous Expenses: r (Read Mode)Why: This mode securely opens an existing file as read-only, ensuring you can display past transactions on the screen without accidentally modifying, corrupting, or deleting them.
    Adding a New Expense: a (Append Mode)Why: This mode targets the very end of your existing file to insert a new transaction, preserving all your historical financial entries instead of wiping them out.
    Creating a New Expense File: w (Write Mode)Why: The w mode instantly generates a blank, clean file from scratch for a new user.