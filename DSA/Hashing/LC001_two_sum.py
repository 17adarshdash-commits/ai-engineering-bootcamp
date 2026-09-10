"""
LeetCode: 1
Title: Two Sum

Difficulty: Easy

Pattern:
- Hashing

Topics:
- Array
- Hash Table
"""

# ==========================================================
# Brute Force Solution
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# ==========================================================

class BruteForceSolution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


# ==========================================================
# Optimized Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================================

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


"""
What I Learned
--------------

1. Brute force checks every pair, which is O(n^2) - too slow for large inputs.

2. Key question while iterating: "What number do I need to have already
   seen to make the current number reach the target?" That number is
   target - nums[i] (the complement).

3. A hash map lets us check "have I seen the complement?" in O(1) time,
   instead of scanning the rest of the array.

4. Only one pass is needed: for each number, first check if its
   complement is already in the map, THEN add the current number to
   the map. This also naturally avoids using the same element twice.

5. Trade-off: we use O(n) extra space (the hash map) to bring time
   down from O(n^2) to O(n).
"""


"""
Pattern Recognition
-------------------

Use a Hash Map when:

- You need to find a pair (or check existence) that satisfies some
  condition (sum, difference, etc.) involving array elements.
- You want O(1) average lookup instead of scanning/nested loops.
- The array is NOT sorted (if it were sorted, Two Pointers is often
  a good fit with O(1) space instead).
"""


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))       # [1, 2]
    print(sol.twoSum([3, 3], 6))          # [0, 1]
