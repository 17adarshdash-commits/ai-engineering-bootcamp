"""
Problem:
494. Target Sum

Difficulty:
Medium

Pattern:
Dynamic Programming
0/1 Knapsack (Subset Sum Counting)

Problem:
You are given an integer array nums and an integer target. You want to build
an expression out of nums by adding one of the symbols '+' and '-' before
each integer in nums and then concatenate all the integers.

Return the number of different expressions that evaluate to target.

Example 1:

Input:
nums = [1, 1, 1, 1, 1], target = 3

Output:
5

Explanation:
There are 5 ways to assign symbols to make the sum of nums be target 3:
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input:
nums = [1], target = 1

Output:
1

Key Idea:
Every number gets a '+' or a '-', which splits nums into two groups: a
"positive" group P (numbers kept positive) and a "negative" group N
(numbers made negative). If S is the total sum of nums:

    sum(P) - sum(N) = target
    sum(P) + sum(N) = S

Adding these two equations:

    2 * sum(P) = target + S
    sum(P) = (target + S) / 2

So the problem reduces to: how many subsets of nums sum to
subset_sum = (target + S) / 2? That's the classic 0/1 knapsack "count the
number of subsets with a given sum" problem, the counting cousin of the
Partition Equal Subset Sum decision problem.

Two edge cases make it "no ways":
- (target + S) must be even (otherwise subset_sum isn't an integer - no
  combination of +/- can split an odd total that way).
- abs(target) > S is impossible (even every number "+" doesn't reach it), so
  subset_sum would be negative or unreachable.

Approach (Bottom-Up, O(n * subset_sum) time):
1. Compute S = sum(nums). If (S + target) is odd or abs(target) > S, return
   0 - no valid split exists.
2. Let subset_sum = (S + target) // 2.
3. dp[s] = number of ways to pick a subset of nums seen so far that sums to
   s. Initialize dp[0] = 1 (the empty subset sums to 0 in exactly one way),
   dp[s] = 0 for s > 0.
4. For each num in nums, update dp from high sums to low (0/1 knapsack -
   each number used at most once, so iterate s downward to avoid reusing
   the same number twice in one pass):
       for s in range(subset_sum, num - 1, -1):
           dp[s] += dp[s - num]
5. Return dp[subset_sum].

Algorithm:
- total = sum(nums)
- if (total + target) % 2 != 0 or abs(target) > total: return 0
- subset_sum = (total + target) // 2
- dp = [1] + [0] * subset_sum
- for num in nums:
      for s in range(subset_sum, num - 1, -1):
          dp[s] += dp[s - num]
- return dp[subset_sum]

Time Complexity:
O(n * subset_sum) where n = len(nums)

Space Complexity:
O(subset_sum) for the dp array

Key Takeaways:
- Turning a "+/- assignment" problem into a subset-sum-counting problem via
  a bit of algebra (P - N = target, P + N = S) is the key insight - once
  that reduction is made, it's the same 0/1 knapsack shape as Coin Change,
  except counting combinations instead of minimizing coins used, and the
  "used at most once" constraint means the inner loop runs downward instead
  of upward (each num can only ever contribute to one subset membership,
  never be reused within the same pass).
- The two early-exit checks (parity, magnitude) aren't just optimizations -
  without them subset_sum could be negative or fractional, which would
  either crash or silently produce a wrong answer.
"""

from typing import List


def find_target_sum_ways(nums: List[int], target: int) -> int:
    total = sum(nums)

    if (total + target) % 2 != 0 or abs(target) > total:
        return 0

    subset_sum = (total + target) // 2

    dp = [1] + [0] * subset_sum
    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[subset_sum]


if __name__ == "__main__":
    tests = [
        ([1, 1, 1, 1, 1], 3, 5),
        ([1], 1, 1),
        ([1], 2, 0),
        ([0, 0, 0, 0, 0, 0, 0, 0, 1], 1, 256),
        ([100], -200, 0),
    ]

    for nums, target, expected in tests:
        result = find_target_sum_ways(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] find_target_sum_ways({nums}, {target}) = {result} (expected {expected})")
