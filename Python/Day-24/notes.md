1. What is recursion? How is recursion different from iteration?
    - Recursion is a programming technique where a function calls itself to solve a smaller, self-similar instance of the same problem. Iteration, on the other hand, uses loops (like for or while) to repeatedly execute a block of code until a specific condition is met.

2. What is a base case? Why is it necessary?
    - A base case is the specific condition in a recursive function that stops the function from calling itself. It provides a direct, non-recursive answer for the smallest or simplest input.

3. What happens if a recursive function has no base case?
    - If a recursive function has no base case, it creates an infinite loop of function calls that quickly crashes your program.

4. Explain the call stack. How does Python execute recursive function calls?
    - The call stack is a dedicated chunk of memory that Python uses to keep track of active functions. It operates on a Last-In, First-Out (LIFO) basis, meaning the last function called is the first one to finish and leave the stack.

5. When should recursion be preferred over loops? Give two examples.
    - Recursion is preferred over loops when navigating deeply nested, branching data structures—like file directories or XML files—or when applying divide-and-conquer algorithms like Merge Sort, because it naturally models the problem's structure without requiring complex manual tracking.