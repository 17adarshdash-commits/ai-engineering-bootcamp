"""
Problem:
121. Best Time to Buy and Sell Stock

Difficulty:
Easy

Pattern:
Arrays
One-Pass / Track Running Minimum

Problem:
You are given an array prices where prices[i] is the price of a given
stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one
stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you
cannot achieve any profit, return 0.

Example 1:

Input:
prices = [7, 1, 5, 3, 6, 4]

Output:
5

Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1
= 5.

Example 2:

Input:
prices = [7, 6, 4, 3, 1]

Output:
0

Explanation:
Prices only fall, so no transaction is done and the max profit is 0.

Key Idea:
The brute force way checks every pair of buy/sell days (O(n^2)), but a
sale on day i is only ever worth doing against the lowest price seen on
any day before i - no earlier price can help more than the minimum. So
instead of comparing every pair, walk the array once and keep a running
minimum price seen so far. At each day, treat that day as a potential
sell day and check the profit against the running minimum. The largest
such profit across all days is the answer.

Approach (O(n) time, O(1) space):
1. Initialize min_price to the first price, and max_profit to 0.
2. For each subsequent price p:
   a. If p < min_price, update min_price = p (a new potential buy day).
   b. Otherwise, compute profit = p - min_price and update
      max_profit = max(max_profit, profit) (a potential sell day).
3. Return max_profit.

Algorithm:
- min_price = prices[0]
- max_profit = 0
- for p in prices[1:]:
      if p < min_price:
          min_price = p
      else:
          max_profit = max(max_profit, p - min_price)
- return max_profit

Time Complexity:
O(n) - a single pass over the array.

Space Complexity:
O(1) - only two running variables are kept.

Key Takeaways:
- Whenever "best pair with i as the second element" only depends on the
  best value seen before i, a single running min/max replaces the need
  to compare every pair.
- Track the running minimum, not the running max, because the buy has
  to happen before the sell - the minimum is only useful "so far", not
  looking ahead.
- Same one-pass shape as Kadane's Algorithm: keep a running best,
  update it greedily at each step instead of re-scanning.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = prices[0]
        max_profit = 0

        for p in prices[1:]:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)

        return max_profit
