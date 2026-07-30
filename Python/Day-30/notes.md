1. Dummy (Sentinel) Node
Learn:
What a dummy node is
Why interviewers love it
How it simplifies edge cases
Removing the head node
Inserting before the head
Eliminating special cases
Example:
Dummy → 1 → 2 → 3
instead of
Head → 1 → 2 → 3
    - A dummy (sentinel) node is a temporary placeholder node placed before the true head of a linked list. Interviewers love it because it eliminates special conditional checks for edge cases, making head deletions, head insertions, and empty list management uniform across the entire data structure.

2. Removing Nodes
Understand:
Removing the first node
Removing the last node
Removing a middle node
Removing consecutive nodes
Why pointer order matters
    - Removing nodes from a linked list requires precise pointer updates to prevent breaking the chain or causing memory leaks.Understanding Node RemovalRemoving the First Node: Break the link from the head pointer and move it to the second node.Removing the Last Node: Traverse to the second-to-last node and set its next pointer to null.Removing a Middle Node: Link the predecessor node directly to the successor node, bypassing the target.Removing Consecutive Nodes: Use a loop to continuously bridge the current valid node to the next non-target node.

3. Linked List Traversal Patterns
Study:
Simple traversal
Searching
Counting
Finding previous node
Two-pointer traversal
    - Linked list traversal patterns form the foundation of almost every complex list manipulation algorithm. Mastery of these patterns ensures you can navigate, inspect, and track positions within a sequential structure efficiently without losing node references.

4. Common Interview Mistakes
Examples:
Losing the next node
Forgetting to update head
Null pointer errors
Infinite loops
Returning the wrong node
    - Avoiding common pointer bugs is the difference between passing and failing a technical interview. Because linked lists do not have indices, a single misplaced line of code can instantly crash your program or corrupt your data

    