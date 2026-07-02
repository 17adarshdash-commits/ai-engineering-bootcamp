"""
LeetCode: 125
Title: Valid Palindrome

Difficulty: Easy

Pattern:
- Two Pointers

Topics:
- String
- Two Pointers
"""

# ==========================================================
# Optimized Solution (Two Pointers)
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================================

class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1

        while l < r:

            # Skip non-alphanumeric characters from the left
            if not s[l].isalnum():
                l += 1
                continue

            # Skip non-alphanumeric characters from the right
            if not s[r].isalnum():
                r -= 1
                continue

            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


"""
What I Learned
--------------

1. Two Pointers is an efficient technique for comparing values from
   both ends of a string or array.

2. The left and right pointers move toward each other until they meet.

3. Skip invalid characters before comparing.

4. Compare characters without considering case using lower().

5. This solution avoids creating another string and therefore uses
   O(1) extra space.

6. The order of operations is important:
   - Skip invalid left character
   - Skip invalid right character
   - Compare characters
   - Move both pointers
"""