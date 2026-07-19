"""
LeetCode 682 - Baseball Game

Pattern:
Stack

Time Complexity:
O(n)

Space Complexity:
O(n)

What I Learned:
- A stack is useful when operations depend on the most recent elements.
- append() acts as push.
- pop() removes the latest element.
- stack[-1] accesses the top of the stack.
- stack[-2] accesses the second most recent element.
"""

class Solution(object):
    def calPoints(self, operations):
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)