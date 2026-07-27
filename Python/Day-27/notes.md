1. What is Binary Search on Answer?
    - Binary search on answer is an algorithmic technique used to find a target value by performing a binary search over a range of possible solutions rather than through a direct array. 

2. Iteration vs Recursion
    - Iteration and recursion are two different programming methods used to execute a set of instructions repeatedly. Iteration uses a loop structure (like for or while), whereas recursion occurs when a function calls itself to solve a smaller piece of the same problem.

3. Binary Search Variations
Explain the difference between:
Standard Binary Search
First Occurrence
Last Occurrence
Peak Element
Binary Search on Answer
    - Binary search variations differ primarily in their target goals, boundary updates, and how they handle duplicate values.
    Standard Binary Search: Finds any single instance of a target value in a sorted array and returns its index immediately.
    First Occurrence: Finds the very first instance of a target value when duplicates exist by continuing to search the left half even after finding a match.
    Last Occurrence: Finds the very last instance of a target value when duplicates exist by continuing to search the right half even after finding a match.
    Peak Element: Finds a local maximum in an unsorted or partially sorted array by comparing a midpoint to its neighbors to determine which direction climbs upward.
    Binary Search on Answer: Finds an optimal value from a continuous range of possible solutions instead of searching through index positions in a concrete array.

4. Why must every Binary Search maintain a valid search space? Explain why we never discard a possible answer.
    - Every Binary Search must maintain a valid search space because discarding a valid range can cause the algorithm to return an incorrect result or loop forever. The logic relies entirely on the guarantee that the target value exists exclusively within the active boundaries.

5. Time Complexity Review
Write the complexity of:
Arrays
Hash Maps
Stack
Queue
Binary Search
    - Arrays offer \(O(1)\) access but \(O(N)\) search, insertion, and deletion; Hash Maps average \(O(1)\) for all operations; Stacks and Queues offer \(O(1)\) modifications at their ends but \(O(N)\) search; and Binary Search finds elements in \(O(\log N)\) time.