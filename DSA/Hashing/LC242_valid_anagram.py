"""
LeetCode 242 - Valid Anagram

Pattern:
- Hash Map (Dictionary)

Difficulty:
- Easy
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n + m)
# Space Complexity: O(n)
# ==========================================================

class Solution(object):
    def isAnagram(self, s, t):

        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False

        scount = {}
        tcount = {}

        # Count frequency of each character in s
        for char in s:
            if char in scount:
                scount[char] += 1
            else:
                scount[char] = 1

        # Count frequency of each character in t
        for char in t:
            if char in tcount:
                tcount[char] += 1
            else:
                tcount[char] = 1

        return scount == tcount


"""
What I Learned
--------------

1. Dictionaries are useful for counting the frequency of elements.

2. Updating counts while traversing the string once is much more efficient
   than repeatedly using string.count().

3. If two strings are anagrams, their character-frequency dictionaries
   will be identical.

4. Always check simple edge cases first (like different string lengths)
   before doing extra work.

5. Hash Maps (dictionaries) are one of the most common interview patterns.
"""