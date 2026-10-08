"""
LeetCode 49 - Group Anagrams

Pattern:
- Hash Map (Dictionary) + Strings

Difficulty:
- Medium
"""

# ==========================================================
# Optimized Solution
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
#   n = number of strings, k = average string length
# ==========================================================

class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            # Anagrams share the same sorted character sequence,
            # so the sorted word makes a natural grouping key.
            key = "".join(sorted(word))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())


"""
What I Learned
--------------

1. Words that are anagrams always produce the same string when sorted
   (e.g. "eat" -> "aet", "tea" -> "aet", "ate" -> "aet").

2. That sorted string makes a perfect hash map key for grouping anagrams
   together in a single pass.

3. Sorting each word costs O(k log k), so sorting all n words costs
   O(n * k log k) overall.

4. This is a common pattern: when two inputs are "equivalent" under some
   transformation, use that transformation's output as a hash map key.
"""
