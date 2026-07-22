1. What is configuration? Why should values like filenames, tax rates, or application settings be stored as constants instead of hardcoded throughout the program?
    - Configuration refers to the external variables and settings that define an application's behavior without altering its core code. Storing values like filenames, tax rates, or application settings as constants prevents bugs and allows you to update them instantly across the entire program from a single, centralized location.

2. What is data integrity? How do validation and unique identifiers help maintain correct data?
    - Data integrity is the assurance that data remains accurate, complete, and reliable throughout its entire lifecycle. Validation prevents incorrect or corrupted data from entering the system, while unique identifiers ensure that each record can be distinctively tracked and updated without altering other information.

3. Explain the difference between:
Constant
Variable
Configuration
Give one example of each.
    - A constant is an unchangeable value defined inside the code (e.g., const PI = 3.14), a variable is a mutable storage location for data that changes during execution (e.g., let userScore = 0), and configuration is an external setting used to adjust app behavior without changing code (e.g., DATABASE_URL in a .env file).

4. Why should applications avoid global variables whenever possible? What are the benefits of passing data through function parameters instead?
    - Applications should avoid global variables because they create hidden dependencies, make code difficult to debug, and risk accidental overwrites from different parts of the program. Passing data through function parameters instead ensures that functions are predictable, easier to test individually, and fully self-contained.

5. Explain the Open/Closed Principle (OCP). Why is it useful when software grows larger?
    - The Open/Closed Principle states that software entities should be open for extension but closed for modification, meaning you can add new functionality without changing existing, tested code. This principle is incredibly useful as software grows because it prevents new features from introducing bugs into working systems and significantly lowers maintenance costs.