"""
Problem:
21. Merge Two Sorted Lists

Difficulty:
Easy

Pattern:
Linked List, Dummy (Sentinel) Node

Problem:
You are given the heads of two sorted linked lists, list1 and list2.

Merge the two lists into one sorted linked list by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

Example:

Input:
list1 = [1,2,4]
list2 = [1,3,4]

Output:
[1,1,2,3,4,4]

Key Idea:
Use a dummy (sentinel) node to simplify handling the head of the merged
list. Compare the current nodes of both lists, attach the smaller node
to the merged list, and continue until one list is exhausted. Finally,
attach the remaining nodes.

Approach:
1. Create a dummy node.
2. Create a pointer called current.
3. Compare the current nodes of both lists.
4. Attach the smaller node to current.next.
5. Move the pointer in the list from which the node was taken.
6. Move current forward.
7. After one list ends, attach the remaining nodes of the other list.
8. Return dummy.next.

Algorithm:
- Create dummy and current pointers.
- While both lists are not empty:
    - Compare list1.val and list2.val.
    - Attach the smaller node.
    - Advance the corresponding list.
    - Advance current.
- Attach the remaining list.
- Return dummy.next.

Time Complexity:
O(n + m)

Space Complexity:
O(1)

Key Takeaways:
- Dummy nodes eliminate special cases when building linked lists.
- Always move the pointer of the list whose node you used.
- After one list finishes, the remaining nodes are already sorted.
- This is one of the most common linked list interview patterns.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next