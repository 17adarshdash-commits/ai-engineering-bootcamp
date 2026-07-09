1. What is a module? Why do we use modules?
    - A module is a file containing code we want to include in our program. We include that file using the 'import' function. We use modules as it is useful to break down a large program into reusable seperate files.

2. Explain the difference between:
import math and from math import sqrt
    - import math: used to include the inbuilt module math in our program and to use its functions we need to write math."function"().
    from math import sqrt: used to directly include the sqrt function of the math module in our program and we dont need to write math.sqrt(), we can directly write sqrt() to use it.

3. What does as do? Give an example.
    - In Python, the as keyword is used to create an alias, which gives an alternate, usually shorter name to a module, function, or variable.
    Example:
    import random as rd
    print(rd.randint(1, 10))

4. Explain these file modes:
* r
* w
* a

When would you use each?
    - r (Read Mode): Opens a file strictly for reading text.
    w (Write Mode): Opens a file strictly for writing text.
    a (Append Mode): Opens a file for writing, but the file pointer is placed at the very end of the file.

5. Why is with open() preferred over open()?
    - Using with open() over open ()is preferred because it automatically closes the file for you, even if an error or crash occurs inside the block.

6. Difference between:
read()
readline()
readlines()
    - read(): Reads the entire file as a single, continuous string.
    readline(): Reads only the next single line of the file as a string.
    readlines(): Reads the entire file and splits it into a list of individual line strings.

7. What happens if you open a file in:

* w mode?
* a mode?
    - w mode: Python will completely wipe out (overwrite) all existing content in the file, or create a brand new file if it does not already exist.
    a mode: Python will preserve your existing data and safely place your cursor at the very end of the file to add new content, or create a new file if it is missing.