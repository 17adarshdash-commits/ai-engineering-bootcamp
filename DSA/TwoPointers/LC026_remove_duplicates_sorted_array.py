"""
LeetCode: 26
Title: Remove Duplicates from Sorted Array

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
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        write = 0

        for read in range(1, len(nums)):
            if nums[write] != nums[read]:
                write += 1
                nums[write] = nums[read]

        return write + 1


"""
What I Learned
--------------

1. When an array is sorted, duplicate elements are adjacent.

2. Two Pointers can be used to overwrite duplicate values with the
   next unique value.

3. The write pointer tracks the position of the last unique element.

4. The read pointer scans the array for new unique elements.

5. Since indexing starts from 0, the number of unique elements is
   write + 1.

6. Handle the edge case where the array is empty by returning 0.
"""


"""
Pattern Recognition
-------------------

Use Two Pointers when:

- The array is sorted.
- You need to remove or compress duplicate values.
- You need to modify an array in-place.
- One pointer reads while another pointer writes.
"""