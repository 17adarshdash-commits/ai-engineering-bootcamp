"""
Problem: 206. Reverse Linked List

Difficulty:
Easy

Pattern:
Linked List

Problem:
Given the head of a singly linked list, reverse the list and return the reversed list.

Example:

Input:
1 -> 2 -> 3 -> 4 -> 5

Output:
5 -> 4 -> 3 -> 2 -> 1

Key Idea:
Reverse the direction of every next pointer while traversing the list once.

Approach:
1. Initialize prev = None.
2. Set current = head.
3. While current is not None:
   - Save current.next.
   - Reverse current.next.
   - Move prev forward.
   - Move current forward.
4. Return prev.

Algorithm:
- prev = None
- current = head
- while current is not None:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
- return prev

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- Reverse pointers, not node values.
- Always save the next node before changing links.
- prev becomes the new head after traversal.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev