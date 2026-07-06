"""
LeetCode: 121
Title: Best Time to Buy and Sell Stock

Difficulty: Easy

Pattern:
- Sliding Window (Introduction)
- Track Minimum So Far

Topics:
- Array
- Greedy
"""

# ==========================================================
# Brute Force Idea
# Time Complexity: O(n²)
# Space Complexity: O(1)
# ==========================================================

"""
Try buying on every day and calculate the profit by selling on every
future day. Keep track of the maximum profit found.

Why it is not optimal:
- Compares every possible buy and sell pair.
- Repeats unnecessary calculations.
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================================

class Solution(object):
    def maxProfit(self, prices):
        lowest = prices[0]
        max_profit = 0

        for price in prices:

            if price < lowest:
                lowest = price

            profit = price - lowest

            if profit > max_profit:
                max_profit = profit

        return max_profit


"""
What I Learned
--------------

1. Scan the array only once.

2. Keep track of the lowest price seen so far.

3. At each day, calculate the profit if the stock were sold today.

4. Update the maximum profit whenever a better profit is found.

5. This reduces the time complexity from O(n²) to O(n).

6. If prices always decrease, the maximum profit is 0.
"""


"""
Pattern Recognition
-------------------

Use this pattern when:

- You need the best answer while scanning an array once.
- You are tracking the minimum or maximum value seen so far.
- You want to avoid comparing every pair of elements.
- The answer can be updated incrementally as you iterate.
"""