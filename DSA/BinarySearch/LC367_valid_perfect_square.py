"""
LeetCode 367 - Valid Perfect Square

Difficulty: Easy
Pattern: Binary Search

Problem:
Given a positive integer num, return True if num is a perfect square.
Otherwise, return False.

Do not use any built-in library functions such as sqrt().

Example:
Input: num = 16
Output: True

Input: num = 14
Output: False

--------------------------------------------------
Approach
--------------------------------------------------

Instead of checking every number from 1 to num, we use Binary Search.

Observation:

If mid * mid <= num:
    mid could still be the square root.
    Save it as the current best answer and search the right half.

If mid * mid > num:
    mid is too large.
    Search the left half.

After Binary Search finishes, the variable "result" stores the
largest integer whose square is less than or equal to num.

If result² == num,
then num is a perfect square.
Otherwise, it is not.

--------------------------------------------------
Why use:

mid <= num // mid

instead of

mid * mid <= num ?

Using division avoids integer overflow in languages like C++ and Java.
Although Python integers do not overflow, this is considered good
interview practice.

--------------------------------------------------
Time Complexity

O(log n)

Binary Search halves the search space in every iteration.

--------------------------------------------------
Space Complexity

O(1)

Only a few variables are used.

--------------------------------------------------
Key Takeaways

• Binary Search can search an answer space, not just a sorted array.
• Many problems share the same Binary Search pattern with only small changes.
• Saving the current valid answer allows us to verify whether the final answer is a perfect square.
• Using num // mid avoids multiplication overflow.
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # Edge case
        if num == 1:
            return True

        left = 1
        right = num // 2
        result = 0

        while left <= right:

            # Overflow-safe midpoint calculation
            mid = left + (right - left) // 2

            # mid² <= num
            if mid <= num // mid:
                result = mid
                left = mid + 1

            # mid² > num
            else:
                right = mid - 1

        # Check if the integer square root is exact
        return result * result == num