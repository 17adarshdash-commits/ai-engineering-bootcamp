"""
Problem:
155. Min Stack

Difficulty:
Medium

Pattern:
Stack
Auxiliary Stack

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Approach:
Maintain two stacks:
1. stack -> stores all values
2. minstack -> stores the minimum value at every level

When pushing:
- Push value onto stack.
- Push min(current minimum, value) onto minstack.

When popping:
- Pop from both stacks.

The current minimum is always the top of minstack.

Time Complexity:
Push: O(1)
Pop: O(1)
Top: O(1)
GetMin: O(1)

Space Complexity:
O(n)

Key Takeaways:
- Auxiliary data structures can improve operation efficiency.
- Keeping both stacks synchronized is essential.
- Storing the minimum at each level eliminates repeated searches.
"""

class MinStack(object):

    def __init__(self):

        self.stack = []
        self.minstack = []

    def push(self, value):

        self.stack.append(value)
        if not self.minstack:
            self.minstack.append(value)
        else:
            current_min = self.minstack[-1]
            self.minstack.append(min(current_min, value))
        

    def pop(self):
        
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        
        x = self.stack[-1]
        return x
        

    def getMin(self):
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()