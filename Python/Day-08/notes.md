1. What is an exception? Why do exceptions occur?
    - An exception is an event that interrupts the flow of a program, they occur when an unexpected event disrupts the normal flow of a program’s instructions.

2. Explain

* try
* except
* else
* finally
    - try: Runs the initial code that might cause an error.
    except: Executes fallback code only if an error occurs inside the try block
    else: Runs code only if the try block completes successfully without any errors.
    finally: Always runs at the very end, regardless of whether an error happened or not.

3. Difference between ValueError and TypeError:
    - TypeError: You passed the wrong type of object (e.g., trying to do math on a word).
    ValueError: You passed the correct type, but the content makes no sense (e.g., passing a word to a function that only accepts words shaped like numbers).

4. What does raise do? When should we use it?
    - raise forces an exception to occur manually, intentionally stopping the normal flow of the program. We use raise to intentionally stop the program when data or conditions violate your specific business rules.

5. Why is exception handling important? Give one real-life example.
    - Exception handling prevents a single error from crashing your entire application, allowing the system to recover gracefully or fail safely.
    Real-Life Example: An E-commerce Checkout