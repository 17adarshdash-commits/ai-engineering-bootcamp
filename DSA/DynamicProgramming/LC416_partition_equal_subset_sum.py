"""
Problem:
416. Partition Equal Subset Sum

Difficulty:
Medium

Pattern:
Dynamic Programming
0/1 Knapsack (Subset Sum)

Problem:
Given an integer array nums, return true if nums can be partitioned into
two subsets such that the sum of the elements in both subsets is equal,
or false otherwise.

Example 1:

Input:
nums = [1,5,11,5]

Output:
true

Explanation:
The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input:
nums = [1,2,3,5]

Output:
false

Explanation:
The array cannot be partitioned into equal sum subsets.

Key Idea:
If the two subsets have equal sums, each must sum to total / 2. So the
question "can nums be split into two equal-sum halves?" reduces to "does
some subset of nums sum to exactly total / 2?" - that's the classic 0/1
knapsack decision problem: pick a subset of items (each used at most
once) that hits a target sum.

Two things fall out of that reduction immediately:
- If total is odd, no integer target works - return False without
  computing anything.
- The other subset is whatever's left over, so only one target
  (total // 2) needs to be reachable; its complement is automatically
  reachable too (total - target = target).

dp[s] tracks whether sum s is reachable using a subset of the numbers
processed so far. Each num either goes into the subset or doesn't, which
is why the inner loop runs from high sums down to low: updating dp[s]
from dp[s - num] while iterating downward ensures num is considered at
most once per pass (updating upward would let the same num contribute
to dp[s] multiple times, which is the unbounded-knapsack behavior, not
0/1).

Approach (Bottom-Up, O(n * target) time):
1. Compute total = sum(nums). If total is odd, return False - an odd
   total can't split into two equal integer halves.
2. Let target = total // 2.
3. dp[s] = True if some subset of nums seen so far sums to exactly s.
   Initialize dp[0] = True (the empty subset always sums to 0), all
   other dp[s] = False.
4. For each num in nums, update dp from target down to num (0/1
   knapsack - iterate s downward so num isn't reused within one pass):
       for s in range(target, num - 1, -1):
           dp[s] = dp[s] or dp[s - num]
   Early-exit the moment dp[target] becomes True - no need to keep
   scanning once the answer is known.
5. Return dp[target].

Algorithm:
- total = sum(nums)
- if total % 2 != 0: return False
- target = total // 2
- dp = [True] + [False] * target
- for num in nums:
      for s in range(target, num - 1, -1):
          if dp[s - num]:
              dp[s] = True
      if dp[target]: return True
- return dp[target]

Time Complexity:
O(n * target) where n = len(nums) and target = total(nums) // 2

Space Complexity:
O(target) for the dp array

Key Takeaways:
- "Split into two equal-sum groups" reduces to "does some subset hit
  total // 2?" - the same reduction trick (turn a partition question
  into a single subset-sum target) shows up across this whole family of
  problems.
- This is the decision-problem sibling of Target Sum (LC 494): same
  0/1 knapsack shape and same downward-iterating inner loop, but
  tracking a boolean "reachable?" per sum instead of a count of ways to
  reach it.
- The odd-total check is a free early exit, not just tidiness - without
  it, target would truncate to a value that can never actually
  represent an equal split.
"""

from typing import List


def can_partition(nums: List[int]) -> bool:
    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2

    dp = [True] + [False] * target
    for num in nums:
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True
        if dp[target]:
            return True

    return dp[target]


if __name__ == "__main__":
    tests = [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([1, 2, 5], False),
        ([1, 1], True),
        ([100], False),
        ([2, 2, 1, 1], True),
    ]

    for nums, expected in tests:
        result = can_partition(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] can_partition({nums}) = {result} (expected {expected})")
