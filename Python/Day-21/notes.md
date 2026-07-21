1. What is the datetime module? Explain why applications use dates and times.
    - The datetime module is Python's built-in library for managing dates and times, which applications crucialy rely on to log system events, schedule automated tasks, calculate expirations, and localize global timestamps for users.

2. Difference between:
date
time
datetime
timedelta
Give one practical example of each.
    - date represents only a calendar day (e.g., tracking a user's birthdate like 2026-07-20).
    time represents only a specific time of day independent of any calendar (e.g., setting a daily morning alarm for 07:30:00).
    datetime combines both a specific day and time into a single point (e.g., stamping the exact moment a payment transaction occurs).
    timedelta represents a duration or the absolute span of time between two points (e.g., adding a 7-day expiration to a trial account).

3. Why should reports be generated automatically instead of manually?
    - Automating report generation eliminates human transcription errors, saves hours of manual labor, and ensures stakeholders receive critical, data-driven insights on a strict, predictable schedule.

4. What is code duplication? How can helper functions reduce duplicated code?
    - Code duplication occurs when the same block of logic is repeated across multiple places in a codebase, which helper functions eliminate by consolidating that shared logic into a single, reusable function that can be called whenever needed.

5. Explain the Single Responsibility Principle (SRP). Why is it useful when writing functions?
    - The Single Responsibility Principle dictates that a function should do exactly one thing and have only one reason to change, which makes code significantly easier to test, debug, and reuse without causing unintended side effects.