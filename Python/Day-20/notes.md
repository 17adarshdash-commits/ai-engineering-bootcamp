1. What is input validation? Why is it important even if users are expected to enter correct data?
    - System validation prevents application crashes, malicious cyberattacks, and database corruption caused by inevitable human typos or automated bot exploits.

2. What is refactoring? How is refactoring different from adding new features?
    - Refactoring is the process of improving existing code structure without changing its external behavior.
    Refactoring: Focuses entirely on enhancing internal code readability, reducing complexity, and improving maintainability.
    Adding Features: Focuses on creating new functionality, changing system behavior, and delivering new capabilities to users.

3. Explain the difference between:
Validation
Error Handling
Debugging
Give one example of each.
    - Validation checks user input against rules before processing, like rejecting a password that is too short.
    Error Handling manages unexpected runtime failures to prevent crashes, like displaying an error message when a database connection fails.Debugging is the manual process of investigating and fixing broken code, like tracing lines of source code to find a calculation bug.

4. What are "magic numbers" and "magic strings"? Why should they usually be avoided?
Example:
discount = price * 0.15

vs

DISCOUNT_RATE = 0.15
discount = price * DISCOUNT_RATE
    - "Magic numbers" and "magic strings" are hardcoded, unexplained values in source code that should be avoided because they hide developer intent, make updates difficult, and increase the risk of typos.
    In your example, replacing the unexplained number 0.15 with the named constant DISCOUNT_RATE instantly makes the code self-documenting and allows you to change the discount percentage globally in just one single location.

5. If another developer has to maintain your Student Profile Manager six months from now, what coding practices would make their job easier?
    - To ensure long-term maintainability, transition from custom text parsing to standard formats like JSON, decouple your command-line interface from the core business logic, and encapsulate your global state within clearly defined classes using explicit type hints.