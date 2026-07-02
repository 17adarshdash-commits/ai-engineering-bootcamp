1. What is a string?
    - A string is a sequence of characters enclosed in either ' ' or " ".

2. Why are strings immutable?
    - Strings are immutable to optimize memory through sharing and ensure security as well.

3. Difference between indexing and slicing.
    - Indexing extracts a single character from a string based on the index whereas slicing can extract a range of characters based on the starting point to the ending point.

4. Explain positive and negative indexing with an example.
    - Positive indexing is from the start(left) of the string starting with index 0,1,2 ... whereas Negative indexing starts from the end(right) of the string with index -1,-2,-3 ...
    Example-
    s: "Adarsh"
    s[0] will give "A" and s[-1] will give "h".

5. What does each of these methods do?
.upper()
.lower()
.title()
.capitalize()
.strip()
.replace()
.find()
.count()
.split()
.join()
    - .upper() returns the string with all letters in upper case.
    .lower() returns the string with all letters in lower case.
    .title() returns the string with each word's(in the string) starting character in upper case.
    .capitalize() returns the string with the first character in the string in upper case.
    .strip() returns the string with all whitespaces removed or removes specific characters if they are passed as arguments.
    .replace() returns the string with the character/characters replaced with whatever passed as argument.
    .find() returns the index of the first occurence of the character passed as an argument.
    .count() returns the number of occurences of that character(argument) in the string.
    .split() breaks a single string into a list of substrings based on a delimiter.
    .join() takes a list of strings and combines them into a single string using a specified separator.

6. Difference between: .find() and .index()
    - The main difference is how they handle missing values: .find() returns -1 if the substring is not found, whereas .index() raises a ValueError exception that will crash your program if not caught.

7. What are f-strings?

Why are they better than: print("Hello " + name)
    - f-strings are formatted string literals prefixed with f that embed expressions inside curly braces, making them better than concatenation because they are faster, more readable, and automatically convert data types without crashing.

Reflection

1. What concept did I understand best today?
    - Optimizing approaches to lower time complexity.

2. What took me the longest?
    - The valid anagram question.

3. What is one thing I still find confusing?
    - Finding the correct way to approach the problem at the start is little tricky, but once I get the starting bit, I find it easier