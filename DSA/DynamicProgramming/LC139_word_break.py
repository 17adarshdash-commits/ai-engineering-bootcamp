"""
LeetCode 139. Word Break
Pattern: Dynamic Programming

Given a string s and a dictionary of strings wordDict, return True if s can be
segmented into a space-separated sequence of one or more dictionary words.

The same word in the dictionary may be reused multiple times in the
segmentation.

Example:
    s = "leetcode", wordDict = ["leet", "code"]
    -> True  ("leet" + "code")

    s = "applepenapple", wordDict = ["apple", "pen"]
    -> True  ("apple" + "pen" + "apple")

    s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    -> False

DP state:
    dp[i] = True if s[:i] can be segmented into words from wordDict.

Base case:
    dp[0] = True  (the empty prefix is trivially "segmentable")

Transition:
    dp[i] = True if there exists some j < i such that
            dp[j] is True AND s[j:i] is in wordDict

Answer:
    dp[len(s)]

Time complexity:  O(n^2) where n = len(s)  (n positions * up to n substrings each)
Space complexity: O(n) for the dp array (plus O(1) lookup thanks to the word set)
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    word_set = set(word_dict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True  # empty prefix is always breakable

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # no need to check other j once dp[i] is True

    return dp[n]


if __name__ == "__main__":
    tests = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("", ["a"], True),
        ("a", ["b"], False),
        ("aaaaaaa", ["aaaa", "aaa"], True),
    ]

    for s, word_dict, expected in tests:
        result = word_break(s, word_dict)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] word_break({s!r}, {word_dict}) = {result} (expected {expected})")
