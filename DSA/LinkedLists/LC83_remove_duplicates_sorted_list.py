"""
Problem:
83. Remove Duplicates from Sorted List

Difficulty:
Easy

Pattern:
Linked List Traversal

Problem:
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once.

Return the linked list sorted as well.

Example 1:

Input:
1 -> 1 -> 2

Output:
1 -> 2

Example 2:

Input:
1 -> 1 -> 2 -> 3 -> 3

Output:
1 -> 2 -> 3

Key Idea:
Since the linked list is already sorted, duplicate values will always appear
next to each other.

Instead of using extra memory like a set, simply compare the current node with
the next node.

Approach:
1. If the list is empty, return the head.
2. Traverse the linked list.
3. If the current node and next node have the same value:
    - Skip the duplicate node.
4. Otherwise:
    - Move to the next node.
5. Return the head.

Algorithm:
- current = head
- while current and current.next:
    - if current.val == current.next.val:
        - current.next = current.next.next
    - else:
        - current = current.next
- return head

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- A sorted linked list allows duplicate detection by comparing adjacent nodes.
- No additional data structures are required.
- Removing a node only requires updating one pointer.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head is None:
            return head

        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head