"""
LeetCode: 1480
Title: Running Sum of 1D Array

Difficulty: Easy

Pattern:
- Prefix Sum

Topics:
- Arrays
- Prefix Sum
"""

# ==========================================================
# Brute Force Idea
# Time Complexity: O(n²)
# Space Complexity: O(n)
# ==========================================================

"""
For every index i:

Calculate:
sum(nums[0:i+1])

Append the result to the output list.

This repeatedly recalculates the same sums,
making it inefficient.
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================================

class Solution(object):
    def runningSum(self, nums):
        out = []
        running = 0

        for num in nums:
            running += num
            out.append(running)

        return out


"""
What I Learned
--------------

1. Prefix Sum stores the cumulative sum while traversing the array.

2. Instead of recalculating sums repeatedly,
   keep updating a running total.

3. Each new prefix sum equals:

   previous_prefix_sum + current_element

4. Prefix Sum avoids unnecessary repeated calculations.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


"""
Pattern Recognition
-------------------

Use Prefix Sum when:

- The problem asks for cumulative sums.
- You need the sum of subarrays frequently.
- You want to avoid repeatedly calling sum().

Common phrases:

- Running Sum
- Prefix Sum
- Sum of Range
- Cumulative Sum
"""