"""
Problem: 141. Linked List Cycle

Difficulty:
Easy

Pattern:
Linked List + Fast & Slow Pointers

Problem:
Given head, the head of a linked list, determine if the linked list has a
cycle in it.

Example:

Input:
1 -> 2 -> 3 -> 4
     ^         |
     +---------+

Output:
true

Key Idea:
Use two pointers moving through the list at different speeds:
- slow moves 1 step at a time.
- fast moves 2 steps at a time.

If there is a cycle, fast will eventually "lap" slow and they will meet
(slow == fast). If there is no cycle, fast reaches None first.

Approach:
1. Initialize slow = head, fast = head.
2. While fast and fast.next are not None:
   - Move slow forward by 1.
   - Move fast forward by 2.
   - If slow == fast, a cycle exists -> return True.
3. If the loop ends (fast reaches None), there is no cycle -> return False.

Algorithm:
- slow = head
- fast = head
- while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
- return False

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- This is the classic "Floyd's Cycle Detection" (tortoise and hare) algorithm.
- No extra data structure (like a set) is needed, so space stays O(1).
- fast always reaches slow's old position or a cycle meeting point before
  running off the end of the list, if a cycle exists.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
