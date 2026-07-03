"""
LeetCode: 167
Title: Two Sum II - Input Array Is Sorted

Difficulty: Medium

Pattern:
- Two Pointers

Topics:
- Array
- Two Pointers
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================================

class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum < target:
                l += 1
            elif current_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]


"""
What I Learned
--------------

1. When an array is sorted, Two Pointers can often replace nested loops.

2. If the current sum is too small, move the left pointer right.

3. If the current sum is too large, move the right pointer left.

4. Two Pointers reduced the time complexity from O(n²) to O(n).

5. Always read the problem carefully. This problem requires
   returning 1-indexed positions.
"""


"""
Pattern Recognition
-------------------

Use Two Pointers when:

- The array is sorted.
- Searching for a pair with a target sum.
- Comparing elements from both ends.
- Optimizing a brute-force nested loop solution.
"""