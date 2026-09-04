"""
Problem:
53. Maximum Subarray

Difficulty:
Medium

Pattern:
Arrays
Kadane's Algorithm / Dynamic Programming (One-Pass)

Problem:
Given an integer array nums, find the subarray with the largest sum, and
return its sum. A subarray is a contiguous non-empty part of the array.

Example 1:

Input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output:
6

Explanation:
The subarray [4, -1, 2, 1] has the largest sum 6.

Example 2:

Input:
nums = [1]

Output:
1

Example 3:

Input:
nums = [5, 4, -1, 7, 8]

Output:
23

Key Idea:
The brute force way checks every possible subarray's sum (O(n^2) or worse),
but for each position i, the best subarray *ending exactly at i* only
depends on the best subarray ending at i - 1. If the running sum up to the
previous element is positive, it's worth carrying forward into the current
element (extending helps). If it's negative (or zero), it only drags the
current element down, so it's better to start a fresh subarray at i. This
is Kadane's Algorithm: maintain the best subarray sum ending at the current
position, decide whether to extend or restart, and track the overall
maximum seen so far.

Approach (O(n) time, O(1) space):
1. Initialize current_sum and max_sum to nums[0].
2. For each subsequent number n:
   a. current_sum = max(n, current_sum + n)
      - either start fresh at this element, or extend the running
        subarray, whichever is bigger.
   b. max_sum = max(max_sum, current_sum)
      - update the overall best if this is a new high.
3. Return max_sum.

Algorithm:
- current_sum = nums[0]
- max_sum = nums[0]
- for n in nums[1:]:
      current_sum = max(n, current_sum + n)
      max_sum = max(max_sum, current_sum)
- return max_sum

Time Complexity:
O(n) - a single pass over the array.

Space Complexity:
O(1) - only two running variables are kept.

Key Takeaways:
- "Best subarray ending at i" only depends on "best subarray ending at
  i - 1", so a single running value replaces the need to re-scan from
  every possible start.
- A negative running sum is always a liability to carry forward - drop it
  and restart from the current element instead.
- Same one-pass shape as LC121 (Best Time to Buy and Sell Stock): keep a
  running best, update it greedily at each step instead of comparing
  every pair/subarray.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_sum = nums[0]
        max_sum = nums[0]

        for n in nums[1:]:
            current_sum = max(n, current_sum + n)
            max_sum = max(max_sum, current_sum)

        return max_sum
