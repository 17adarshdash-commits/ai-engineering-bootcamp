1. Iterators
Learn:
What is an iterator?
Iterable vs Iterator
iter()
next()
StopIteration
Why iterators are memory efficient
    - An iterator is a Python object used to traverse a container one element at a time using iter() to initialize it, next() to fetch items, and StopIteration to signal the end, making it highly memory-efficient because it generates values on the fly instead of loading the entire dataset into memory.

2. Generators
Understand:
What is a generator?
yield
Generator functions
Generator expressions
Why generators are useful
Generator vs List
    - A generator is a specialized function or expression that produces a sequence of values lazily using the yield keyword, making it far more memory-efficient than a list because it processes items one at a time on demand rather than storing the entire collection in memory.

3. Decorators
Study:
What is a decorator?
Why decorators exist
Higher-order functions
Wrapper functions
@decorator syntax
Real-world examples
    - A decorator is a higher-order function that takes another function as an argument, extends its behavior using an internal wrapper function without modifying its source code, and is applied cleanly using the @decorator syntax for real-world tasks like logging, timing, and authentication.

4. Closures
Learn:
Inner functions
Lexical scope
Returning functions
Why closures are useful
    - A closure is an inner function that retains access to variables from its enclosing lexical scope even after the outer function has finished executing, which is useful for data hiding and dynamically creating customized functions without using global variables.

5. Iterator vs Generator
Compare:
Memory usage
Speed
Readability
Typical use cases
    - While both stream data lazily to save memory, generators are faster to write and more readable due to the yield keyword, making them ideal for simple data pipelines, whereas iterators require a custom class structure, making them better suited for complex, stateful data structures.