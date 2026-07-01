1. What is a variable?
    - A variable is something that stores/holds a value which can be used in the program.

2. Difference between int, float, str, and bool.
    - int stores numeric values without decimal points
      float stores numeric values with precision (can include decimal points)
      str stores alphanumeric characters and is enclosed in either '' or " "
      bool stores boolean values such as True/False

3. What does input() return by default?
    - input() by default returns string values.

4. Why do we need int() and float()?
    - input() always returns a string. We need int() and float() to convert that string to numeric type used in our program.

5. Difference between = and ==.
    - The difference between = and == is that = is used as an assignment operator (to assign values to variables) and == is used as a           comparison operator (to compare values between 2 things).

6. What is Big O notation?
    - Big O notation tells us how the algorithm's operational time changes w.r.t. change in input size.

7. Why is Big O important?
    - Big O is important as the smaller the time complexity, the lesser time it takes to do that operation and uses less computational power which helps software engineers.

8. Explain these with one real-life example each:

* O(1)
* O(log n)
* O(n)
* O(n²)
    - O(1) means that the algorithm doesn't grow with changing input size. Used in HashMaps.
    O(log n) means that the algorithm grows proportionally to the log of input size. Used in Binary Search(Array of size 8 can be halved a max of 3 times).
    O(n) means that the algorithm grows proportionally to the input size. Used in Linear Search(Searching for a number in an unsorted array may require checking all elements in the array).
    O(n²) means that the algorithm grows proportionally to the square of changing input size. Used in nested loops.

9. Which one is faster as n gets very large?
    - O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n) < O(n!)