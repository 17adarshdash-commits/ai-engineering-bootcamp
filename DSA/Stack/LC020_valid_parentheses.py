"""
LeetCode: 20
Title: Valid Parentheses

Difficulty: Easy

Pattern:
- Stack

Topics:
- String
- Stack
"""

# ==========================================================
# Brute Force Idea
# Time Complexity: O(n²)
# Space Complexity: O(n)
# ==========================================================

"""
A brute force approach would repeatedly search for matching pairs
such as (), [], and {} and remove them until no more pairs remain.

Why it is not optimal:
- Requires repeatedly scanning the string.
- Inefficient for long inputs.
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================================

class Solution(object):
    def isValid(self, s):
        stack = []

        for char in s:

            if char == '[' or char == '{' or char == '(':
                stack.append(char)

            elif char == ']' or char == '}' or char == ')':

                if not stack:
                    return False

                x = stack.pop()

                if x == '(' and char != ')':
                    return False

                if x == '[' and char != ']':
                    return False

                if x == '{' and char != '}':
                    return False

        if stack:
            return False

        return True


"""
What I Learned
--------------

1. A stack follows the Last In, First Out (LIFO) principle.

2. Push every opening bracket onto the stack.

3. When a closing bracket appears, pop the most recent opening bracket.

4. If the brackets do not match, the string is invalid.

5. If the stack is empty before popping, the string is invalid.

6. After processing all characters, the stack must be empty for the string to be valid.
"""


"""
Pattern Recognition
-------------------

Use a Stack when:

- You need to process nested structures.
- You need to match opening and closing symbols.
- The most recent element must be processed first.
- Problems involve parentheses, brackets, tags, or undo operations.
"""