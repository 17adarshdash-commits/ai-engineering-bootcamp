"""
Problem:
300. Longest Increasing Subsequence

Difficulty:
Medium

Pattern:
Dynamic Programming

Problem:
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Example 1:

Input:
nums = [10, 9, 2, 5, 3, 7, 101, 18]

Output:
4

Explanation:
The longest increasing subsequence is [2, 3, 7, 101], therefore the
length is 4.

Example 2:

Input:
nums = [0, 1, 0, 3, 2, 3]

Output:
4

Example 3:

Input:
nums = [7, 7, 7, 7, 7, 7, 7]

Output:
1

Key Idea:
dp[i] = the length of the longest increasing subsequence that ends
exactly at index i (using nums[i] as its last element). For every index
i, look back at every earlier index j < i: if nums[j] < nums[i], then
nums[i] could extend whatever subsequence ends at j, giving a candidate
length of dp[j] + 1. dp[i] is the best (max) of all such candidates, or
1 on its own (nums[i] alone is always a valid subsequence of length 1)
if no earlier element is smaller. This is the same "look back at every
earlier sub-problem and take the best" shape as Coin Change, except the
lookback here is over array positions rather than coin denominations,
and the transition is guarded by an increasing condition instead of
being unconditional.

Approach (Bottom-Up, O(n^2) time):
1. Build a dp array of size n, seeded with 1 everywhere - every single
   element is trivially an increasing subsequence of length 1 on its own.
2. For each index i from 1 to n - 1, check every earlier index j from 0
   to i - 1: whenever nums[j] < nums[i], nums[i] can extend the
   subsequence ending at j, so dp[i] = max(dp[i], dp[j] + 1).
3. The answer is the maximum value anywhere in dp, since the longest
   increasing subsequence can end at any index, not necessarily the
   last one.

Algorithm:
- dp = [1] * n
- for i in range(1, n):
      for j in range(i):
          if nums[j] < nums[i]:
              dp[i] = max(dp[i], dp[j] + 1)
- return max(dp)

Time Complexity:
O(n^2)

Space Complexity:
O(n)

Key Takeaways:
- dp[i] is defined as "ending at i," not "using the first i elements" -
  that distinction is what forces the answer to be max(dp) instead of
  dp[n - 1], since the longest subsequence doesn't have to end at the
  last element.
- Like Coin Change, this is bottom-up tabulation with an inner loop over
  every earlier choice rather than a fixed pair of choices - here the
  inner loop tries every earlier index as a potential predecessor instead
  of every coin denomination.
- dp[j] is only ever looked up after it has already been computed,
  because indices are processed in increasing order - the same
  build-smaller-answers-first structure as every prior tabulation
  problem in this series.
- An O(n log n) solution exists using binary search over a "tails" array
  (the smallest possible tail value for an increasing subsequence of each
  length), but the O(n^2) DP is the natural starting point and the one
  that generalizes to variants like "count the number of longest
  increasing subsequences."
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
