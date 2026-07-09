"""
LeetCode: 35
Title: Search Insert Position

Difficulty: Easy

Pattern:
- Binary Search

Topics:
- Array
- Binary Search
"""

# ==========================================================
# Brute Force Idea
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================================

"""
Scan the array from left to right.

If the target is found, return its index.

If the current element becomes greater than the target,
return that index because the target should be inserted there.

If the loop finishes, insert the target at the end.
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ==========================================================

class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return low


"""
What I Learned
--------------

1. Binary Search only works on sorted arrays.

2. Compare the target with the middle element.

3. If the target is larger, search the right half.

4. If the target is smaller, search the left half.

5. If the target is not found, the final value of 'low'
   is the correct insertion position.

6. Binary Search reduces the search space by half every iteration.

7. Time complexity improves from O(n) to O(log n).
"""


"""
Pattern Recognition
-------------------

Use Binary Search when:

- The array is sorted.
- You need to search for an element.
- You need to find where an element should be inserted.
- You can eliminate half of the search space after each comparison.
"""