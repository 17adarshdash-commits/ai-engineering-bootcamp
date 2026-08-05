def logger(func):
    def wrapper(*args, **kwargs):
        print("Starting function...")
        result = func(*args, **kwargs)
        print("Finished function...")
        return result
    return wrapper


@logger
def say_hello():
    print("Hello!")


@logger
def calculate_sum(a, b):
    print(f"Sum: {a + b}")


if __name__ == "__main__":
    say_hello()
    calculate_sum(7, 8)
