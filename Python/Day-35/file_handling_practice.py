def write_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)


def read_file(filename):
    with open(filename, "r") as f:
        return f.read()


def read_lines(filename):
    with open(filename, "r") as f:
        return f.readlines()


def append_file(filename, text):
    with open(filename, "a") as f:
        f.write(text)


def count_lines(filename):
    with open(filename, "r") as f:
        return len(f.readlines())


def count_words(filename):
    with open(filename, "r") as f:
        return len(f.read().split())


if __name__ == "__main__":
    sample_file = "sample.txt"

    print("Writing text...")
    write_file(sample_file, "Hello, this is the first line.\nThis is the second line.\n")
    print(read_file(sample_file))

    print("Reading entire file...")
    print(read_file(sample_file))

    print("Reading line by line...")
    for line in read_lines(sample_file):
        print(line.rstrip())

    print("Appending more text...")
    append_file(sample_file, "This is an appended third line.\n")
    print(read_file(sample_file))

    print("Counting lines...")
    print(count_lines(sample_file))

    print("Counting words...")
    print(count_words(sample_file))
