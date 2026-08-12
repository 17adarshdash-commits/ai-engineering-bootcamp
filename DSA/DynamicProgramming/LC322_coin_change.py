"""
Problem:
322. Coin Change

Difficulty:
Medium

Pattern:
Dynamic Programming
Bottom-Up (Tabulation)

Problem:
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins needed to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return
-1. You may assume there are infinitely many coins of each denomination.

Example 1:

Input:
coins = [1, 2, 5], amount = 11

Output:
3

Explanation:
11 = 5 + 5 + 1, using 3 coins.

Example 2:

Input:
coins = [2], amount = 3

Output:
-1

Explanation:
3 cannot be made up using only coins of denomination 2.

Example 3:

Input:
coins = [1], amount = 0

Output:
0

Key Idea:
For every sub-amount from 1 up to the target, there are exactly as many
choices as there are coin denominations: use that coin (and add 1 to the
best answer already found for the remaining amount), or don't. The fewest
coins needed for a given amount is the minimum, over every coin no larger
than that amount, of 1 + (fewest coins for amount - coin). This is the
same "take it or skip it" shape as House Robber and Min Cost Climbing
Stairs, except here the choice is which coin to take rather than a single
binary include/exclude decision, so every coin is tried and the best of
all of them is kept.

Approach (Bottom-Up, O(amount * coins) time):
1. Build a dp array of size amount + 1, where dp[a] holds the fewest coins
   needed to make amount a. Seed dp[0] = 0 (zero coins needed to make 0),
   and every other entry at "infinity" (amount + 1 works as a stand-in,
   since no valid answer can ever reach that high).
2. For each sub-amount a from 1 to amount, try every coin denomination
   that is <= a: dp[a] = min(dp[a], 1 + dp[a - coin]) - taking that coin
   costs 1 coin plus whatever it took to make the remaining a - coin.
3. After filling the whole table, dp[amount] holds the answer - unless it
   is still stuck at the "infinity" sentinel, meaning no combination of
   coins reaches that amount, in which case return -1.

Algorithm:
- dp = [0] + [amount + 1] * amount
- for a in range(1, amount + 1):
      for coin in coins:
          if coin <= a:
              dp[a] = min(dp[a], 1 + dp[a - coin])
- return dp[amount] if dp[amount] <= amount else -1

Time Complexity:
O(amount * len(coins))

Space Complexity:
O(amount)

Key Takeaways:
- The "infinity" sentinel (amount + 1) is a clean stand-in for
  unreachable because the true answer, if it exists, can never exceed
  amount coins (using only 1-value coins) - anything at or above that
  sentinel is provably impossible.
- Unlike House Robber's two-choice-per-step decision, this problem tries
  every coin at every sub-amount, since the best coin to use isn't fixed -
  it's still bottom-up tabulation, just with an inner loop over choices
  instead of a single fixed pair of them.
- dp[a - coin] is only ever looked up after it has already been computed,
  because sub-amounts are solved in increasing order - the same
  build-smaller-answers-first structure as every prior tabulation problem.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        unreachable = amount + 1
        dp = [0] + [unreachable] * amount

        for sub_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= sub_amount:
                    dp[sub_amount] = min(dp[sub_amount], 1 + dp[sub_amount - coin])

        return dp[amount] if dp[amount] <= amount else -1
