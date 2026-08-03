"""
Problem:
19. Remove Nth Node From End of List

Difficulty:
Medium

Pattern:
Two Pointers, Dummy Node

Problem:
Given the head of a linked list, remove the nth node from the end of the
list and return its head.

Example:

Input:
head = [1,2,3,4,5]
n = 2

Output:
[1,2,3,5]

Key Idea:
Use a dummy node to simplify removing the head node. Maintain two pointers,
fast and slow. Move the fast pointer n+1 steps ahead, then move both pointers
together until fast reaches the end. The slow pointer will then be positioned
immediately before the node that needs to be removed.

Approach:
1. Create a dummy node pointing to the head.
2. Initialize fast and slow pointers at the dummy node.
3. Move the fast pointer n+1 steps ahead.
4. Move both pointers one step at a time until fast reaches None.
5. Remove slow.next by linking it to slow.next.next.
6. Return dummy.next.

Algorithm:
- Create a dummy node.
- Set fast = slow = dummy.
- Advance fast n+1 steps.
- Move fast and slow together until fast becomes None.
- Remove the target node.
- Return dummy.next.

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- Dummy nodes simplify deleting the head node.
- Two pointers allow the problem to be solved in a single traversal.
- Keeping a fixed gap between pointers is a common interview technique.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast pointer n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the target node
        slow.next = slow.next.next

        return dummy.next