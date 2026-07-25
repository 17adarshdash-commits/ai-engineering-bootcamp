"""
=========================================================
LeetCode 34 - Find First and Last Position of Element in Sorted Array
Difficulty: Medium
Pattern: Binary Search
=========================================================

Problem
-------
Given a sorted array of integers 'nums' sorted in non-decreasing order
and an integer 'target', find the starting and ending position of the
target value.

If the target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example
-------
Example 1:
Input:
nums = [5,7,7,8,8,10]
target = 8

Output:
[3,4]

---------------------------------------------------------

Example 2:
Input:
nums = [5,7,7,8,8,10]
target = 6

Output:
[-1,-1]

---------------------------------------------------------

Example 3:
Input:
nums = []
target = 0

Output:
[-1,-1]

---------------------------------------------------------

Key Idea
--------
A standard Binary Search stops as soon as the target is found.

In this problem, finding the target is not enough because there may be
multiple occurrences.

To find the complete range:

1. Run Binary Search once to find the FIRST occurrence.
   - Save the index.
   - Continue searching toward the left.

2. Run Binary Search again to find the LAST occurrence.
   - Save the index.
   - Continue searching toward the right.

Finally return:
[first_occurrence, last_occurrence]

---------------------------------------------------------

Approach
--------
1. Create a helper function to find the first occurrence.
   - Perform Binary Search.
   - When the target is found:
        • Save the current index.
        • Continue searching the left half.

2. Create another helper function to find the last occurrence.
   - Perform Binary Search.
   - When the target is found:
        • Save the current index.
        • Continue searching the right half.

3. Return both indices as a list.

---------------------------------------------------------

Algorithm
---------
Find First Occurrence

- Initialize:
      left = 0
      right = len(nums) - 1
      answer = -1

- While left <= right:
      Calculate mid.

      If nums[mid] == target:
            Save answer.
            Continue searching LEFT.

      Else if nums[mid] < target:
            Search RIGHT.

      Else:
            Search LEFT.

---------------------------------------------------------

Find Last Occurrence

- Initialize:
      left = 0
      right = len(nums) - 1
      answer = -1

- While left <= right:
      Calculate mid.

      If nums[mid] == target:
            Save answer.
            Continue searching RIGHT.

      Else if nums[mid] < target:
            Search RIGHT.

      Else:
            Search LEFT.

---------------------------------------------------------

Time Complexity
---------------
O(log n)

Binary Search is performed twice.

O(log n) + O(log n)

Simplifies to:

O(log n)

---------------------------------------------------------

Space Complexity
----------------
O(1)

Only a few variables are used.

---------------------------------------------------------

Key Takeaways
-------------
- Binary Search can be modified to find boundaries instead of stopping
  immediately.
- Continue searching after finding the target.
- Search left to find the first occurrence.
- Search right to find the last occurrence.
- Running Binary Search twice still results in O(log n) complexity.

=========================================================
"""

class Solution(object):
    def searchRange(self, nums, target):

        def findFirst(nums, target):
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    answer = mid
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return answer

        def findLast(nums, target):
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    answer = mid
                    left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return answer

        first = findFirst(nums, target)
        last = findLast(nums, target)

        return [first, last]