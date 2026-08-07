1. Lambda Functions
Learn:
What is a lambda function?
Anonymous functions
Syntax
When to use lambda
Lambda vs normal functions
    - A lambda function is a small, anonymous, single-expression function defined with the `lambda` keyword (e.g. `lambda x: x * 2`), useful for short, throwaway logic passed directly into functions like `map()`, `filter()`, or `sorted()` without needing a full `def`.

2. Functional Programming
Understand:
map()
filter()
reduce()
Pure functions (introduction)
Why functional programming is useful
    - Functional programming treats computation as the application of functions to data rather than step-by-step mutation; `map()` transforms every item in an iterable, `filter()` keeps items matching a condition, `reduce()` folds an iterable down to a single value, and pure functions (same input always gives same output, no side effects) make code easier to test, reason about, and compose.

3. Context Managers
Study:
What is a context manager?
with statement
Automatic resource management
__enter__()
__exit__()
Why context managers exist
    - A context manager is an object that defines `__enter__()` and `__exit__()` so the `with` statement can set up and automatically tear down a resource (like a file or lock) even if an exception occurs, removing the need for manual try/finally cleanup.

4. functools
Learn:
reduce()
partial() (introduction)
    - The `functools` module provides higher-order function tools such as `reduce()` (imported from here in Python 3, since it's no longer a builtin) for folding an iterable into one value, and `partial()` for pre-filling some arguments of a function to create a new, simpler callable.

5. Best Practices
Understand:
When not to use lambda
Readability vs clever code
When normal functions are better
    - Lambdas should stay short and simple; once logic needs a name, multiple statements, comments, or reuse across the codebase, a regular `def` function is more readable and maintainable than a clever one-liner.
