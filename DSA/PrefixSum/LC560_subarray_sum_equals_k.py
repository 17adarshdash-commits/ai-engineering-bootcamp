"""
LeetCode: 560
Title: Subarray Sum Equals K

Difficulty: Medium

Pattern:
- Prefix Sum
- Hash Map

Topics:
- Arrays
- Prefix Sum
- Hash Map
"""

# ==========================================================
# Brute Force Idea
# Time Complexity: O(n²)
# Space Complexity: O(1)
# ==========================================================

"""
Start from every index.

Keep adding elements until the end.

Whenever the running sum equals k,
increase the answer.

This checks every possible subarray.
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================================

class Solution(object):
    def subarraySum(self, nums, k):
        cnt = 0
        running = 0
        prefix = {0: 1}

        for num in nums:
            running += num
            target = running - k

            if target in prefix:
                cnt += prefix[target]

            if running in prefix:
                prefix[running] += 1
            else:
                prefix[running] = 1

        return cnt


"""
What I Learned
--------------

1. Prefix Sum can be combined with a Hash Map.

2. The Hash Map stores:
   Prefix Sum -> Frequency

3. At every index:
   target = running - k

4. If target exists,
   then a valid subarray has been found.

5. After checking,
   store the current Prefix Sum for future iterations.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


"""
Pattern Recognition
-------------------

Use this pattern when:

- Finding subarrays with a given sum.
- Multiple Prefix Sums are involved.
- Fast lookup of previous Prefix Sums is needed.

Common interview phrases:

- Subarray Sum
- Prefix Sum
- Hash Map
- Running Sum
- Frequency Map
"""