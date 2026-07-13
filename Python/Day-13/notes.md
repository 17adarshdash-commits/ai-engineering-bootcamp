1. What is Encapsulation? Why is it important?
    - Encapsulation is the process of hiding important data and only allow controlled access to it. It is important as we protect the important data from access to everyone and only gives controlled access.

2. Explain the difference between:
   - Public Members
   - Protected Members
   - Private Members

   - * Public Members: Accessible from anywhere in the program.
* Protected Members (_name): Intended for internal use and subclasses by convention, but still accessible from outside.
* Private Members (__name): Name-mangled to discourage direct access and mainly accessed through class methods.

3. Why do we use getters and setters? Give one real-world example.
    - We use getters and setters to control how class data is accessed and modified, ensuring validation, security, and data integrity through encapsulation. Real-World Example: A Bank Account

4. What is Abstraction? How is it different from Encapsulation?
    - Abstraction is the process of only showing those information that is required not showing the unnecessary information. Encapsulation restricts direct access to data at the code level to secure how an object operates.

5. Can Python truly make variables private? Explain why or why not.
    - No, Python cannot truly make variables private because it does not have strict enforcement modifiers like other languages.

6. Give one real-world example where all four OOP pillars are used together. 
    - A Smartphone is a perfect real-world example that uses all four OOP pillars simultaneously