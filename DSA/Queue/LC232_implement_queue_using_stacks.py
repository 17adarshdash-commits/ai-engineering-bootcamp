"""
Problem:
232. Implement Queue using Stacks

Difficulty:
Easy

Pattern:
Stack
Queue
Two Stacks (Amortized O(1))

Problem:
Implement a first-in-first-out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal
queue (push, peek, pop, empty).

Key idea:
- Queue -> FIFO (First In, First Out)
- Stack -> LIFO (Last In, Last Out)

A single stack reverses order once. Reversing it a second time
restores the original order. Two stacks give us exactly that:
- in_stack:  holds newly pushed elements, in push order (top = most
  recent).
- out_stack: holds elements in reverse of in_stack, so its top is the
  oldest element -> exactly what a queue needs to pop/peek next.

Approach:
push(x):
    Always push onto in_stack. O(1), no reordering needed yet.

pop() / peek():
    If out_stack is empty, dump all of in_stack into out_stack
    (popping each and pushing it onto out_stack). This reverses the
    order once, so the oldest element ends up on top of out_stack.
    Then pop()/peek() from out_stack.

    If out_stack already has elements, its top is already the oldest
    remaining element -> use it directly, no need to touch in_stack.

empty():
    True only if both stacks are empty.

Why amortized O(1):
Each element is pushed onto in_stack once and, at some point, popped
from in_stack and pushed onto out_stack once, then popped from
out_stack once. That's at most 3 "stack operations" per element over
its whole lifetime in the queue. So while a single pop() call can be
O(n) in the worst case (when it triggers the full transfer), the cost
is "paid for" by the n pushes that put those elements there. Averaged
over any sequence of operations, each operation costs O(1).

Time Complexity:
push: O(1)
pop:  amortized O(1) (worst case O(n) on a transfer)
peek: amortized O(1) (worst case O(n) on a transfer)
empty: O(1)

Space Complexity:
O(n) -- elements live in one of the two stacks at any time.

Key Takeaways:
- Two stacks can simulate a queue because reversing twice restores
  original order.
- Only transfer elements from in_stack to out_stack when out_stack is
  empty -- this is what makes the amortized cost O(1) instead of O(n)
  per operation.
- "Amortized" means the average cost per operation over a sequence is
  low, even if individual operations occasionally cost more.
"""


class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def _transfer_if_needed(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self):
        self._transfer_if_needed()
        return self.out_stack.pop()

    def peek(self):
        self._transfer_if_needed()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # 1
    print(q.pop())    # 1
    print(q.empty())  # False
