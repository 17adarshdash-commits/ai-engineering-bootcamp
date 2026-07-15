try:
    filename = input("Enter filename: ")

    with open(filename,"r") as file:
        content = file.read()

    num_lines = len(content.splitlines())
    num_words = len(content.split())
    num_chars = len(content)

    print(f"\n--- Analysis of '{filename}' ---")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of characters: {num_chars}")
    print("-" * 30)

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
    print("Please make sure the file is in the same folder as this script and try again.")