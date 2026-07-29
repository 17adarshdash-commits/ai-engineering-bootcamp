"""
Problem:
141. Linked List Cycle

Difficulty:
Easy

Pattern:
Fast & Slow Pointer (Floyd's Cycle Detection Algorithm)

Problem:
Given the head of a linked list, determine if the linked list has a cycle.

A cycle exists if a node can be reached again by continuously following the next pointers.

Return True if there is a cycle.
Otherwise, return False.

Example 1:

Input:
3 -> 2 -> 0 -> -4
     ^         |
     |_________|

Output:
True

Example 2:

Input:
1 -> 2 -> None

Output:
False

Key Idea:
Use two pointers moving at different speeds.

The slow pointer moves one node at a time.
The fast pointer moves two nodes at a time.

If a cycle exists, the fast pointer will eventually catch up to the slow pointer.
If there is no cycle, the fast pointer will reach the end of the list.

Approach:
1. Initialize slow and fast pointers at the head.
2. Move slow one step and fast two steps.
3. If slow and fast point to the same node, a cycle exists.
4. If the fast pointer reaches None, there is no cycle.

Algorithm:
- slow = head
- fast = head
- while fast and fast.next:
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
- The Fast & Slow Pointer technique detects cycles without extra memory.
- The fast pointer gains one node on the slow pointer every iteration inside a cycle.
- If there is no cycle, the fast pointer reaches the end of the list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False