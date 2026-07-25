1. What are the advantages of recursion?
    - The key advantages of recursion are cleaner and simpler code, natural problem-solving for hierarchical structures, and an easy way to handle divide-and-conquer algorithms.

2. What are its disadvantages?
    - The key disadvantages of recursion are high memory usage, slower execution speed, and the risk of program crashes.

3. What is stack overflow?
    - Stack overflow is a runtime error that happens when a program runs out of allocated call stack memory.

4. Explain recursion using the factorial example.
    - A factorial is the product of all positive integers less than or equal to a number. For example, the factorial of 4 (written as 4!) is 4 × 3 × 2 × 1 = 24.
    The Core Logic
    Recursion solves this by breaking the problem into a smaller version of itself:4! = 4 × 3!
    To find 3!, the program breaks it down again:3! = 3 × 2!
    This pattern continues until it reaches the smallest possible piece, which is 1.

5. Compare recursion and iteration.
    - Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem, whereas iteration uses loops to repeat a set of instructions until a condition is met.