"""
Problem:
203. Remove Linked List Elements

Difficulty:
Easy

Pattern:
Dummy (Sentinel) Node

Problem:
Given the head of a linked list and an integer val, remove all the nodes
of the linked list that have Node.val == val, and return the new head.

Example 1:

Input:
head = [1,2,6,3,4,5,6]
val = 6

Output:
[1,2,3,4,5]

Example 2:

Input:
head = []
val = 1

Output:
[]

Example 3:

Input:
head = [7,7,7,7]
val = 7

Output:
[]

Key Idea:
Use a dummy (sentinel) node before the head of the linked list.

The dummy node eliminates the need to handle deleting the head node as a
special case. Every node in the list now has a previous node, making pointer
updates simple and consistent.

Approach:
1. Create a dummy node and point it to the head.
2. Start traversing from the dummy node.
3. If the next node contains the target value, skip it.
4. Otherwise, move to the next node.
5. Return dummy.next as the new head.

Algorithm:
- Create a dummy node.
- Set dummy.next = head.
- Initialize current = dummy.
- While current.next exists:
    - If current.next.val == val:
        - Skip the node by updating current.next.
    - Otherwise:
        - Move current forward.
- Return dummy.next.

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- Dummy nodes simplify linked list operations involving the head node.
- Do not move the current pointer immediately after deleting a node, as
  consecutive nodes may also need to be removed.
- Every node is visited at most once, resulting in linear time complexity.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)
        dummy.next = head

        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next