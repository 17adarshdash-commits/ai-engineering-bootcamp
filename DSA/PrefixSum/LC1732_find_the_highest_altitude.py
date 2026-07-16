"""
LeetCode: 1732
Title: Find the Highest Altitude

Difficulty: Easy

Pattern:
- Prefix Sum

Topics:
- Arrays
- Prefix Sum
"""

# ==========================================================
# Brute Force Idea
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================================

"""
Start at altitude 0.

Create an array that stores the altitude after every gain/loss.

Return the maximum altitude from the array.
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================================

class Solution(object):
    def largestAltitude(self, gain):
        altitudes = [0]

        for i in range(len(gain)):
            altitude = altitudes[-1] + gain[i]
            altitudes.append(altitude)

        return max(altitudes)


"""
What I Learned
--------------

1. Prefix Sum can represent cumulative values instead of just sums.

2. Every new altitude depends on the previous altitude.

3. The first altitude is always 0.

4. After calculating all altitudes,
   the highest altitude is simply the maximum value.

Time Complexity:
O(n)

Space Complexity:
O(n)

Possible Optimization:
Instead of storing every altitude,
keep only:

- current_altitude
- highest_altitude

This reduces the space complexity to O(1).
"""


"""
Pattern Recognition
-------------------

Use this pattern when:

- Values are cumulative.
- Each state depends on the previous state.
- You need the maximum or minimum cumulative value.

Common interview phrases:

- Running Total
- Prefix Sum
- Cumulative Sum
- Highest Altitude
- Running Balance
"""