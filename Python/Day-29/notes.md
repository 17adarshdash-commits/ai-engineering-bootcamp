1. Fast & Slow Pointer Technique
Cover:
What is the Fast & Slow Pointer pattern?
Why is it useful?
Why does one pointer move twice as fast?
Advantages over counting nodes.
Common interview problems.
    - The Fast & Slow Pointer technique, also known as Hare & Tortoise algorithm, uses two pointers traversing a data structure (usually a linked list or array) at different speeds. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.Why is it Useful?
    It detects cycles and finds specific nodes in a single pass without extra memory. It solves structural problems in linear time (O(N)) while maintaining constant space (O(1)). This makes it highly optimized for memory-constrained environments.
    Why Does One Pointer Move Twice as Fast?
    Moving the fast pointer at exactly twice the speed (2x) creates a predictable relative speed of 1x between the two pointers.
    In a cycle: The distance between them decreases by exactly 1 node per step. This guarantees they will eventually land on the exact same node without skipping over each other.Without a cycle: When the fast pointer reaches the end (N), the slow pointer is mathematically guaranteed to be exactly at the midpoint (N/2).Advantages Over Counting NodesZero Extra Space: Unlike hash tables that store visited nodes (O(N) space), this pattern uses only two pointers (O(1) space).Single Pass Efficiency: Traditional methods require counting all nodes first, then traversing a second time to find the target. The two-pointer approach finds the target in a single pass.Handles Infinite Loops Safely: If you try to count nodes in a cyclic list, your code will crash from an infinite loop. The fast/slow pattern detects the loop safely during the first iteration.Common Interview ProblemsLinked List Cycle Detection: Determine if a linked list has a loop (LeetCode 141).Find the Midpoint: Locate the middle node of a linked list in one pass (LeetCode 876).Find the Cycle Start: Determine the exact node where a loop begins (LeetCode 142).Happy Number: Determine if a number eventually reduces to 1 when replaced by the sum of squares of its digits (LeetCode 202).Palindrome Linked List: Check if a linked list reads the same forward and backward by finding the middle and reversing the second half (LeetCode 234).

2. Finding the Middle Node
Explain:
Naive approach
Optimized approach
Complexity comparison
    - Naive Approach: The naive approach uses a two-pass strategy to find the middle element.Pass 1: Traverse the entire linked list from the head to the end to count the total number of nodes (\(N\)).Calculate: Divide the total count by two (\(\lfloor N/2 \rfloor\)) to find the index of the middle node.Pass 2: Start again from the head and move forward exactly \(\lfloor N/2 \rfloor\) times to reach and return the middle node.
    Optimized Approach: The optimized approach applies the Fast & Slow Pointer pattern to find the middle node in a single pass.Initialization: Place both the slow and fast pointers at the head of the linked list.Traversal: Advance the slow pointer by 1 node and the fast pointer by 2 nodes in each iteration.Termination: Stop the loop when the fast pointer reaches the end of the list (null) or the last node.Result: Because the fast pointer travels twice as fast, the slow pointer will be positioned exactly at the middle node when the loop terminates.

3. Detecting a Cycle
Explain:
What is a cycle?
Why can a normal traversal loop forever?
Floyd's Cycle Detection Algorithm (Tortoise and Hare)
Why fast and slow eventually meet.
    - The Fast & Slow Pointer (Tortoise and Hare) technique uses two pointers moving at different speeds—typically 1x and 2x—to solve structural data problems in a single pass while using optimal O(1) constant space. When finding a midpoint, this approach is superior to the naive two-pass counting method because it locates the exact center node on the very first run; the slow pointer sits precisely at the middle index (N/2) the moment the fast pointer reaches the end (N). When used to detect cycles—which are infinite loops caused by a node pointing backward instead of to null—the algorithm safely prevents code crashes because the fast pointer reduces the gap between them by exactly 1 node per iteration, mathematically guaranteeing they will land on the exact same node rather than skipping over each other. This high-efficiency, single-pass advantage makes it the definitive strategy for common interview problems like cycle detection (LeetCode 141), finding the middle node (LeetCode 876), and identifying cycle entry points (LeetCode 142).

4. Common Linked List Patterns
Briefly describe:
Reverse
Fast & Slow
Dummy Node
Merge Lists
    - Common Linked List Patterns
    Reverse: Flips the direction of the next pointers in a list by using three tracking variables (prev, curr, next_node) to update connections in-place in \(O(N)\) time and \(O(1)\) space without creating new nodes.
    Fast & Slow: Advances two pointers at different speeds (1x and 2x) to find the middle node, detect structural cycles, or identify loop entry points in a single pass without storing visited nodes in a hash map.
    Dummy Node: Uses a placeholder node at the beginning of a new or modified list to simplify edge cases, eliminate redundant null checks, and handle head insertions or deletions uniformly.
    Merge Lists: Combines two sorted linked lists into a single sorted list by using a pointer to compare the front nodes of each list and stitch them together sequentially.