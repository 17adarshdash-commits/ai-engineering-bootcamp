"""
LeetCode: 704
Title: Binary Search

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
Scan the array from left to right until the target is found.

Why it is not optimal:
- Checks every element in the worst case.
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ==========================================================

class Solution(object):
    def search(self, nums, target):
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

        return -1


"""
What I Learned
--------------

1. Binary Search works only on sorted data.

2. Compare the middle element with the target.

3. If the target is larger, search the right half.

4. If the target is smaller, search the left half.

5. Repeating this process cuts the search space in half each time.

6. Time complexity improves from O(n) to O(log n).
"""


"""
Pattern Recognition
-------------------

Use Binary Search when:

- The data is sorted.
- You need to search for an element or its position.
- You can eliminate half of the search space after each comparison.
"""