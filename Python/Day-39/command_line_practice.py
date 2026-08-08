"""
command_line_practice.py

Practice with sys.argv: printing arguments, counting them, greeting a
user, and handling missing arguments gracefully.

Usage:
    python command_line_practice.py
    python command_line_practice.py Adarsh
    python command_line_practice.py Adarsh Engineer
"""

import sys


def print_all_arguments(args):
    """Print the script name and every argument passed."""
    print(f"Script name: {args[0]}")
    if len(args) == 1:
        print("No additional arguments were passed.")
        return

    for index, arg in enumerate(args[1:], start=1):
        print(f"Argument {index}: {arg}")


def count_arguments(args):
    """Count arguments passed, excluding the script name itself."""
    return len(args) - 1


def greet_user(args):
    """Greet a user using the first command-line argument, if provided."""
    if len(args) < 2:
        print("No name provided. Usage: python command_line_practice.py <name>")
        return

    name = args[1]
    print(f"Hello, {name}! Welcome to the command-line practice script.")


def main():
    args = sys.argv

    print("=" * 50)
    print("All Command-Line Arguments")
    print("=" * 50)
    print_all_arguments(args)

    print()
    print("=" * 50)
    print("Argument Count")
    print("=" * 50)
    print(f"Number of arguments (excluding script name): {count_arguments(args)}")

    print()
    print("=" * 50)
    print("Greeting")
    print("=" * 50)
    greet_user(args)


if __name__ == "__main__":
    main()
