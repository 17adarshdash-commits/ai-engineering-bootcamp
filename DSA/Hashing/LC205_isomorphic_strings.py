"""
LeetCode: 205
Title: Isomorphic Strings
Difficulty: Easy
Pattern: Hash Map (One-to-One Mapping)
Topics: Hash Map, String

Problem:
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced
to get t.

Each character must map to exactly one other character, and no
two characters may map to the same character.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# -------------------------
# My Solution
# -------------------------

class Solution(object):
    def isIsomorphic(self, s, t):
        dict_s_to_t = {}
        seen_t = set()

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char in dict_s_to_t:
                if dict_s_to_t[s_char] != t_char:
                    return False
            else:
                if t_char in seen_t:
                    return False

                dict_s_to_t[s_char] = t_char
                seen_t.add(t_char)

        return True


# -------------------------
# What I Learned
# -------------------------

"""
1. A Hash Map can be used to maintain a one-to-one mapping.
2. A set helps ensure that two different keys do not map to the same value.
3. Always verify an existing mapping before creating a new one.
4. Early length checks simplify the solution.
"""

# -------------------------
# Pattern Recognition
# -------------------------

"""
Pattern:
Hash Map (One-to-One Mapping)

Use this pattern when:
- One value must uniquely correspond to another.
- Existing mappings need to stay consistent.
- Duplicate target mappings are not allowed.

Examples:
- LC205 Isomorphic Strings
- LC290 Word Pattern
"""