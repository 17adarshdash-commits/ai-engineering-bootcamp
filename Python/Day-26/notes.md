1. What is Divide and Conquer?
Explain the three stages:
Divide
Conquer
Combine
Give two examples.
    - Divide and Conquer is an algorithmic strategy that solves a large problem by breaking it into smaller sub-problems (Divide), solving those sub-problems recursively (Conquer), and merging their results into a final solution (Combine), with classic examples being Merge Sort and Binary Search.

2. What is Tail Recursion? How is it different from normal recursion?
    - Tail recursion is a specific type of recursion where the recursive call is the very last operation performed by the function, differing from normal recursion because it allows the compiler to optimize memory by reusing a single stack frame instead of keeping multiple active frames in memory.

3. Why is Fibonacci recursion inefficient? Explain repeated subproblems.
    - Fibonacci recursion is highly inefficient because it calculates the same values repeatedly, meaning the function solves identical subproblems over and over again and creates an exponentially growing tree of redundant calculations.

4. What is Memoization? How does it improve recursive solutions?
    - Memoization is an optimization technique that stores the results of expensive function calls in a cache, improving recursive solutions by immediately returning the cached result whenever the same inputs occur again to eliminate redundant calculations.

5. Compare
Normal recursion
Tail recursion
Memoization
    - While normal recursion adds a new frame to the call stack for every step and tail recursion optimizes memory by reusing a single stack frame, memoization completely avoids redundant steps across both methods by storing and reusing past calculation results.
    