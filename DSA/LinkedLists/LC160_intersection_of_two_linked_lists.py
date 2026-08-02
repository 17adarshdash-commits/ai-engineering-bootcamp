"""
Problem:
160. Intersection of Two Linked Lists

Difficulty:
Easy

Pattern:
Two Pointers

Problem:
Given the heads of two singly linked lists, return the node at which
the two lists intersect. If the two linked lists have no intersection,
return None.

Key Idea:
Use two pointers. When one pointer reaches the end of its list,
redirect it to the head of the other list. After both pointers have
traversed both lists, they will either meet at the intersection or
both reach None.

Approach:
1. Initialize two pointers at the heads of each list.
2. Move each pointer one step at a time.
3. When a pointer reaches the end, redirect it to the other list.
4. Continue until both pointers are equal.
5. Return the meeting node.

Time Complexity:
O(m + n)

Space Complexity:
O(1)

Key Takeaways:
- Compare node references, not values.
- Redirecting pointers equalizes path lengths.
- No extra memory is required.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        currentA = headA
        currentB = headB

        while currentA != currentB:
            
            currentA = currentA.next if currentA else headB
            currentB = currentB.next if currentB else headA
        
        return currentA
            
        