"""
LeetCode 744 - Find Smallest Letter Greater Than Target

Difficulty: Easy
Pattern: Binary Search

Problem:
Given a sorted list of characters 'letters' and a target character,
return the smallest character that is lexicographically greater than
the target.

The letters wrap around.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"

Output:
"c"

----------------------------

Input:
letters = ["c", "f", "j"]
target = "c"

Output:
"f"

----------------------------

Input:
letters = ["c", "f", "j"]
target = "j"

Output:
"c"

--------------------------------------------------
Approach
--------------------------------------------------

The letters are already sorted.

We use Binary Search to find the first letter that is
strictly greater than the target.

If letters[mid] <= target,
the answer must be on the right side.

Otherwise,
store the possible answer by moving left.

After Binary Search:

• If left is still inside the array,
  letters[left] is the answer.

• If left goes beyond the last index,
  the answer wraps around to letters[0].

--------------------------------------------------
Time Complexity

O(log n)

--------------------------------------------------
Space Complexity

O(1)

--------------------------------------------------
Key Takeaways

• Binary Search can find the first element greater than a target.
• Always use integer division (//) for the midpoint in Python.
• Some Binary Search problems require handling edge cases such as wrap-around.
"""


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        left = 0
        right = len(letters) - 1

        while left <= right:

            # Overflow-safe midpoint
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # Wrap around if necessary
        return letters[left] if left < len(letters) else letters[0]