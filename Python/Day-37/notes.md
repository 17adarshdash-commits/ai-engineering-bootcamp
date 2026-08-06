1. Modules
Learn:
What is a module?
Why modules exist
Importing modules
import
from ... import
import ... as
Built-in modules
User-defined modules
    - A module is simply a file containing Python code (functions, classes, variables) that can be imported and reused in other programs, and modules exist to organize code, avoid repetition, and keep programs maintainable.

2. Packages
Understand:
What is a package?
__init__.py
Package hierarchy
Importing from packages
Absolute vs relative imports (introduction)
    - A package is a directory of related modules grouped together, marked as importable by an __init__.py file, allowing large codebases to be organized into a hierarchical, importable namespace.

3. Virtual Environments
Study:
What is a virtual environment?
Why virtual environments exist
venv
Creating a virtual environment
Activating/deactivating it
Installing packages inside it
requirements.txt
    - A virtual environment is an isolated Python environment with its own dependencies, created with venv so that packages installed for one project don't conflict with those needed by another.

4. Python Standard Library
Learn about:
math
random
datetime
os
sys
Understand when each is commonly used.
    - The Python Standard Library is a collection of built-in modules like math, random, datetime, os, and sys that ship with Python and provide ready-made tools for common tasks like calculations, randomness, dates, file systems, and interpreter interaction.

5. Project Organization
Understand:
Splitting code into multiple files
Why modular code is important
Avoiding duplicate code
Importing your own modules
    - Project organization is the practice of splitting code into multiple files and modules based on responsibility, which keeps programs modular, avoids duplicate code, and makes large codebases easier to navigate and maintain.
