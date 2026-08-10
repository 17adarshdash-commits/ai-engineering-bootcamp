"""
Problem:
198. House Robber

Difficulty:
Medium

Pattern:
Dynamic Programming
Bottom-Up (Tabulation)

Problem:
You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, but adjacent houses have
connected security systems - if two adjacent houses are broken into on the
same night, the alarm goes off.

Given an integer array nums representing the amount of money at each house,
return the maximum amount of money you can rob tonight without robbing two
adjacent houses.

Example 1:

Input:
nums = [1, 2, 3, 1]

Output:
4

Explanation:
Rob house 0 (money = 1) and house 2 (money = 3), total = 1 + 3 = 4.

Example 2:

Input:
nums = [2, 7, 9, 3, 1]

Output:
12

Explanation:
Rob house 0 (money = 2), house 2 (money = 9), and house 4 (money = 1),
total = 2 + 9 + 1 = 12.

Key Idea:
At every house there are exactly two choices: rob it (and add its money to
the best total that excludes the previous house), or skip it (and keep the
best total already found up to the previous house). The best result at
house i is therefore the max of those two choices, and since that decision
only ever depends on the best results at the two preceding houses, the
whole array can be swept with two running values instead of an array.

Approach (Bottom-Up, O(1) space):
1. Track the best amount obtainable considering houses up to two houses
   back (prev_two) and up to one house back (prev_one), both seeded at 0
   for an empty prefix.
2. For each house's money, compute the best amount through that house as
   max(prev_one, prev_two + money) - either skip it and keep prev_one, or
   rob it on top of the best total that stopped before the adjacent house.
3. Slide the window forward: prev_two becomes the old prev_one, prev_one
   becomes the newly computed amount.
4. After processing every house, prev_one holds the answer.

Algorithm:
- prev_two, prev_one = 0, 0
- for money in nums:
      current = max(prev_one, prev_two + money)
      prev_two, prev_one = prev_one, current
- return prev_one

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- This is the same "include current vs. exclude current" decision as
  Min Cost Climbing Stairs, but framed as a maximization over money instead
  of a minimization over cost.
- Only the previous two subproblem results are ever needed, so two
  variables replace a full DP array (space-optimized tabulation).
- Seeding both running values at 0 correctly handles the base cases of
  "no houses robbed yet" without special-casing the first one or two
  houses.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev_two = 0
        prev_one = 0

        for money in nums:
            current = max(prev_one, prev_two + money)
            prev_two = prev_one
            prev_one = current

        return prev_one
