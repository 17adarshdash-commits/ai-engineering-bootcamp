"""
LeetCode 217 - Contains Duplicate

Pattern:
- Hash Set

Difficulty:
- Easy
"""

# ==========================================================
# Brute Force Solution
# Time Complexity: O(n²)
# Space Complexity: O(1)
# ==========================================================

class SolutionBruteForce(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# ==========================================================
# Optimized Solution (Hash Set)
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================================

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
    
"""
What I Learned
--------------

1. A correct solution is not always an efficient solution.

2. Sets provide approximately O(1) lookup time.

3. Using extra memory can significantly reduce runtime.

4. When I only need to know whether an item has been seen before,
   a set is often the right data structure.
"""