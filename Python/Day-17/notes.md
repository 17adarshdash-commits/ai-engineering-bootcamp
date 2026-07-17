1. What is modular programming? Why is it better than writing everything in one file?
    - Modular programming splits code into separate, independent pieces to make software easier to maintain, reuse, and test than one large file.

2. What is input validation?
Explain the difference between:
Type Validation
Range Validation
Format Validation
Give one example of each.
    - Input validation ensures that user input meets specific criteria before processing, differentiating between type validation (checking data types, like ensuring age is an integer), range validation (checking numeric or date limits, like restricting age between 1 and 120), and format validation (checking structural patterns, like verifying an email contains an "@" symbol).

3. Why should business logic and user interaction be separated? Give one real-world example.
    - Separating business logic from user interaction allows you to change the visual interface without breaking the underlying calculations, such as updating a banking app's design while ensuring the interest rate formula remains completely untouched and functional.

4. Imagine your Expense Tracker grows to 5,000 lines. How would functions and modules make it easier to maintain?
    - Functions and modules would break that 5,000-line file into small, structured pieces, allowing you to fix bugs in isolated files like analytics.py without risking changes to your core data storage code.

5. What are the advantages of planning a program before writing code? Mention at least five.
    - Planning a program before coding saves time, prevents logical errors, refines the app structure, reduces development costs, and aligns team communication.