"""
LeetCode: 643
Title: Maximum Average Subarray I

Difficulty: Easy

Pattern:
- Sliding Window

Topics:
- Array
- Sliding Window
"""

# ==========================================================
# Brute Force Idea
# Time Complexity: O(n*k)
# Space Complexity: O(1)
# ==========================================================

"""
Calculate the sum of every subarray of size k from scratch.
Keep track of the maximum sum and divide it by k at the end.

Why it is not optimal:
- Recalculates the same elements repeatedly.
- Inefficient for large arrays.
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================================

class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(len(nums) - k):
            window_sum = window_sum - nums[i] + nums[i + k]

            if window_sum > max_sum:
                max_sum = window_sum

        return float(max_sum) / k


"""
What I Learned
--------------

1. Sliding Window is useful for problems involving consecutive elements.

2. Calculate the first window only once.

3. As the window moves:
   - Remove the element leaving the window.
   - Add the element entering the window.

4. Reusing the previous window's sum avoids unnecessary calculations.

5. Time complexity improves from O(n*k) to O(n).

6. In Python 2, divide using float(max_sum) / k to avoid integer division.
"""


"""
Pattern Recognition
-------------------

Use Sliding Window when:

- The problem involves consecutive elements.
- The window size is fixed.
- You need the maximum, minimum, average, or sum of a subarray.
- The next window can be derived from the previous one by removing one element and adding another.
"""