"""
LeetCode: 303
Title: Range Sum Query - Immutable

Difficulty: Easy

Pattern:
- Prefix Sum

Topics:
- Arrays
- Prefix Sum
"""

# ==========================================================
# Brute Force Idea
# Time Complexity: O(n) per query
# Space Complexity: O(1)
# ==========================================================

"""
Store the original array.

Whenever sumRange(left, right) is called:

Calculate:
sum(nums[left:right+1])

Since every query scans part of the array,
multiple queries become slow.
"""

# ==========================================================
# Optimized Solution
# Time Complexity:
#   __init__()  -> O(n)
#   sumRange()  -> O(1)
# Space Complexity: O(n)
# ==========================================================

class NumArray(object):

    def __init__(self, nums):
        running = 0
        prefix = []

        for num in nums:
            running += num
            prefix.append(running)

        self.prefix = prefix

    def sumRange(self, left, right):

        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]


"""
What I Learned
--------------

1. Some problems allow preprocessing.

2. Build the Prefix Sum array once inside __init__().

3. Store the Prefix Sum array inside the object using:
   self.prefix

4. Every future query can now be answered in O(1).

5. Formula:

If left == 0:
    answer = prefix[right]

Otherwise:
    answer = prefix[right] - prefix[left - 1]

Time Complexity:
__init__() : O(n)

sumRange() : O(1)

Space Complexity:
O(n)
"""


"""
Pattern Recognition
-------------------

Use Prefix Sum when:

- Multiple range sum queries are performed.
- The array does not change after creation.
- Preprocessing once can speed up future operations.

Common interview phrases:

- Range Sum Query
- Immutable Array
- Prefix Sum
- Preprocessing
- Many Queries
"""