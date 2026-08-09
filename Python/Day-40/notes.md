1. Testing
Learn:
What is testing?
Why testing is important
Manual vs automated testing
Unit testing
Test cases
Assertions
    - Testing is the practice of running code against known inputs to check that it produces the expected outputs, catching bugs before users do. It matters because it turns "I think this works" into "I verified this works," and it keeps working as the codebase grows - a change that breaks something old shows up immediately instead of surfacing as a production bug. Manual testing is a person clicking through the app and eyeballing the result; it's slow, inconsistent, and gets skipped under deadline pressure. Automated testing is code that tests other code - it runs in seconds, the same way every time, and can run on every commit. Unit testing is automated testing aimed at the smallest testable pieces (a single function or method) in isolation from the rest of the system. A test case is one specific scenario being checked (e.g. "dividing by zero raises an error"), and an assertion is the actual check inside it - a statement that says "this expression must be true, or the test fails."

2. unittest
Understand:
unittest module
TestCase
assertEqual()
assertTrue()
assertFalse()
assertRaises()
Running tests
    - `unittest` is Python's built-in testing framework, modeled on JUnit's xUnit style. Tests are grouped into classes that subclass `unittest.TestCase`; each method starting with `test_` is discovered and run automatically. `TestCase` provides assertion methods that give clear failure messages: `assertEqual(a, b)` checks `a == b`, `assertTrue(x)` / `assertFalse(x)` check truthiness, and `assertRaises(SomeError)` (used as a context manager) checks that a block of code raises the given exception - the test fails if it doesn't. Tests are run with `python -m unittest filename.py`, which discovers every `TestCase` subclass in the file and reports pass/fail/error counts.

3. Debugging
Study:
What is debugging?
Reading tracebacks
Common Python errors
Using breakpoint()
Debugging strategies
    - Debugging is the process of locating and fixing the cause of incorrect behavior in a program. A traceback is Python's report of an unhandled exception: it lists the call stack from where execution started down to the line that raised the error, with the error type and message last - read it bottom-up to find the actual failure point, then trace upward to see how execution got there. Common errors include `ZeroDivisionError` (dividing by zero), `IndexError` (accessing a list index that doesn't exist), `KeyError` (accessing a dict key that doesn't exist), and `TypeError` (an operation applied to a value of the wrong type). `breakpoint()` drops into Python's interactive debugger (`pdb`) at that exact line, letting you inspect variables and step through execution live instead of guessing from print statements. General strategies: reproduce the bug reliably, read the traceback carefully, narrow down the failing section (print/breakpoint), form a hypothesis, test it, and fix the root cause rather than the symptom.

4. Code Quality
Learn:
Clean code
Naming conventions
DRY (Don't Repeat Yourself)
KISS (Keep It Simple)
Comments vs self-documenting code
    - Clean code is code that's easy for another person (or future you) to read, understand, and change safely. Naming conventions - descriptive variable/function names, `snake_case` for functions and variables, `PascalCase` for classes - make code self-explanatory without needing comments to explain what a name should have said. DRY means avoiding duplicated logic: repeated code drifts out of sync as one copy gets fixed and the other doesn't, so shared behavior belongs in one function. KISS means preferring the simplest solution that correctly solves the problem over a cleverer one that's harder to follow. Self-documenting code (clear names, small functions, obvious structure) is preferred over comments explaining *what* code does; comments are best reserved for *why* a non-obvious decision was made.

5. Best Practices
Understand:
Write small functions
Validate inputs
Test edge cases
Handle expected exceptions
Keep business logic separate from UI
    - Small functions that do one thing are easier to test, name, and reuse than large ones doing several things at once. Validating inputs at the boundary (before they reach core logic) turns silent bad data into an immediate, clear error. Edge cases - empty input, zero, negative numbers, boundary values, missing keys - are where bugs hide, so tests should deliberately target them, not just the "happy path." Expected exceptions (a file that might not exist, a division that might be by zero) should be caught and handled deliberately, not left to crash the program. Keeping business logic (the actual rules and computations) separate from UI/CLI code means the core logic can be tested and reused without needing a terminal, a web server, or user input to exercise it - this is the same separation the banking system's `Bank`/`Account` classes vs. `main.py` menu demonstrates.
