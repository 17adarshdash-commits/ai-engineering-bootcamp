"""
LeetCode: 724
Title: Find Pivot Index

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
# Space Complexity: O(1)
# ==========================================================

"""
For every index:

Calculate:

Left Sum:
sum(nums[:i])

Right Sum:
sum(nums[i+1:])

If both sums are equal,
return the current index.

This repeatedly recalculates sums,
making the solution inefficient.
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================================

class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1


"""
What I Learned
--------------

1. Prefix Sum can eliminate repeated sum() calculations.

2. Instead of calculating left and right sums every iteration,
   maintain the left sum and derive the right sum.

3. Right Sum = Total Sum - Left Sum - Current Element

4. Check the pivot before updating left_sum.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


"""
Pattern Recognition
-------------------

Use Prefix Sum when:

- The problem involves cumulative sums.
- You need repeated range sum calculations.
- The array can be processed from left to right while maintaining running information.

Common interview phrases:

- Running Sum
- Prefix Sum
- Pivot Index
- Range Sum
- Equal Left and Right Sum
"""