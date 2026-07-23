"""
LeetCode 153 - Find Minimum in Rotated Sorted Array

Difficulty: Medium
Pattern: Binary Search

Problem:
Suppose an array of unique integers is sorted in ascending order
and then rotated between 1 and n times.

Return the minimum element.

You must write an algorithm that runs in O(log n) time.

Examples:

Input:
nums = [3,4,5,1,2]

Output:
1

----------------------------

Input:
nums = [4,5,6,7,0,1,2]

Output:
0

----------------------------

Input:
nums = [11,13,15,17]

Output:
11

--------------------------------------------------
Approach
--------------------------------------------------

A rotated sorted array always has one sorted half.

Compare the middle element with the last element.

If nums[mid] > nums[right]:
    The minimum must be in the right half,
    because the rotation point lies after mid.

Otherwise:
    The minimum is either at mid or somewhere
    in the left half.

Continue shrinking the search space until
left == right.

That index contains the minimum element.

--------------------------------------------------
Why compare with nums[right]?
--------------------------------------------------

Example:

nums = [4,5,6,7,0,1,2]

mid = 7
right = 2

Since 7 > 2,
the minimum must be to the right of mid.

Another example:

nums = [5,6,7,0,1,2,3]

mid = 0
right = 3

Since 0 < 3,
the minimum could be mid itself,
so we keep mid by moving:

right = mid

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

• Rotated arrays are not fully sorted,
  but one half is always sorted.
• Compare nums[mid] with nums[right].
• If nums[mid] > nums[right],
  search the right half.
• Otherwise,
  keep mid and search the left half.
• The search ends when left == right.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left < right:

            # Overflow-safe midpoint
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]