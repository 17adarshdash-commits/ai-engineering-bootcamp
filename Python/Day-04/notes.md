1. What is a loop?
    - A loop is used when we need to execute a set of instructions (block of code) repeatedly without having to rewrite the code again and again.

2. Difference between while and for.
    - A for loop is used when we execute a block of code a fixed number of times whereas a while loop is used when we don't know the number of iterations to run the block of code for.

3. How does range() work?
Explain:
range(5)
range(2, 8)
range(2, 10, 2)
    - In Python, the range() function generates an immutable sequence of integers on demand rather than storing them all in your computer's memory. It accepts up to three integer arguments—start, stop, and step—and is most commonly used to control the number of iterations in for loops.
    range(5): executes block of code 5 times
    range(2, 8): executes block of code from starting step 2 till ending step 8(exclusive).
    range(2, 10, 2): executes block of code from starting step 2 till ending step 10(exclusive) with step size 2.

4. Difference between:
break
continue
pass

    - break exits a loop, continue skips to the next turn of a loop, and pass does absolutely nothing except fill an empty space.

5. When should you use a while loop instead of a for loop?
    - When we know the number of times to execute a block of code, we should use for loops and when we dont know the number of times to execute a block of code, we use while loops.

6. What is an infinite loop? How can it happen?
    - An infinite loop is a loop that keeps running and never comes to a halt. It can happen when we dont specify the terminating condition.