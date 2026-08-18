"""
Problem:
152. Maximum Product Subarray

Difficulty:
Medium

Pattern:
Dynamic Programming
Bottom-Up (Tabulation) - Track Both Max and Min

Problem:
Given an integer array nums, find a subarray that has the largest
product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit
integer.

Example 1:

Input:
nums = [2,3,-2,4]

Output:
6

Explanation:
[2,3] has the largest product 6.

Example 2:

Input:
nums = [-2,0,-1]

Output:
0

Explanation:
The result cannot be 2, because [-2,-1] is not a subarray.

Key Idea:
This looks like Maximum Subarray (Kadane's), but "+" and "max" don't
compose the same way "*" and "max" do. With addition, extending a
negative running sum is never beneficial, so only the running max needs
tracking. With multiplication, a large *negative* running product can
flip into the new maximum the moment it's multiplied by another negative
number - so throwing away a negative running product loses information
the next element might need.

The fix is to track two running values at each index: the max product
ending here, and the min product ending here. A negative num[i] swaps
the roles of the incoming max and min (multiplying by a negative number
turns the largest product into the smallest, and vice versa), so
swapping them before combining with num[i] handles that flip uniformly
instead of branching on sign. At each index, both running values are
also compared against starting fresh at num[i] alone - exactly like
Kadane's "extend vs. restart" choice, since a very negative running
product can be worse than restarting even for the min track.

Approach (Bottom-Up, O(n) time):
1. Handle the trivial case: an empty nums has no subarray, return 0.
2. Initialize cur_max and cur_min to nums[0], and result to nums[0] -
   the running max/min product ending at the first element, and the
   best product seen so far, both seeded from the single-element
   subarray.
3. For each subsequent num:
   a. If num is negative, swap cur_max and cur_min - multiplying by a
      negative number flips which one becomes the larger product.
   b. cur_max = max(num, cur_max * num) - either restart the subarray at
      num, or extend the previous best running product.
   c. cur_min = min(num, cur_min * num) - the mirror update, tracking
      the most negative running product (the one that could flip large
      on the next negative number).
   d. result = max(result, cur_max) - cur_max is the best product ending
      at the current index, so it's a candidate for the overall best.
4. Return result.

Algorithm:
- if not nums: return 0
- cur_max = cur_min = result = nums[0]
- for num in nums[1:]:
      if num < 0: cur_max, cur_min = cur_min, cur_max
      cur_max = max(num, cur_max * num)
      cur_min = min(num, cur_min * num)
      result = max(result, cur_max)
- return result

Time Complexity:
O(n) - one pass over nums.

Space Complexity:
O(1) - only a constant number of running values are kept.

Key Takeaways:
- Multiplication doesn't share addition's "negative running total is
  always useless" property - a very negative running product is
  actually valuable information, because the next negative number can
  turn it into the new best.
- Whenever an operation's effect depends on the sign of the next input
  (multiplication flipping max/min), tracking both extremes and letting
  a swap absorb the sign flip is simpler than branching on sign inside
  the update itself.
- The "extend vs. restart" choice from Kadane's still applies here, just
  applied to two running values (max and min) instead of one.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        cur_max = cur_min = result = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)

            result = max(result, cur_max)

        return result
