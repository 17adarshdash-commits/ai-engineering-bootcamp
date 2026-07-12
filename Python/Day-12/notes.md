1. What is inheritance? Why is it useful? Give one real-world example.
    - Inheritance is basically inheriting the features(attributes and methods) of the parent class. It is useful as it helps with code reusability i.e. developers can write common logic once in a parent class and reuse it across multiple child classes.
    Real-World Example: E-Commerce Payment System

2. Difference between:

* Parent Class
* Child Class

    - Parent class(acts as foundational blueprint) is the super class from which features are inherited whereas child class(extends that blueprint) is the class which inherits those features.

3. What does super() do? When should we use it?
    - The super() function is a built-in tool that allows a child class to call methods and access properties from its parent class.
    Use super() when a child class needs to initialize parent properties or extend an existing parent method without rewriting its logic.

4. What is Method Overriding? Why would we override a method?
    - Method overriding occurs when both parent and child class have the same method but the child class method overrides the parent class method. We override a method to replace generic parent logic with specific behavior tailored to the unique needs of a child class.

5. What is Polymorphism? Give one real-world example.
    - Polymorphism is a core Object-Oriented Programming (OOP) concept that allows different objects to respond to the same command or method in their own unique way. Real-World Example: Payment Processing

6. What are the four pillars of OOP?

Briefly explain:

* Encapsulation
* Abstraction
* Inheritance
* Polymorphism

    - Encapsulation: Bundling data and methods into a single class while restricting direct access to shield the internal state.
    Abstraction: Hiding complex implementation details to show only the essential features needed for interaction.
    Inheritance: Enabling a new class to automatically receive properties and behaviors from an existing class to reuse code.
    Polymorphism: Allowing different objects to execute the exact same method in their own unique way.