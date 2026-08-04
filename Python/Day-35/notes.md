1. File Handling
Learn:
What is file handling?
Why file handling is important
Reading files
Writing files
Appending files
File modes (r, w, a, x)
Context managers (with open())
    - File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface. It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.

2. Exception Handling
Understand:
What is an exception?
Why exceptions occur
try
except
else
finally
Raising exceptions
    - Exception handling is a programming mechanism that detects and manages runtime errors using try, except, else, and finally blocks to prevent programs from crashing.

3. Built-in Exceptions
Know the purpose of:
ValueError
TypeError
IndexError
KeyError
FileNotFoundError
ZeroDivisionError
    - Built-in exceptions are predefined error types in Python that signal specific issues, such as invalid values (ValueError), incorrect types (TypeError), missing sequences (IndexError), absent keys (KeyError), missing files (FileNotFoundError), or division by zero (ZeroDivisionError).

4. Custom Exceptions
Learn:
Why create custom exceptions
Creating a class that inherits from Exception
Raising custom exceptions
Catching custom exceptions
    - Custom exceptions are user-defined error classes that inherit from the base Exception class, allowing developers to raise and catch highly specific, meaningful errors tailored to their application's unique business logic.

5. Best Practices
Study:
Never use bare except:
Catch only expected exceptions
Keep try blocks small
Provide meaningful error messages
    - Best practices require keeping try blocks small, catching only expected errors instead of using a bare except:, and providing meaningful error messages to ensure code remains maintainable and easy to debug.