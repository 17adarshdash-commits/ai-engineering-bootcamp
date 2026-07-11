"""
LeetCode: 278
Title: First Bad Version

Difficulty: Easy

Pattern:
- Binary Search
- Binary Search on Answer / Boundary

Topics:
- Binary Search
"""

# ==========================================================
# Brute Force Idea
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================================

"""
Start from version 1 and check every version one by one.

The first version for which isBadVersion(version)
returns True is the answer.

Why it is not optimal:
- In the worst case, every version has to be checked.
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ==========================================================

# The isBadVersion API is already defined for you.
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low


"""
What I Learned
--------------

1. Binary Search is not only used to search for values.

2. It can also find the first position where a condition changes.

3. If the middle version is bad, continue searching the left half.

4. If the middle version is good, continue searching the right half.

5. When the loop ends, 'low' points to the first bad version.

6. Time Complexity: O(log n)

7. Space Complexity: O(1)
"""


"""
Pattern Recognition
-------------------

Use this Binary Search pattern when:

- The answer changes from False to True.
- You need to find the first occurrence of a condition.
- You need to find the leftmost valid answer.
- The search space is monotonic (once True, always True).
"""