"""
Problem:
213. House Robber II

Difficulty:
Medium

Pattern:
Dynamic Programming
Bottom-Up (Tabulation)

Problem:
You are a professional robber planning to rob houses along a street. The
houses are arranged in a circle - the first house is adjacent to the last
one. Each house has a certain amount of money stashed, and adjacent houses
have connected security systems, so robbing two adjacent houses on the same
night trips the alarm.

Given an integer array nums representing the amount of money at each house,
return the maximum amount of money you can rob tonight without robbing two
adjacent houses.

Example 1:

Input:
nums = [2, 3, 2]

Output:
3

Explanation:
Robbing house 0 (money = 2) and house 2 (money = 2) is not allowed because
they are adjacent in the circle (house 0 and house 2 are neighbors). The
best option is house 1 alone, total = 3.

Example 2:

Input:
nums = [1, 2, 3, 1]

Output:
4

Explanation:
Rob house 0 (money = 1) and house 2 (money = 3), total = 1 + 3 = 4.
House 0 and house 3 are adjacent here too, but neither is robbed, so
there's no conflict.

Example 3:

Input:
nums = [1, 2, 3]

Output:
3

Key Idea:
The only thing that makes this different from House Robber I is the wrap-
around adjacency between the first and last house - a plan can never
include both. That means any valid plan either excludes house 0 entirely
or excludes the last house entirely (possibly both, but never neither).
Those two cases no longer have a wrap-around constraint, so each is just a
plain House Robber I problem on a sub-array, and the answer is the better
of the two.

Approach (Bottom-Up, O(1) space):
1. Handle the trivial case: a single house has no neighbor conflict, so the
   answer is just its money.
2. Run the linear House Robber sweep (two running values, prev_two and
   prev_one) once over nums[0 : n-1] (excludes the last house).
3. Run the same sweep again over nums[1 : n] (excludes the first house).
4. Return the max of the two results - this covers every valid circular
   plan, since a plan either skips the first house, the last house, or
   both, and never neither.

Algorithm:
- if len(nums) == 1: return nums[0]
- def rob_linear(houses):
      prev_two, prev_one = 0, 0
      for money in houses:
          current = max(prev_one, prev_two + money)
          prev_two, prev_one = prev_one, current
      return prev_one
- return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

Time Complexity:
O(n)

Space Complexity:
O(1) auxiliary (the two slices are O(n) if you count the copies, but the
sweep itself only tracks two running values)

Key Takeaways:
- A circular constraint is often solvable by reducing it to two (or more)
  linear sub-problems that each avoid the wrap-around, then combining their
  results - here, "exclude house 0" and "exclude the last house" together
  cover every valid arrangement.
- The linear sweep itself is unchanged from House Robber I; the new logic
  is entirely in how the two sub-problems are set up and combined.
- The single-house edge case must be handled separately, since slicing it
  down to an empty sub-array on either side would incorrectly return 0.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev_two = 0
            prev_one = 0

            for money in houses:
                current = max(prev_one, prev_two + money)
                prev_two = prev_one
                prev_one = current

            return prev_one

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
