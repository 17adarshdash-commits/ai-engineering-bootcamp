"""
Problem:
53. Maximum Subarray (Review #2)

Difficulty:
Medium

Pattern:
Arrays
Kadane's Algorithm / Dynamic Programming (One-Pass)

Problem:
Given an integer array nums, find the subarray with the largest sum, and
return its sum. A subarray is a contiguous non-empty part of the array.

Example:
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum 6.

Approach (O(n) time, O(1) space):
Walk the array once, tracking the best sum of a subarray ending at the
current index (current_sum) and the best sum seen anywhere so far
(max_sum). At each element, decide whether to extend the running
subarray or drop it and start fresh at this element.

Algorithm:
- current_sum = nums[0]
- max_sum = nums[0]
- for n in nums[1:]:
      current_sum = max(n, current_sum + n)
      max_sum = max(max_sum, current_sum)
- return max_sum

Time Complexity:
O(n) - single pass over the array.

Space Complexity:
O(1) - only two running variables.

Plain-English explanation of `current_sum = max(num, current_sum + num)`:
At every element, we ask: "am I better off tacking this number onto the
subarray I've been building, or is that running subarray actually
dragging me down, so I should just start over from this number alone?"
- `current_sum + num` = the value if we keep extending the existing run.
- `num` on its own = the value if we abandon everything before it and
  restart right here.
Whichever of those two is bigger becomes the new current_sum. In short:
a subarray with a negative (or too-small) running total is a liability,
not an asset - the moment carrying it forward would make things worse
than starting fresh, we cut it loose.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(sol.maxSubArray([1]))                              # 1
    print(sol.maxSubArray([5, 4, -1, 7, 8]))                 # 23
