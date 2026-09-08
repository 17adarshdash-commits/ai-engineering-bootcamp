"""
LeetCode 121 — Best Time to Buy and Sell Stock (Review)

Given an array `prices` where prices[i] is the price of a stock on day i,
find the maximum profit from buying on one day and selling on a later day.
If no profit is possible, return 0.

Example:
    prices = [7, 1, 5, 3, 6, 4]
    answer = 5   (buy at 1, sell at 6)

Pattern:
    minimum price so far
            |
    profit if selling today = price[i] - min_price_so_far
            |
    maximum profit = best profit seen across all days

Time:  O(n)  -- single pass through the array
Space: O(1)  -- only two running variables
"""


def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        # track the lowest price seen so far (best day to have bought)
        min_price = min(min_price, price)

        # profit if we sold today, given the cheapest buy so far
        profit_today = price - min_price

        # keep the best profit seen across all days
        best_profit = max(best_profit, profit_today)

    return best_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("prices:", prices)
    print("max profit:", max_profit(prices))  # expected: 5

    print(max_profit([7, 6, 4, 3, 1]))  # expected: 0 (prices only fall)
    print(max_profit([]))               # expected: 0 (empty input)
