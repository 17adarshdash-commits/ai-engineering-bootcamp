"""
Problem:
62. Unique Paths

Difficulty:
Medium

Pattern:
Dynamic Programming
Bottom-Up (Tabulation) - Grid DP

Problem:
There is a robot on an m x n grid. The robot is initially located at the
top-left corner. The robot tries to move to the bottom-right corner. The
robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique
paths that the robot can take to reach the bottom-right corner.

Example 1:

Input:
m = 3, n = 7

Output:
28

Example 2:

Input:
m = 3, n = 2

Output:
3

Explanation:
From the top-left corner, there are a total of 3 ways to reach the
bottom-right corner:
1. Right -> Down -> Down
2. Down -> Right -> Down
3. Down -> Down -> Right

Key Idea:
The only way to arrive at cell (i, j) is from directly above (i-1, j) or
directly to the left (i, j-1) - movement is restricted to down/right, so
those are the sole two predecessors. Every route that reaches (i, j)
therefore arrives via exactly one of those two cells, so the number of
distinct routes to (i, j) is the sum of the routes to each predecessor:
dp[i][j] = dp[i-1][j] + dp[i][j-1]. This is the same predecessor
relationship as Minimum Path Sum, except summing route counts instead of
minimizing costs - "+" replaces the "min" combination step.

The first row and first column are edge cases: a cell in row 0 can only
be reached from the left (no row above it), and a cell in column 0 can
only be reached from above (no column to its left) - each has exactly
one way to be reached, since there's only one straight-line path along
that edge.

Approach (Bottom-Up, O(m * n) time):
1. Build an m x n dp table.
2. Seed the entire first row and first column with 1 - there's exactly
   one way to reach any cell along either edge (a straight line of
   rights, or a straight line of downs).
3. Fill every remaining cell in row-major order:
   dp[i][j] = dp[i-1][j] + dp[i][j-1] - both predecessors are guaranteed
   to already be filled in, since row-major order visits (i-1, j) and
   (i, j-1) before (i, j).
4. dp[-1][-1] holds the answer - the total number of unique paths to the
   bottom-right corner.

Algorithm:
- dp = [[1] * n for _ in range(m)]
- for i in range(1, m):
      for j in range(1, n):
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
- return dp[-1][-1]

Time Complexity:
O(m * n)

Space Complexity:
O(m * n) for the dp table; can be reduced to O(n) by keeping only the
previous row, since each cell only ever needs the row above and the
value directly to its left.

Key Takeaways:
- Grid DP transitions are shaped by which cells can legally lead into the
  current one - here, exactly "above" and "left", same predecessor set as
  Minimum Path Sum, just combined with a different operator (add for
  counting paths, instead of min + add for minimizing cost).
- The first row/column aren't special-cased logic so much as a
  degenerate version of the same transition - each has only one valid
  predecessor instead of two, collapsing "sum of two" down to "the one
  that exists", which is exactly 1 way.
- Seeding edges with 1 (not 0) reflects that reaching any edge cell has
  exactly one possible route, not zero - a base case, not an absence of
  paths.
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
