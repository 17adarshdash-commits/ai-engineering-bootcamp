1. Inheritance
Learn:
What is inheritance?
Why inheritance exists
Parent class (Base Class)
Child class (Derived Class)
Advantages of inheritance
Real-world examples
    - What is inheritance?Inheritance is a programming mechanism where a new class automatically acquires the properties and behaviors of an existing class.Why inheritance existsIt exists to eliminate code redundancy by allowing developers to reuse existing code across multiple related objects.Parent class (Base Class)The parent class is the original, higher-level class that contains the common attributes and methods to be shared.Child class (Derived Class)The child class is the specialized class that inherits from the parent and can add its own unique features.Advantages of inheritanceIt minimizes code duplication, simplifies software maintenance, and establishes a clear, logical hierarchy in your program.Real-world examplesA real-world example is a "Vehicle" parent class sharing traits like speed and fuel capacity with child classes like "Car" and "Motorcycle."

2. Types of Inheritance
Understand:
Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
    - Single Inheritance“In single inheritance, a sub-class is derived from only one super class,”meaning one child class directly extends exactly one parent class.Multiple Inheritance“In Multiple inheritance, one class can have more than one superclass and inherit features from all parent classes.”Multilevel Inheritance“Multilevel inheritance means a class is derived from another derived class, forming a chain of inheritance”similar to a grandchild, parent, and grandparent relationship.Hierarchical Inheritance“In hierarchical inheritance, more than one subclass is inherited from a single base class”to form a tree-like structure.

3. Method Overriding
Explain:
What is method overriding?
Why override methods?
How Python chooses which method to call.
    - What is method overriding?Method overriding occurs when a child class provides a specific implementation for a method that is already defined in its parent class.Why override methods?It allows a child class to change or specialize a generic behavior inherited from the parent class to fit its specific needs.How Python chooses which method to callPython uses the Method Resolution Order (MRO) to search for the method starting from the child class up through the parent hierarchy, executing the first matching name it finds.

4. super()
Learn:
What super() does
Calling the parent constructor
Calling parent methods
Why super() is preferred
    - What super() doesThe super() function creates a temporary object of the parent class, allowing you to access its inherited methods and properties.Calling the parent constructorUsing super().__init__() triggers the parent class constructor to guarantee that all base attributes are properly initialized within the child object.Calling parent methodsIt lets a child class execute an overridden method from the parent class to extend its original functionality rather than completely replacing it.Why super() is preferredIt is preferred because it eliminates the need to explicitly hardcode the parent class name, keeping your code flexible and maintainable in complex multi-inheritance setups.

5. Polymorphism (Introduction)
Study:
What is polymorphism?
Same interface, different behavior
Real-world examples
Advantages
    - What is polymorphism?Polymorphism is the programming concept where a single interface or entity can take on multiple distinct forms.Same interface, different behaviorIt allows different object classes to share the exact same method names while executing completely different, customized code internally.Real-world examplesA real-world example is a single "Play" button that starts video on a streaming app but triggers music on an audio app.AdvantagesIt makes your software highly adaptable, extensible, and clean by allowing a single function to process different object types without complex conditional checks.