"""
Problem:
83. Remove Duplicates from Sorted List

Difficulty:
Easy

Pattern:
Linked List, Traversal

Problem:
Given the head of a sorted linked list, delete all duplicates so that each
element appears only once. Return the linked list sorted as well.

Example:

Input:
1 -> 1 -> 2 -> 3 -> 3

Output:
1 -> 2 -> 3

Approach:
Since the linked list is sorted, duplicate values are always adjacent.
Traverse the list and compare the current node with the next node.
If both values are equal, skip the duplicate node.
Otherwise, move to the next node.

Algorithm:
1. Start from the head.
2. While current and current.next exist:
   - If current.val == current.next.val:
       Remove current.next.
   - Otherwise move current forward.
3. Return the head.

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- A sorted linked list allows duplicate detection without extra memory.
- Adjacent node comparison is sufficient.
- Removing a node requires updating only one pointer.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:

            if current.val == current.next.val:
                current.next = current.next.next

            else:
                current = current.next

        return head