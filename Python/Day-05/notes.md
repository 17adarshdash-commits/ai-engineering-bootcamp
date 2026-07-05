1. What is a list?
    -   A list is an ordered, mutable collection of elements enclosed in []. It allows duplicate values.

2. Why are lists mutable? How is this different from strings?
    - Lists are mutable because they are stored as references in memory, allowing you to change, add, or remove items without creating a completely new list. Strings are immutable.

3. Explain:
append()
insert()
remove()
pop()
sort()
reverse()
clear()
index()
count()
    - append(): used to add 1 element at the end of a list.
    insert(): used to insert an element at a particular position(index) in the list.
    remove(): used to remove an element from the list by passing the value of the element to be removed.
    pop(): used to remove an element from the list by passing the index of element to be removed.
    sort(): used to sort the list.
    reverse(): used to reverse the order of the elements in list.
    clear(): used to clear the list(make it empty).
    index(): used to retrieve the index of the first occurence of the element whose value is used as argument.
    count(): used to return the number of times that element occurs in that list.

4. Difference between append() and extend():
    - append() is used to add a single element to the existing list.
    extend() is used to add multiple elements to the existing list.

5. Difference between pop() and remove():
    - pop() removes element from list by passing index whereas remove() removes an element from the list by passing the value of the element to be removed.

6. What is a nested (2D) list? Give one real-life example.
    - A nested (2D) list is a list where each element is itself a list, creating a tabular structure of rows and columns (a matrix).
    Real-Life Example: A Digital Cinema Seat Map