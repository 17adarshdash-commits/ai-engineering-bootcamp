"""
regex_practice.py

Practice with the re module: match(), search(), findall(), and sub().
"""

import re


def is_valid_email(text):
    """Validate a simple email pattern: word@word.word"""
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
    return re.match(pattern, text) is not None


def find_all_numbers(sentence):
    """Find all numbers (integers or decimals) in a sentence."""
    pattern = r"\d+\.?\d*"
    return re.findall(pattern, sentence)


def collapse_spaces(text):
    """Replace multiple consecutive spaces with a single space."""
    pattern = r" {2,}"
    return re.sub(pattern, " ", text)


def find_capitalized_words(text):
    """Extract all words that begin with a capital letter."""
    pattern = r"\b[A-Z][a-zA-Z]*\b"
    return re.findall(pattern, text)


def contains_digit(text):
    """Check if a string contains at least one digit anywhere (search)."""
    return re.search(r"\d", text) is not None


if __name__ == "__main__":
    print("=" * 50)
    print("Testing re.match() -> is_valid_email()")
    print("=" * 50)
    for email in ["adarsh@example.com", "not-an-email", "user.name@sub.domain.co"]:
        print(f"{email!r:35} -> {is_valid_email(email)}")

    print()
    print("=" * 50)
    print("Testing re.findall() -> find_all_numbers()")
    print("=" * 50)
    sentence = "I bought 3 apples, 12 oranges, and 4.5 kg of rice for 250.75 rupees."
    print(f"Sentence: {sentence}")
    print(f"Numbers found: {find_all_numbers(sentence)}")

    print()
    print("=" * 50)
    print("Testing re.sub() -> collapse_spaces()")
    print("=" * 50)
    messy = "This   sentence has    way too   many    spaces."
    print(f"Before: {messy!r}")
    print(f"After:  {collapse_spaces(messy)!r}")

    print()
    print("=" * 50)
    print("Testing re.findall() -> find_capitalized_words()")
    print("=" * 50)
    text = "Adarsh went to Paris with John to visit the Eiffel Tower in June."
    print(f"Text: {text}")
    print(f"Capitalized words: {find_capitalized_words(text)}")

    print()
    print("=" * 50)
    print("Testing re.search() -> contains_digit()")
    print("=" * 50)
    for sample in ["hello world", "room 42", "no digits here"]:
        print(f"{sample!r:20} -> contains digit: {contains_digit(sample)}")
