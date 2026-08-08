"""
Problem:
509. Fibonacci Number

Difficulty:
Easy

Pattern:
Dynamic Programming
Bottom-Up (Tabulation)

Problem:
The Fibonacci numbers form a sequence where each number is the sum of the two
preceding ones.

F(0) = 0
F(1) = 1

For n > 1:

F(n) = F(n - 1) + F(n - 2)

Return F(n).

Example 1:

Input:
n = 2

Output:
1

Example 2:

Input:
n = 4

Output:
3

Key Idea:
The naive recursive solution recomputes the same subproblems over and
over (O(2^n)). Dynamic Programming avoids this by solving each
subproblem exactly once and reusing the result.

Approach (Bottom-Up, O(1) space):
1. Handle base cases: if n <= 1, return n.
2. Keep only the last two computed values (prev2 = F(0), prev1 = F(1)).
3. Iterate from 2 to n, computing the current value as prev1 + prev2,
   then sliding the window forward.
4. Return the final computed value.

Algorithm:
- if n <= 1: return n
- prev2, prev1 = 0, 1
- for _ in range(2, n + 1):
      prev2, prev1 = prev1, prev1 + prev2
- return prev1

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- Dynamic Programming turns exponential recursive solutions into linear
  ones by eliminating repeated work on overlapping subproblems.
- Fibonacci only ever needs the previous two values, so a full DP array
  isn't required - two variables are enough (space-optimized tabulation).
- This is the natural next step after the plain recursive solution.
"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return n

        prev2, prev1 = 0, 1
        for _ in range(2, n + 1):
            prev2, prev1 = prev1, prev1 + prev2

        return prev1
