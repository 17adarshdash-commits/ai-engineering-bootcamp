"""
Problem:
876. Middle of the Linked List

Difficulty:
Easy

Pattern:
Fast & Slow Pointer

Problem:
Given the head of a singly linked list, return the middle node.
If there are two middle nodes, return the second middle node.

Example:

Input:
1 -> 2 -> 3 -> 4 -> 5

Output:
3

Input:
1 -> 2 -> 3 -> 4 -> 5 -> 6

Output:
4

Key Idea:
Use two pointers moving at different speeds.
The slow pointer moves one node at a time while the fast pointer moves two nodes.
When the fast pointer reaches the end of the list, the slow pointer will be positioned at the middle node.

Approach:
1. Initialize slow and fast pointers at the head.
2. Move slow one step and fast two steps.
3. Continue until the fast pointer reaches the end.
4. Return the slow pointer.

Algorithm:
- slow = head
- fast = head
- while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
- return slow

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Takeaways:
- Fast & Slow Pointer finds the middle in a single traversal.
- No extra memory is required.
- For even-length lists, this implementation returns the second middle node.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        current = head

        slow = current
        fast = current

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        