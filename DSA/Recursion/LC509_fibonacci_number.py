"""
Problem:
509. Fibonacci Number

Difficulty:
Easy

Pattern:
Recursion

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
The recursive definition of the Fibonacci sequence directly translates into
recursive code.

Approach:
1. If n is 0 or 1, return n.
2. Otherwise:
    - Compute fib(n-1)
    - Compute fib(n-2)
3. Return their sum.

Algorithm:
- if n <= 1:
    return n
- return fib(n-1) + fib(n-2)

Time Complexity:
O(2^n)

Space Complexity:
O(n)

Key Takeaways:
- Every recursive function requires a base case.
- Fibonacci demonstrates recursive thinking clearly.
- This simple recursive solution is elegant but inefficient because it
  recalculates many values.
- Later, Dynamic Programming and Memoization optimize this to O(n).
"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)