1. What is a tuple? How is it different from a list?
    -   A tuple is an ordered, immutable collection of elements that allows duplicate values and is enclosed in (). They are much faster than lists [].

2. Why are tuples immutable? When should we use tuples?
    - Tuples cannot be changed because they are designed to be safe wrappers for data that must stay the exact same and we should use them to store things that will never change such as days of the week, months of the year etc.

3. What is a set? List three important properties.
    - A set is unordered and mutable collection of elements and they do not allow duplicate values.

4. Explain these set methods:
add()
remove()
discard()
pop()
clear()
update()
    - add(): used to add elements to the set by passing value of element to be added as argument.
    remove(): used to remove elements to the set by passing value of element to be removed as argument.
    discard(): removes a specific, named element and ignores missing values.
    pop(): removes and returns a random, unpredictable element from the set.
    clear(): clears all elements from the set entirely.
    update(): adds all elements from another iterable (set, list, tuple, etc.) into the current set.

5. What is a dictionary? Why is it called a Hash Map?
    - A dictionary is a collection of key-value pairs. A dictionary is the general concept of looking up data using keys, while a hashmap is the specific, ultra-fast method that uses a mathematical formula called a hash function to make those lookups happen almost instantly.

6. Difference between:
keys()
values()
items()
get()
- keys(): returns all the keys of the dictionary.
values(): returns all the values of the dictionary keys.
items(): returns key-value pairs as tuples.
get(): returns the value of the key passed as argument.

7. When would you use:
* List
* Tuple
* Set
* Dictionary
Give one real-life example for each.
    - Use a List when you have an ordered collection of items that might change or have duplicates. Real-life example: A shopping list where you can add, remove, or rearrange items.
    Use a Tuple when you have a fixed collection of items that must stay in a specific order and never change. Real-life example: GPS coordinates for a city, which always look like a locked pair of (Latitude, Longitude).
    Use a Set when you only care about unique items and the exact order does not matter. Real-life example: A guest list checking into a party, where you want to make sure no one is counted twice.
    Use a Dictionary when you want to connect a specific piece of information to a label so you can look it up instantly. Real-life example: A phone book where you look up a friend's name to instantly find their phone number.