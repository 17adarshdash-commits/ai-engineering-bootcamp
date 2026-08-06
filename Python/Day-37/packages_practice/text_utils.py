def count_words(text):
    return len(text.split())


def reverse_text(text):
    return text[::-1]


def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())
