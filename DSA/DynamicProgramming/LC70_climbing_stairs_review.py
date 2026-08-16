"""
Problem:
70. Climbing Stairs (Review)

Difficulty:
Easy

Pattern:
Dynamic Programming (Bottom-Up)

Problem:
You can climb either 1 or 2 steps at a time. Return the number of distinct
ways to reach the top of an n-step staircase.

Example 1:

Input:
n = 2

Output:
2

Explanation:
1 + 1
2

Example 2:

Input:
n = 3

Output:
3

Explanation:
1 + 1 + 1
1 + 2
2 + 1

Approach (Bottom-Up DP, O(n) time / O(1) space):
The last move to reach step n is either a 1-step from n-1, or a 2-step from
n-2. So the number of ways to reach n is the sum of the ways to reach those
two prior steps - this is just the Fibonacci recurrence:

    ways(n) = ways(n-1) + ways(n-2)

Base cases:
    ways(1) = 1
    ways(2) = 2

Instead of recursing (which recomputes the same subproblems exponentially
many times), walk forward from the base cases, keeping only the last two
values - no array needed since each step only depends on the two before it.

Algorithm:
- if n <= 2: return n
- prev2, prev1 = 1, 2   (ways(1), ways(2))
- for step in range(3, n + 1):
      prev2, prev1 = prev1, prev1 + prev2
- return prev1

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- Climbing Stairs is Fibonacci in disguise: the recurrence falls straight
  out of "the last step was either a 1 or a 2".
- Bottom-up with two rolling variables beats top-down recursion (or even
  memoized recursion) here because each state only ever needs the previous
  two values - no need to keep a full dp array around.
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2

    return prev1


if __name__ == "__main__":
    tests = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89),
    ]

    for n, expected in tests:
        result = climb_stairs(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] climb_stairs({n}) = {result} (expected {expected})")
