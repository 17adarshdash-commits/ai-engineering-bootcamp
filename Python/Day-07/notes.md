1. What is a function? Why do we use functions?
    - A function is a named block of reusable code that performs a specific task and it only executes when it is explicitly called.

2. Difference between Parameter & Argument
    - A parameter is what is passed in the function header and an argument is what is explicitly mentioned while calling the function.

3. What does return do? Difference between print() and return.
    - A return statement is used at the end of a function and it returns a particular value to the statement that called the function.
    A print statement just prints whatever is passed inside the parentheses.

4. What are default arguments? Give an example.
    - Default arguments are specified in the function header and are used only if we dont pass a value for that parameter in the function call.
    Example: 
    def greet(name="Guest"):
        print(f"Hello, {name}!")
    greet()  

5. Difference between:

* Positional arguments
* Keyword arguments
    - Positional arguments rely entirely on the order (the position) of the values you pass in.
    Keyword arguments rely on explicitly naming the variable (name=value), meaning the order does not matter.

6. What are *args and **kwargs? When would we use them?
    - *args and **kwargs are special symbols in Python that allow a function to accept a variable number of arguments.
    *args (Arguments) lets a function take any number of extra positional arguments. It stores them as a tuple (a packed list).
    **kwargs (Keyword Arguments) lets a function take any number of extra keyword arguments. It stores them as a dictionary (labeled key-value pairs).

7. Explain:

* Local variable
* Global variable

Which one should be preferred?
    - Local variables are the variables whose values are valid only within the scope of the function whereas global variables are the variables that are valid throughout the program.
    As a general best practice in Python, local variables should always be preferred over global variables.