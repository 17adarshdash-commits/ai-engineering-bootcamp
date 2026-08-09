"""
Problem:
746. Min Cost Climbing Stairs

Difficulty:
Easy

Pattern:
Dynamic Programming
Bottom-Up (Tabulation)

Problem:
You are given an integer array cost where cost[i] is the cost of the i-th
step on a staircase. Once you pay the cost, you can either climb one or two
steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor (one step past the
last index of cost).

Example 1:

Input:
cost = [10, 15, 20]

Output:
15

Explanation:
Start at index 1, pay 15, then climb two steps to reach the top.

Example 2:

Input:
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

Output:
6

Explanation:
Start at index 0, pay 1, then climb two steps repeatedly, skipping the
expensive 100-cost steps: 1 + 1 + 1 + 1 + 1 + 1 = 6.

Key Idea:
The minimum cost to stand on step i is the cost of that step plus the
cheaper of the two ways to have arrived there: from one step back or two
steps back. Since only the last two computed costs are ever needed, the
full result can be built bottom-up while keeping just two running values.

Approach (Bottom-Up, O(1) space):
1. The top of the staircase is one step past the last index, so it can be
   reached from either of the last two steps - there's no fixed base cost
   at the top itself.
2. Track the minimum cost to stand on each of the last two steps
   (two_steps_back, one_step_back), seeded with cost[0] and cost[1].
3. For each step i from 2 onward, compute the cheapest cost to stand on
   it as cost[i] + min(one_step_back, two_steps_back), then slide the
   window forward.
4. The answer is the minimum of the costs to stand on the last two steps,
   since the top can be reached with a single or double step from either.

Algorithm:
- two_steps_back, one_step_back = cost[0], cost[1]
- for i in range(2, len(cost)):
      current_cost = cost[i] + min(one_step_back, two_steps_back)
      two_steps_back, one_step_back = one_step_back, current_cost
- return min(one_step_back, two_steps_back)

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- The answer isn't cost[n-1] plus the minimum of the last two - the top is
  a virtual step past the array, so the final result must compare both of
  the last two standing costs, not just take one of them.
- Like Fibonacci-style DP, only the previous two subproblem results are
  ever needed, so two variables replace a full DP array (space-optimized
  tabulation).
- Choosing to start at index 0 or 1 is handled naturally by seeding both
  base cases up front rather than picking one.
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        two_steps_back = cost[0]
        one_step_back = cost[1]

        for i in range(2, len(cost)):
            current_cost = cost[i] + min(one_step_back, two_steps_back)
            two_steps_back = one_step_back
            one_step_back = current_cost

        return min(one_step_back, two_steps_back)
