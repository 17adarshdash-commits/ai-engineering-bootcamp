1. What is file persistence? Why is it important in real-world applications?
    - File persistence is the process of saving application data to non-volatile storage so it remains accessible after the program or system shuts down.It is important because it prevents data loss from crashes, maintains user sessions, and ensures long-term data reliability across application restarts.

2. Explain the difference between:
Variables
Files
Databases
When would you use each?
    - Variables store data temporarily in RAM and disappear when the program closes, making them perfect for quick calculations or active user interactions.
    Files store data permanently on a disk as unstructured text or binaries, which is ideal for simple logs, configurations, or media storage.
    Databases organize permanent data into structured tables or collections, enabling powerful searching, security, and concurrent access for complex application data.

3. What are the different Python file modes?
Explain:
r
w
a
x
When should each be used?
    - r: Opens an existing file for reading only and errors out if the file is missing. Use this mode when you only need to read data from a configuration or document.
    w: Overwrites an existing file or creates a new one to write data from scratch. Use this mode when saving a fresh document or completely replacing old system logs.
    a: Appends new data to the end of an existing file without deleting current content. Use this mode when continuously adding new timestamps or entries to a running log file.
    x: Creates a new file exclusively for writing and fails if the file already exists. Use this mode to prevent accidental data loss when generating unique transaction receipts or user accounts.

4. Why should file operations be separated into functions? How does that improve maintainability?
    - Separating operations: Moving file operations into functions isolates tricky storage logic from your main business logic to keep the code organized.
    Improving maintainability: This separation improves maintainability by allowing you to fix bugs or change storage formats in a single function without breaking the rest of your application.

5. Your Expense Tracker currently stores data in memory. How will adding file persistence improve the user experience?
    - User Experience Improvement: Adding file persistence prevents users from losing their budget data every time they close the app, allowing them to track long-term spending patterns effortlessly.