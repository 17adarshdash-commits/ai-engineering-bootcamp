1. Why should large programs be divided into functions? Give one real-world example.
    - Large programs should be divided into functions to manage complexity, eliminate repetitive code, and make debugging easier.
    Real-World Example: Online shopping app like Amazon.

2. What makes code “clean” and maintainable? Mention at least five good coding practices.
    - Code is considered “clean” and maintainable if it can be read, understood, and modified easily by any developer—including the original author months after writing it.
    5 Good Coding Practices
    Meaningful Naming: Use descriptive names for variables and functions (e.g., calculate_total_price() instead of ctp()).
    Single Responsibility: Ensure each function or class handles exactly one specific task or behavior.
    Don't Repeat Yourself (DRY): Replace duplicate code blocks with reusable functions or loops.
    Consistent Formatting: Maintain uniform indentation, spacing, and styling rules throughout the entire codebase.
    Robust Error Handling: Predict potential failures and use standard error catchers to prevent ungraceful crashes.

3. Why is input validation important? Give two examples.
    - Input validation ensures your program only processes safe, correctly formatted data. Without it, malformed data can trigger unhandled system crashes, corrupt your databases, or leave your application open to severe security breaches.
    Two Examples of Input Validation
    Type and Boundary Checking (Calculator App)
    Format Checking (Online Sign-up Forms)

4. What is a menu-driven program? Where are they commonly used?
    - A menu-driven program is an application that presents users with a structured list of options to guide their interactions, executing specific tasks based on the user's selection rather than requiring them to memorize complex text commands. This user-friendly design is commonly used in interactive voice response (IVR) phone systems, automated teller machines (ATMs), embedded systems like digital microwave displays, and command-line interface (CLI) setup utilities to simplify navigation and restrict user inputs to predefined, safe operations.

5. Why should we avoid repeating code? How do functions help?
    - Repeating code creates bloated programs where a single bug is duplicated across multiple lines, making updates tedious and error-prone. Functions solve this by bundling logic into a single, reusable block that you write once and call anywhere. If you need to fix a bug or change how the logic works, you only update it inside that one function, and the change instantly applies everywhere.