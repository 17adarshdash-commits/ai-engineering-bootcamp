1. Regular Expressions (Regex)
Learn:
What is Regex?
Why Regex exists
re module
match()
search()
findall()
sub()
Common regex patterns
Raw strings (r"")
    - A regex (regular expression) is a mini language for describing patterns in text; it exists because plain string methods (`in`, `.find()`, `.split()`) can't express "one or more digits" or "an email-shaped string" without a lot of manual code. Python's `re` module provides `match()` (checks the start of a string), `search()` (finds the first match anywhere), `findall()` (returns all matches as a list), and `sub()` (replaces matches). Raw strings (`r"..."`) stop Python from interpreting backslashes as escape sequences, so patterns like `r"\d+"` mean what they look like instead of colliding with string escapes like `\n`.

2. Command-Line Arguments
Understand:
sys.argv
Passing arguments
Reading command-line input
Basic validation
Why CLI arguments are useful
    - `sys.argv` is a list of strings holding the command used to launch a script: `sys.argv[0]` is the script name, and everything after is the arguments the user typed (e.g. `python script.py name age` gives `sys.argv == ["script.py", "name", "age"]`). Reading and validating `len(sys.argv)` before indexing avoids `IndexError` when arguments are missing. CLI arguments matter because they let a script be configured and automated (piped into other tools, scheduled, scripted) without editing code or prompting interactively.

3. Logging
Study:
Why logging exists
logging module
Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
Logging to console
Logging to file
Why logging is better than print()
    - Logging exists to record what a running program is doing in a structured, filterable, persistent way. The `logging` module defines five increasing severity levels - DEBUG (diagnostic detail), INFO (normal events), WARNING (something unexpected but not fatal), ERROR (a failure), CRITICAL (the program may not continue) - and a `Handler` can send records to the console, a file, or both at once. Logging beats `print()` because it can be turned on/off or filtered by level without touching call sites, includes timestamps/severity/source automatically, and can persist to a file for later debugging instead of vanishing with the terminal.

4. Best Practices
Learn:
Don't use regex when simple string methods are clearer.
Use raw strings for regex patterns.
Log meaningful events, not everything.
Validate command-line arguments.
    - Reach for regex only when a pattern genuinely needs it (variable-length matches, alternation, extraction) - `"@" in email` beats a regex for a trivial check. Always write regex patterns as raw strings to avoid escape-sequence bugs. Log events that matter for understanding or debugging behavior (state changes, errors, key decisions), not every line, or the log becomes noise no one reads. Always check argument count and types before using `sys.argv` values, and fail with a clear message rather than crashing.

5. Real-World Applications
Understand where these topics are used:
Email validation
Phone number validation
Log files
Automation scripts
CLI utilities
Server applications
    - Regex powers form validation (emails, phone numbers, postal codes) and text extraction/cleanup pipelines. `sys.argv`-style CLI arguments drive automation scripts, build tools, and command-line utilities (like `git`, `pip`) that take configuration from the command line instead of a UI. Logging is essential in long-running server applications, background jobs, and automation scripts, where a persistent, timestamped record of events is the only way to diagnose issues after the fact.
