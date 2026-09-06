"""
Day 66 — Matplotlib Basics with Pandas
Bar chart vs Scatter plot
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Adarsh", "Rahul", "Priya", "Aman", "Sneha"],
    "Marks": [85, 72, 91, 64, 78]
}

df = pd.DataFrame(data)
print(df)

# ---------- Line plot (extra practice) ----------
plt.plot(df["Name"], df["Marks"], marker="o", label="Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks — Line Plot")
plt.legend()
plt.show()

# ---------- Bar chart ----------
# Good for comparing categories (each student's marks side by side)
plt.bar(df["Name"], df["Marks"], color="skyblue")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks — Bar Chart")
plt.show()

# ---------- Scatter plot ----------
# Good for seeing relationships / distribution between numerical variables
plt.scatter(df["Name"], df["Marks"], color="red")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks Distribution — Scatter Plot")
plt.show()


# =========================================================
# Part 4 — DSA: LeetCode 121, Best Time to Buy and Sell Stock
# Reimplemented from memory (review, not new problem)
# =========================================================

def max_profit(prices):
    """
    Track the minimum price seen so far while scanning left to right.
    At each day, the best profit if we sold today is price - min_so_far.
    Keep a running max of that.

    Time:  O(n) — single pass
    Space: O(1) — two variables only
    """
    if not prices:
        return 0

    min_price_so_far = prices[0]
    max_profit_so_far = 0

    for price in prices[1:]:
        # current possible profit if sold today
        current_profit = price - min_price_so_far
        max_profit_so_far = max(max_profit_so_far, current_profit)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit_so_far


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    result = max_profit(prices)
    print(f"prices = {prices}")
    print(f"max profit = {result}")  # expected 5

    # Challenge: why we don't need to compare every buy/sell pair
    # ------------------------------------------------------------
    # A brute-force approach checks every (buy_day, sell_day) pair
    # with buy_day < sell_day -> O(n^2) comparisons.
    #
    # But for any sell day, the best possible buy day is always the
    # day with the LOWEST price seen so far (before it). Any other
    # earlier buy day would only produce a smaller or equal profit,
    # since profit = sell_price - buy_price, and we want buy_price
    # minimized. So instead of re-checking all previous days for
    # every sell day, we just carry forward the minimum price seen
    # so far as a single running value. That collapses the inner
    # loop into O(1) work per day, giving O(n) total.
