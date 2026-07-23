"""
=========================================================
LeetCode 33 - Search in Rotated Sorted Array
Difficulty: Medium
Pattern: Binary Search
=========================================================

Problem
-------
Given a rotated sorted array and a target value,
return the index of the target if it exists.
Otherwise return -1.

Example
-------
Input:
nums = [4,5,6,7,0,1,2]
target = 0

Output:
4

---------------------------------------------------------

Key Idea
--------
A rotated sorted array always has one half that is sorted.

1. Find the middle element.
2. Determine which half is sorted.
3. Check if the target lies within the sorted half.
4. Discard the other half.
5. Repeat until the target is found.

---------------------------------------------------------

Approach
--------
1. Initialize left and right pointers.
2. Calculate the middle index.
3. If nums[mid] equals target, return mid.
4. If the left half is sorted:
      - Check whether the target lies inside it.
      - Search left or right accordingly.
5. Otherwise, the right half is sorted:
      - Check whether the target lies inside it.
      - Search accordingly.
6. Return -1 if the target is not found.

---------------------------------------------------------

Time Complexity
---------------
O(log n)

Space Complexity
----------------
O(1)

---------------------------------------------------------

Key Takeaways
-------------
- A rotated sorted array always has one sorted half.
- Identify the sorted half first.
- Check if the target lies within the sorted half.
- Eliminate half of the search space every iteration.
"""

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1