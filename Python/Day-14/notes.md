1. What is a Python standard library? Why is it useful?
    - The Python standard library is a built-in collection of pre-written modules included automatically with every Python installation to handle common programming tasks. It allows developers to write efficient, cross-platform code immediately without downloading third-party software or managing external dependencies.

2. Explain the purpose of these modules:

* math
* random
* datetime
* os

Give one real-world use case for each.
    - math: Provides advanced mathematical functions and constants for precise numeric calculations. 
    Use Case: Calculating the precise trajectory of a rocket using trigonometric functions and the constant Pi.

    random: Generates pseudo-random numbers, selects random elements, and shuffles sequences.
    Use Case: Selecting a random winning ticket number from an array of participants in an online lottery drawing.

    datetime: Supplies classes for manipulating and formatting dates, times, and time intervals.
    Use Case: Calculating the exact number of days remaining until a customer's subscription renewal date.

    os: Provides a portable way to interact with the host operating system and file system.
    Use Case: Automating the bulk renaming of thousands of raw image files inside a specific desktop folder.

3. What’s the difference between: import math and from math import sqrt?
    - import math: Imports the entire module, requiring you to use the module name as a prefix (math.sqrt(16)) to access its functions.
    from math import sqrt: Imports only the specific function into your program, allowing you to call it directly (sqrt(16)) without the prefix.

4. When would you use:

* random.randint()
* math.sqrt()
* datetime.now()
* os.getcwd()
    - random.randint(): Use this when you need a whole number within a strict range, like rolling a 6-sided die or generating a temporary 4-digit PIN.
    math.sqrt(): Use this when calculating geometric distances, like finding the hypotenuse of a triangle or checking the radius of a circle.datetime.now(): Use this when you need a real-time timestamp, like logging the exact moment a user clicks a button or saves a document.os.getcwd(): Use this when your script needs to locate itself, like finding the folder where it is running to read a nearby data file.

5. Why are built-in modules better than writing everything from scratch?
    - Built-in modules are better because they are thoroughly tested for bugs, highly optimized for speed, and instantly available without spending time writing and maintaining foundational code from scratch.