1. When would you use a function instead of writing code directly? Give one real-world example.
    - We would use a function whenever we need to execute the same block of code multiple times to prevent writing the same thing again and again. Real-World Example: Uber/Ride-Booking Fare Calculation

2. Which data structure would you choose for each?

* Shopping cart
* Phone contacts
* Unique usernames
* GPS coordinates

Explain why.
    - Shopping Cart: Array / List Structure: A sequential list of ordered items.Why: You need to maintain the specific order in which items were added. Shopping carts also frequently require duplicate items (e.g., buying two identical shirts), which lists support naturally.
    Phone Contacts: Dictionary / Map / Hash Table Structure: Key-value pairs matching a unique identifier to data.Why: This structure allows for instant lookups. You can use the contact's name as the unique key to immediately retrieve their phone number and email as the value, without scanning the whole list alphabetically.
    Unique Usernames: Set Structure: A collection of distinct elements with no duplicates.Why: Sets automatically prevent duplicate entries. When a new user registers, a set can instantly check if the username already exists, ensuring every single username remains completely unique.
    GPS Coordinates: Tuple / Object Structure: A fixed, immutable grouping of related values.Why: A GPS point requires exactly two connected values: a latitude and a longitude. Using a tuple ensures these numbers stay locked together as a single reference point that cannot be accidentally separated or altered.

3. When should you use:

* List
* Tuple
* Set
* Dictionary
    - List: Use when you need an ordered collection of items that can be changed, reordered, or contain duplicates.
    Tuple: Use for fixed, unchangeable groups of related data that must always stay locked together.
    Set: Use when you need to guarantee all items are completely unique and want to instantly filter out duplicates.
    Dictionary: Use when you want to look up data instantly using a specific custom label instead of a number position.

4. Explain the difference between:

* Module
* Function
* File
    - Module - Inbuilt collections in python that have a set of function that can be used by importing the module.
    Function - Used when we need to execute the same block of code multiple times instead of writing the same thing again and again.
    File - Used to store the data so that it can be permanently kept in your system.

5. Why is File Handling important for CLI applications? Give one example.
    - File handling is important for CLI applications because it allows them to persist data between runs, process large files that cannot fit into standard command inputs, and automate file-system tasks like logging or backups.
    Real-World Example: A CLI Log Analyzer

6. What is the difference between print() and return? When should each be used?
    - A return statement is used at the end of a function and it returns a particular value to the statement that called the function.
    A print statement just prints whatever is passed inside the parentheses.