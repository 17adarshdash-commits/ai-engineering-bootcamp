"""
Problem: 875. Koko Eating Bananas

Difficulty:
Medium

Pattern:
Binary Search on Answer

Problem:
Koko loves eating bananas. There are several piles of bananas, and the ith pile has piles[i] bananas.
The guards have gone away and will return in h hours.

Koko can decide her eating speed K (bananas per hour). Each hour, she chooses one pile and eats up to K bananas.
If the pile has fewer than K bananas, she eats all of them and waits until the next hour.

Return the minimum integer eating speed K such that she can eat all the bananas within h hours.

Example:
Input:
piles = [3,6,7,11]
h = 8

Output:
4

Key Idea:
Instead of searching for an element in an array, Binary Search is performed over the range of all possible eating speeds.

If a speed works, try a smaller speed.
If a speed does not work, try a larger speed.

Approach:
1. Set the search space from 1 to max(piles).
2. Pick a middle speed.
3. Calculate the total hours needed at that speed.
4. If Koko finishes within h hours, search the left half.
5. Otherwise, search the right half.
6. Return the minimum valid speed.

Algorithm:
- low = 1
- high = max(piles)
- while low < high:
    - mid = (low + high) // 2
    - calculate hours required
    - if hours <= h:
        high = mid
    - else:
        low = mid + 1
- return low

Time Complexity:
O(n * log(max(piles)))

Space Complexity:
O(1)

Key Takeaways:
- Binary Search can be used on a range of possible answers.
- The answer space must be monotonic.
- If a speed works, all larger speeds also work.
- If a speed fails, all smaller speeds fail.
"""


class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            hours = sum((pile + mid - 1) // mid for pile in piles)

            if hours <= h:
                high = mid
            else:
                low = mid + 1

        return low