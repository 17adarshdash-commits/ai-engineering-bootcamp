"""
LeetCode: 290
Title: Word Pattern
Difficulty: Easy
Pattern: Hash Map (One-to-One Mapping)
Topics: Hash Map, String

Problem:
Given a pattern and a string s, determine if s follows the same pattern.

A bijection must exist between characters in the pattern and words in
the string. Each pattern character maps to exactly one unique word,
and each word maps to exactly one pattern character.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# -------------------------
# My Solution
# -------------------------

class Solution(object):
    def wordPattern(self, pattern, s):

        words = s.split()
        map_pattern_to_word = {}
        seen_words = set()

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p in map_pattern_to_word:
                if map_pattern_to_word[p] != w:
                    return False
            else:
                if w in seen_words:
                    return False

                map_pattern_to_word[p] = w
                seen_words.add(w)

        return True


# -------------------------
# What I Learned
# -------------------------

"""
1. The same Hash Map pattern can solve different problems.
2. A dictionary stores the mapping between pattern characters and words.
3. A set prevents multiple pattern characters from mapping to the same word.
4. Splitting a sentence into words allows us to compare each word with its pattern character.
5. Reusing known patterns is more important than memorizing solutions.
"""


# -------------------------
# Pattern Recognition
# -------------------------

"""
Pattern:
Hash Map (One-to-One Mapping)

Use this pattern when:
- One value must uniquely correspond to another.
- Existing mappings must remain consistent.
- Duplicate target mappings are not allowed.

Examples:
- LC205 Isomorphic Strings
- LC290 Word Pattern
"""