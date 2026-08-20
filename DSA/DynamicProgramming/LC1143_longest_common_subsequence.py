"""
Problem:
1143. Longest Common Subsequence

Difficulty:
Medium

Pattern:
Dynamic Programming
Bottom-Up (Tabulation) - 2D String DP

Problem:
Given two strings text1 and text2, return the length of their longest
common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original
string with some characters (can be none) deleted without changing the
relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to
both strings.

Example 1:

Input:
text1 = "abcde", text2 = "ace"

Output:
3

Explanation:
The longest common subsequence is "ace" and its length is 3.

Example 2:

Input:
text1 = "abc", text2 = "abc"

Output:
3

Explanation:
The longest common subsequence is "abc" and its length is 3.

Example 3:

Input:
text1 = "abc", text2 = "def"

Output:
0

Explanation:
There is no such common subsequence, so the result is 0.

Key Idea:
dp[i][j] means the length of the LCS between the first i characters of
text1 and the first j characters of text2 (i.e. text1[:i] and
text2[:j]). Row/column 0 represent the empty prefix, so dp[0][j] and
dp[i][0] are always 0 - the LCS of anything with an empty string is
empty.

The transition compares the *last* characters of the two prefixes under
consideration, text1[i-1] and text2[j-1]:
- If they match, that character can extend any LCS found in the shorter
  prefixes: dp[i][j] = 1 + dp[i-1][j-1] - both pointers retreat past the
  matched character, and 1 is added for having matched it.
- If they don't match, the matched character can't be part of the LCS
  for this specific pair of endpoints, so the best is whichever happens
  if one string's prefix is trimmed by one and the other kept as-is:
  dp[i][j] = max(dp[i-1][j], dp[i][j-1]) - try dropping the last
  character of text1, or dropping the last character of text2, and keep
  the better of the two.

This is the general shape for "compare two sequences" DP: matching
characters chain diagonally (i-1, j-1), mismatches fall back to the
better of the cell above or the cell to the left - unlike Edit
Distance, there's no "substitute" option, since LCS only ever
skips characters, never replaces them.

Approach (Bottom-Up, O(m * n) time):
1. Let m = len(text1), n = len(text2).
2. Build a (m+1) x (n+1) table dp, all initialized to 0 - row 0 and
   column 0 stay 0, representing an empty prefix of either string.
3. Fill row by row, i from 1 to m, j from 1 to n:
   a. If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1.
   b. Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
4. dp[m][n] holds the answer - the LCS length over the full strings.

Algorithm:
- m, n = len(text1), len(text2)
- dp = [[0] * (n + 1) for _ in range(m + 1)]
- for i in range(1, m + 1):
      for j in range(1, n + 1):
          if text1[i - 1] == text2[j - 1]:
              dp[i][j] = dp[i - 1][j - 1] + 1
          else:
              dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
- return dp[m][n]

Time Complexity:
O(m * n) - one pass filling every cell of the (m+1) x (n+1) table.

Space Complexity:
O(m * n) for the full table. Reducible to O(min(m, n)) by keeping only
the previous row, since dp[i][j] only ever depends on the row directly
above and the current row's already-filled cells.

Key Takeaways:
- dp[i][j] = "answer using the first i and first j elements of the two
  inputs" is the standard framing for any two-sequence comparison DP
  (LCS, Edit Distance, string matching variants) - row/column 0 encode
  the empty-prefix base case.
- Matching elements chain diagonally (dp[i-1][j-1] + 1); non-matching
  elements fall back to the best of dropping one element from either
  side (max of up/left) - no diagonal move happens on a mismatch here,
  since LCS never substitutes, only skips.
- The same table also reconstructs the actual subsequence (not just its
  length) by walking back from dp[m][n]: step diagonally on a match,
  otherwise step toward whichever of dp[i-1][j] / dp[i][j-1] was larger.
"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
