"""
Problem: 162. Find Peak Element

Difficulty: Medium

Pattern:
Binary Search

Problem:
A peak element is an element that is strictly greater than its neighbours.
Return the index of any peak element.

Examples:
Input: nums = [1,2,3,1]
Output: 2

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5

Key Idea:
Instead of searching for a target, compare nums[mid] with nums[mid + 1].

- If nums[mid] < nums[mid + 1], we are on an increasing slope,
  so a peak must exist to the right.

- Otherwise, we are on a decreasing slope,
  so a peak is at mid or to the left.

Approach:
1. Initialize low and high.
2. While low < high:
    - Find mid.
    - Compare nums[mid] and nums[mid + 1].
    - Move towards the side that must contain a peak.
3. Return low.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Key Takeaways:
- Binary Search can work without a fully sorted array.
- Look for a property that lets you eliminate half of the search space.
- Always keep the possible peak in the search range.
"""

class Solution(object):
    def findPeakElement(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low