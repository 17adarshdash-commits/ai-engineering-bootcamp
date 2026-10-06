"""
Problem: 98. Validate Binary Search Tree

Difficulty:
Medium

Pattern:
Trees + Recursion

Problem:
Given the root of a binary tree, determine if it is a valid binary search
tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with values strictly less
  than the node's value.
- The right subtree of a node contains only nodes with values strictly
  greater than the node's value.
- Both the left and right subtrees must also be binary search trees.

Example:

Input:
    2
   / \
  1   3

Output:
True

Input:
    5
   / \
  1   4
     / \
    3   6

Output:
False
(4's left subtree has a node with value 3, but 4 is in 5's right subtree,
so every node there must be > 5. More directly: node 4's right child is 6,
which is fine, but node 4 itself must be > 5, which it isn't.)

Key Idea:
A node isn't just checked against its direct parent - it must fall within
the bounds set by every ancestor above it. Pass down a valid (low, high)
range as we recurse, and narrow that range on each step down.

Approach:
1. Recurse with a (low, high) bound, starting at (-infinity, infinity).
2. If the current node is None, it's valid (empty subtree).
3. If the current node's value isn't strictly within (low, high), return False.
4. Recurse left with bound (low, node.val) - left subtree must stay below node.val.
5. Recurse right with bound (node.val, high) - right subtree must stay above node.val.
6. Valid only if both sides are valid.

Algorithm:
- def validate(node, low, high):
-     if node is None:
-         return True
-     if not (low < node.val < high):
-         return False
-     return validate(node.left, low, node.val) and validate(node.right, node.val, high)
- return validate(root, float("-inf"), float("inf"))

Time Complexity:
O(n)

Space Complexity:
O(h)
(h = height of the tree, for the recursion stack)

Key Takeaways:
- Checking only against the immediate parent is not enough - bounds must
  propagate from every ancestor.
- Carrying (low, high) down the recursion encodes all ancestor constraints
  without extra bookkeeping.
- Comparisons must be strict (<, not <=) since BST values are unique and
  duplicates on either side are invalid.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isValidBST(self, root):
        def validate(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return (
                validate(node.left, low, node.val)
                and validate(node.right, node.val, high)
            )

        return validate(root, float("-inf"), float("inf"))
