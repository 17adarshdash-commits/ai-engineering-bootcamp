from calculator import add, subtract, multiply, divide
from text_utils import count_words, reverse_text, capitalize_words


def main():
    # calculator demo
    print("add(4, 5) =", add(4, 5))
    print("subtract(10, 3) =", subtract(10, 3))
    print("multiply(6, 7) =", multiply(6, 7))
    print("divide(20, 4) =", divide(20, 4))

    try:
        divide(5, 0)
    except ValueError as e:
        print("divide(5, 0) raised ValueError:", e)

    # text_utils demo
    sample = "the quick brown fox jumps over the lazy dog"
    print("count_words:", count_words(sample))
    print("reverse_text:", reverse_text(sample))
    print("capitalize_words:", capitalize_words(sample))


if __name__ == "__main__":
    main()
