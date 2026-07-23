1. What conditions must be true before Binary Search can be used?
    - The collection must be sorted in a consistent order and allow random access to elements so the search space can be repeatedly halved.

2. Explain the difference between:
Linear Search
Binary Search
When would you choose each?
    - Linear search checks elements sequentially and works on unsorted data, while binary search repeatedly halves a sorted search space; choose linear search for small, unsorted datasets, and binary search for large, pre-sorted datasets to achieve faster logarithmic time complexity.

3. Why is code reuse important? Give examples from your Student Profile Manager.
    - Code reuse is important because it reduces development time and prevents bugs by allowing developers to use proven, tested logic across multiple features. In a Student Profile Manager, code reuse can be seen when a single validation function checks GPA formatting for both creating a new profile and updating an existing one, or when a database connection utility is shared across student lookup, enrollment, and grading modules.

4. What is defensive programming? How does input validation improve software quality?
    - Defensive programming is a software design practice that anticipates potential errors and unexpected user actions to ensure continuous, predictable program execution.
    Input validation improves software quality by filtering out malformed data before it reaches core logic, which directly prevents application crashes, data corruption, and security vulnerabilities like injection attacks.

5. Why should programs separate business logic from user interface code?
    - Programs should separate business logic from user interface code to ensure that the core data-processing rules can be tested, maintained, and reused independently without being broken by visual or formatting changes to the layout.