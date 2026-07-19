1. What is code reusability? Why is it important?
    - Code reusability means writing a block of software code once so it can be used multiple times across different parts of a program or in other projects.It is important because it saves development time, reduces programming errors through pre-tested code, and simplifies future updates by keeping logic in one central place.

2. What is the difference between:
Reusability
Readability
Maintainability
Give an example of each.
    - Reusability is the ability to use existing code in multiple places without rewriting it, like calling a single calculate_tax() function for every checkout screen.
    Readability is how easily a human developer can understand the purpose and logic of code, such as using clear names like user_age instead of a vague variable like x.
    Maintainability is how easily code can be modified, fixed, or scaled over time, such as changing a database password in one configuration file instead of updating hundreds of individual code files.

3. Why should large programs be broken into functions? What problems occur if everything is written inside main()?
    - Large programs are broken into functions to make the code modular, reusable, and easy for a human developer to understand and test.Problems with Everything Inside main()Writing everything inside main() creates a giant, confusing block of code that is incredibly difficult to debug, impossible to reuse, and prone to breaking whenever a small change is made.

4. What makes code "clean"?
Discuss things like:
Naming variables
Comments
Function size
Duplicate code
Formatting
    - Code is considered clean when it is simple, direct, and so easy to read that it looks like it was written by someone who cares.
    Naming variables: Use meaningful, self-explanatory names like total_price instead of vague abbreviations like tp.
    Comments: Use them sparingly only to explain why tricky logic exists, rather than explaining what obvious code does.
    Function size: Keep functions small, focused, and dedicated to doing exactly one single task perfectly.
    Duplicate code: Eliminate repetition entirely by pulling shared logic into single, reusable functions.
    Formatting: Use consistent indentation, spacing, and line breaks so the code is visually effortless to scan.

5. Imagine your Expense Tracker grows to 5,000 lines. How would breaking it into functions make future updates easier?
    - Breaking a 5,000-line Expense Tracker into functions makes future updates easier by isolating features so you can edit one part, like adding a new currency, without accidentally breaking another part, like the analytics charts.