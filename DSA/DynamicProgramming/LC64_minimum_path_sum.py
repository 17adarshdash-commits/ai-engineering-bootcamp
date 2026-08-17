"""
Problem:
64. Minimum Path Sum

Difficulty:
Medium

Pattern:
Dynamic Programming
Bottom-Up (Tabulation) - Grid DP

Problem:
Given an m x n grid filled with non-negative numbers, find a path from
top left to bottom right, which minimizes the sum of all numbers along
its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input:
grid = [[1,3,1],[1,5,1],[4,2,1]]

Output:
7

Explanation:
Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum.

Example 2:

Input:
grid = [[1,2,3],[4,5,6]]

Output:
12

Key Idea:
The only way to reach cell (i, j) is from directly above (i-1, j) or
directly to the left (i, j-1) - movement is restricted to down/right, so
those are the sole two predecessors. The cheapest way to reach (i, j) is
therefore the cheapest way to reach whichever of those two predecessors
is smaller, plus the cost of (i, j) itself. This is the same
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) transition as
Unique Paths, except summing costs along the way instead of counting
route combinations - min replaces the "+" combination step.

The first row and first column are edge cases: a cell in row 0 can only
be reached from the left (no row above it), and a cell in column 0 can
only be reached from above (no column to its left) - each accumulates as
a straight running sum along that edge.

Approach (Bottom-Up, O(rows * cols) time):
1. Reuse the input grid itself as the dp table - grid[i][j] is
   overwritten in place to mean "cheapest path sum to reach (i, j)"
   instead of "the cost of cell (i, j) alone".
2. Seed grid[0][0] as itself (the start, no predecessor).
3. Fill the first row left to right: grid[0][j] += grid[0][j-1] (only
   reachable from the left).
4. Fill the first column top to bottom: grid[i][0] += grid[i-1][0] (only
   reachable from above).
5. Fill every remaining cell in row-major order: grid[i][j] +=
   min(grid[i-1][j], grid[i][j-1]) - both predecessors are guaranteed to
   already be filled in, since row-major order visits (i-1, j) and
   (i, j-1) before (i, j).
6. grid[-1][-1] holds the answer - the cheapest path sum to the bottom
   right corner.

Algorithm:
- for j in range(1, cols): grid[0][j] += grid[0][j - 1]
- for i in range(1, rows): grid[i][0] += grid[i - 1][0]
- for i in range(1, rows):
      for j in range(1, cols):
          grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
- return grid[-1][-1]

Time Complexity:
O(rows * cols)

Space Complexity:
O(1) extra (in-place on the input grid); O(rows * cols) if the grid must
be left unmodified and a separate dp table is used instead.

Key Takeaways:
- Grid DP transitions are shaped by which cells can legally lead into the
  current one - here, exactly "above" and "left", same predecessor set as
  Unique Paths, just combined with a different operator (min + add,
  instead of add for counting paths).
- The first row/column aren't special-cased logic so much as a
  degenerate version of the same transition - each has only one valid
  predecessor instead of two, so the "min of two" collapses to "the one
  that exists".
- Reusing the input grid as the dp table is a common space optimization
  whenever the problem doesn't require preserving the original input.
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])

        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
