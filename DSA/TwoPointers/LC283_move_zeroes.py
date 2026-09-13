"""
LeetCode: 283
Title: Move Zeroes

Difficulty: Easy

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
    def moveZeroes(self, nums):
        insert_pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1


"""
What I Learned
--------------

1. `insert_pos` tracks the next slot where a non-zero element belongs.

2. Walk through the array once with `i`. Whenever nums[i] is non-zero,
   swap it into `insert_pos` and advance `insert_pos`.

3. Zeroes naturally get pushed toward the end because they're the
   elements left behind by the swaps.

4. Swapping (instead of just overwriting) modifies the array in-place
   without needing extra space for a copy.

5. Relative order of non-zero elements is preserved because we only
   ever swap a non-zero element into position — we never reorder two
   non-zero elements relative to each other.
"""


"""
Pattern Recognition
-------------------

Use Two Pointers when:

- Partitioning an array in-place based on a condition (zero/non-zero,
  even/odd, etc.).
- Need O(1) space and O(n) time.
- One pointer scans the array, another tracks where the next "kept"
  element should go.
"""
