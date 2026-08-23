"""
Problem:
72. Edit Distance

Difficulty:
Medium

Pattern:
Dynamic Programming
Bottom-Up (Tabulation) - 2D String DP

Problem:
Given two strings word1 and word2, return the minimum number of
operations required to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

Example 1:

Input:
word1 = "horse", word2 = "ros"

Output:
3

Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input:
word1 = "intention", word2 = "execution"

Output:
5

Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Key Idea:
dp[i][j] means the minimum number of operations required to convert the
first i characters of word1 (word1[:i]) into the first j characters of
word2 (word2[:j]). Row/column 0 represent the empty prefix, so dp[i][0]
= i (delete all i characters of word1 to reach empty) and dp[0][j] = j
(insert all j characters of word2 to build it up from empty) - pure
edge cases, same framing as Longest Common Subsequence.

The transition compares the *last* characters of the two prefixes under
consideration, word1[i-1] and word2[j-1]:
- If they match, that character needs no operation and both pointers
  retreat past it for free: dp[i][j] = dp[i-1][j-1] - identical to
  LCS's diagonal move, but without the "+1", since matching costs
  nothing here.
- If they don't match, one of the three operations must be spent, and
  each maps to a specific predecessor cell:
    - Replace word1[i-1] with word2[j-1]: dp[i-1][j-1] + 1 - both
      prefixes shrink by one, paying for the substitution.
    - Delete word1[i-1]: dp[i-1][j] + 1 - word1's prefix shrinks by
      one, word2's stays put.
    - Insert word2[j-1] onto word1: dp[i][j-1] + 1 - word2's prefix
      shrinks by one, word1's stays put (equivalently: word1 already
      matches word2[:j-1], so append the missing character).
  dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) - take the
  cheapest of the three, then pay for that one operation.

This is the general shape for "transform one sequence into another" DP:
a match chains diagonally for free, a mismatch pays 1 and falls back to
the best of diagonal/up/left - unlike LCS, all three neighbors are
candidates here, since edit distance allows substitution as well as
skipping.

Approach (Bottom-Up, O(m * n) time):
1. Let m = len(word1), n = len(word2).
2. Build a (m+1) x (n+1) table dp.
3. Seed dp[i][0] = i for every i (delete down to empty) and
   dp[0][j] = j for every j (insert up from empty).
4. Fill row by row, i from 1 to m, j from 1 to n:
   a. If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1].
   b. Else: dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]).
5. dp[m][n] holds the answer - the minimum edit distance over the full
   strings.

Algorithm:
- m, n = len(word1), len(word2)
- dp = [[0] * (n + 1) for _ in range(m + 1)]
- for i in range(m + 1): dp[i][0] = i
- for j in range(n + 1): dp[0][j] = j
- for i in range(1, m + 1):
      for j in range(1, n + 1):
          if word1[i - 1] == word2[j - 1]:
              dp[i][j] = dp[i - 1][j - 1]
          else:
              dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
- return dp[m][n]

Time Complexity:
O(m * n) - one pass filling every cell of the (m+1) x (n+1) table.

Space Complexity:
O(m * n) for the full table. Reducible to O(min(m, n)) by keeping only
the previous row, since dp[i][j] only ever depends on the row directly
above and the current row's already-filled cells.

Key Takeaways:
- dp[i][j] = "cost to turn the first i characters of word1 into the
  first j characters of word2" is the same two-sequence framing as LCS,
  but the transition rewards a match with a free diagonal move instead
  of a "+1" diagonal move, and a mismatch costs 1 no matter which of
  the three neighbors is chosen.
- The three operations map directly onto the three neighboring cells:
  replace <-> diagonal (i-1, j-1), delete <-> up (i-1, j), insert <->
  left (i, j-1) - "which cell am I pulling from" answers "which
  operation am I paying for".
- Base cases dp[i][0] = i and dp[0][j] = j aren't arbitrary - they're
  the cost of turning a non-empty prefix into (or out of) nothing,
  which can only be done by inserting or deleting every character.
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]
                    )

        return dp[m][n]
