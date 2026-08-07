"""
Problem:
70. Climbing Stairs

Difficulty:
Easy

Pattern:
Recursion
Dynamic Programming (Introduction)

Problem:
You can climb either 1 or 2 steps at a time.
Return the number of distinct ways to reach the top.

Approach:
Use recursion.

At every step:
- Climb 1 step
- Climb 2 steps

Total ways:

f(n) = f(n-1) + f(n-2)

Base Cases:
f(1) = 1
f(2) = 2

Time Complexity:
O(2^n)

Space Complexity:
O(n)

Note:
This recursive solution is easy to understand but inefficient because it
recomputes the same subproblems. Dynamic Programming improves it to O(n).
"""

class Solution(object):
    def climbStairs(self, n):
        
        if n <= 2:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)