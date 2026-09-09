"""
LeetCode: 88
Title: Merge Sorted Array

Difficulty: Easy

Pattern:
- Two Pointers (from the end)

Topics:
- Array
- Two Pointers
- Sorting
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n + m)
# Space Complexity: O(1)
# ==========================================================

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1       # last actual element in nums1
        j = n - 1       # last element in nums2
        k = m + n - 1   # last position in nums1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


"""
What I Learned
--------------

1. Merging from the back avoids overwriting values in nums1 that
   haven't been compared yet — merging from the front would require
   shifting elements around.

2. Three pointers are needed:
   - i tracks the last real element in nums1
   - j tracks the last element in nums2
   - k tracks the last open slot in nums1 (the write position)

3. Once nums2 is exhausted (j < 0), nums1 is already correctly
   merged, so the loop can stop — no need to keep copying
   remaining nums1 elements, they're already in place.

4. If nums1 runs out first (i < 0) but nums2 still has elements,
   just keep copying from nums2 — that's why the condition checks
   `i >= 0` before comparing.

5. Working in-place from the end achieves O(1) extra space,
   compared to the naive approach of merging into a new array.
"""


"""
Pattern Recognition
-------------------

Use Two Pointers (from the end) when:

- Merging two sorted arrays/lists in-place.
- One array has extra trailing space to hold the merged result.
- Writing from the back avoids overwriting unprocessed data.
- Comparable to "merge step" of merge sort, but in-place.
"""
