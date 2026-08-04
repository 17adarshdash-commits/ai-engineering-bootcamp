def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Error: cannot divide {a} by zero.")
    else:
        print(f"{a} / {b} = {result}")
        return result
    finally:
        print("divide: operation attempted.\n")


def convert_to_int(value):
    try:
        result = int(value)
    except ValueError:
        print(f"Error: '{value}' cannot be converted to an integer.")
    else:
        print(f"'{value}' converted to int: {result}")
        return result
    finally:
        print("convert_to_int: operation attempted.\n")


def get_value(dictionary, key):
    try:
        result = dictionary[key]
    except KeyError:
        print(f"Error: key '{key}' not found in dictionary.")
    else:
        print(f"Value for key '{key}': {result}")
        return result
    finally:
        print("get_value: operation attempted.\n")


def get_item(lst, index):
    try:
        result = lst[index]
    except IndexError:
        print(f"Error: index {index} is out of range for the list.")
    else:
        print(f"Item at index {index}: {result}")
        return result
    finally:
        print("get_item: operation attempted.\n")


def open_file(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
    else:
        with f:
            content = f.read()
            print(f"Contents of '{filename}':\n{content}")
            return content
    finally:
        print("open_file: operation attempted.\n")


if __name__ == "__main__":
    print("--- Division ---")
    divide(10, 2)
    divide(5, 0)

    print("--- Integer Conversion ---")
    convert_to_int("42")
    convert_to_int("not_a_number")

    print("--- Dictionary Lookup ---")
    sample_dict = {"name": "Alice", "age": 30}
    get_value(sample_dict, "name")
    get_value(sample_dict, "email")

    print("--- List Indexing ---")
    sample_list = [10, 20, 30]
    get_item(sample_list, 1)
    get_item(sample_list, 10)

    print("--- File Opening ---")
    open_file("exception_handling_practice.py")
    open_file("nonexistent_file.txt")
