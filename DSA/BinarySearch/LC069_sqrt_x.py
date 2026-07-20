"""
LeetCode 69 - Sqrt(x)

Difficulty: Easy
Pattern: Binary Search

Problem:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

Example:
Input: x = 8
Output: 2

Explanation:
The square root of 8 is approximately 2.828, so we return 2.

--------------------------------------------------
Approach
--------------------------------------------------

Instead of checking every number from 1 to x, we use Binary Search.

Observation:

If mid * mid <= x:
    mid is a possible answer.
    Try searching the right half to find a larger valid square root.

If mid * mid > x:
    mid is too large.
    Search the left half.

We keep track of the latest valid answer using the variable "result".

--------------------------------------------------
Why use:

mid <= x // mid

instead of

mid * mid <= x ?

Using division avoids integer overflow in languages like C++ and Java.
Although Python integers don't overflow, this is considered good interview practice.

--------------------------------------------------
Time Complexity

O(log n)

Each iteration halves the search space.

--------------------------------------------------
Space Complexity

O(1)

Only a few variables are used.

--------------------------------------------------
Key Takeaways

• Binary Search isn't only for searching arrays.
• It can also search the "answer space".
• Always save the current valid answer before searching further.
• Using x // mid is safer than mid * mid.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Edge cases
        if x < 2:
            return x

        left = 1
        right = x // 2
        result = 0

        while left <= right:

            # Prevent overflow in other languages
            mid = left + (right - left) // 2

            # mid^2 <= x
            if mid <= x // mid:
                result = mid
                left = mid + 1

            # mid^2 > x
            else:
                right = mid - 1

        return result