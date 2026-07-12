"""
LeetCode: 374
Title: Guess Number Higher or Lower

Difficulty: Easy

Pattern:
- Binary Search

Topics:
- Binary Search
"""

# ==========================================================
# Brute Force Idea
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================================

"""
Start guessing from version 1 up to n.

For every guess:
    - Call guess(number).

If guess(number) returns 0,
that number is the answer.

Worst Case:
The picked number is n, so we check every number.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ==========================================================

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            result = guess(mid)

            if result == 1:
                left = mid + 1

            elif result == -1:
                right = mid - 1

            else:
                return mid

        return -1


"""
What I Learned
--------------

1. Binary Search can be applied even when we don't have direct
   access to the answer.

2. Instead of comparing array values, we use the guess() API
   to decide which half to search.

3. If guess(mid) returns:
      1  -> Search the right half.
     -1  -> Search the left half.
      0  -> Found the answer.

4. Storing guess(mid) in a variable avoids calling the API
   multiple times.

5. Binary Search reduces the search space by half
   after every iteration.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""


"""
Pattern Recognition
-------------------

Use Binary Search when:

1. The search space is sorted.

2. Every comparison lets you eliminate half of the
   remaining search space.

3. The problem gives directional feedback such as:
   - Higher
   - Lower
   - Too Small
   - Too Large
   - Left
   - Right

4. The answer can be found by repeatedly narrowing
   the search interval.
"""