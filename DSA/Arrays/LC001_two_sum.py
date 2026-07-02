"""
LeetCode 1 - Two Sum

Pattern:
- Brute Force

Difficulty:
- Easy
"""

# ==========================================================
# Brute Force Solution
# Time Complexity: O(n²)
# Space Complexity: O(1)
# ==========================================================

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


"""
What I Learned
--------------

1. I learned how to compare every possible pair of elements.

2. I learned that nested loops usually result in O(n²) time complexity.

3. LeetCode expected a list [i, j], not a set {i, j}.

4. This solution is correct but not optimal.

Next Improvement:
- Solve using a HashMap to achieve O(n) time complexity.
"""