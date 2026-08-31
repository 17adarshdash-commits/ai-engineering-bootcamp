"""
Problem:
152. Maximum Product Subarray

Difficulty:
Medium

Pattern:
Dynamic Programming
Kadane's Algorithm Variant - Track Max AND Min

Problem:
Given an integer array nums, find a subarray that has the largest
product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit
integer.

Example 1:

Input:
nums = [2, 3, -2, 4]

Output:
6

Explanation:
[2, 3] has the largest product 6.

Example 2:

Input:
nums = [-2, 0, -1]

Output:
0

Explanation:
The result cannot be 2, because [-2, -1] is not a subarray - 0 sits
between them, splitting it into two separate subarrays.

Key Idea:
This looks like Kadane's Algorithm (max sum subarray), but
multiplication breaks the "extend or restart" rule that works for sums:
a large negative product can flip into the best positive product if
multiplied by one more negative number. Tracking only a running max (as
plain Kadane's does) loses that information the moment a negative
number shows up.

The fix: track two running values ending at each index, not one -
current_max (the best/most positive product of a subarray ending here)
and current_min (the worst/most negative product ending here). The
current_min matters because a very negative product, multiplied by a
future negative number, can become the new current_max.

At each new number n:
- If n is negative, multiplying by n flips sign: whatever was the max
  ending at i-1 could become the min ending at i, and whatever was the
  min could become the max. Swap current_max and current_min before
  computing the new values, so the same two lines of code handle both
  the positive and negative case.
- current_max = max(n, current_max * n) - either start fresh at this
  index, or extend the previous best.
- current_min = min(n, current_min * n) - the mirror image, tracking
  the worst case in case a future negative flips it back to useful.
- The overall answer is the largest current_max seen across every
  index, since the best subarray doesn't have to end at the last
  element.

Approach (O(n) time, O(1) space):
1. Initialize result, current_max, current_min all to nums[0].
2. For each subsequent number n in nums[1:]:
   a. If n < 0: swap current_max and current_min.
   b. current_max = max(n, current_max * n)
   c. current_min = min(n, current_min * n)
   d. result = max(result, current_max)
3. Return result.

Algorithm:
- result = current_max = current_min = nums[0]
- for n in nums[1:]:
      if n < 0:
          current_max, current_min = current_min, current_max
      current_max = max(n, current_max * n)
      current_min = min(n, current_min * n)
      result = max(result, current_max)
- return result

Time Complexity:
O(n) - a single pass over the array.

Space Complexity:
O(1) - only a constant number of running variables are kept.

Key Takeaways:
- Whenever a running value can flip sign on multiplication, track both
  a running max AND a running min - the min is "useless" until a
  negative number turns it into the new max.
- Swapping current_max/current_min before recomputing on a negative
  number is what lets one pair of formulas cover both the "n is
  positive" and "n is negative" cases without branching further.
- Same "extend or restart" instinct as Kadane's (max(n, running * n)
  restarts at n if the running product isn't helping), just carried
  through two tracked values instead of one.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = current_max = current_min = nums[0]

        for n in nums[1:]:
            if n < 0:
                current_max, current_min = current_min, current_max

            current_max = max(n, current_max * n)
            current_min = min(n, current_min * n)

            result = max(result, current_max)

        return result
