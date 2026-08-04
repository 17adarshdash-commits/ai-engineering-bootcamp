class InvalidAgeError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


def validate_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is below the minimum required age of 18.")
    return True


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw {amount}; balance is only {balance}."
        )
    return balance - amount


if __name__ == "__main__":
    try:
        validate_age(21)
        print("validate_age(21) passed")
    except InvalidAgeError as e:
        print(f"validate_age(21) failed: {e}")

    try:
        validate_age(15)
        print("validate_age(15) passed")
    except InvalidAgeError as e:
        print(f"validate_age(15) failed: {e}")

    try:
        new_balance = withdraw(1000, 200)
        print(f"withdraw(1000, 200) passed, new balance: {new_balance}")
    except InsufficientFundsError as e:
        print(f"withdraw(1000, 200) failed: {e}")

    try:
        new_balance = withdraw(500, 700)
        print(f"withdraw(500, 700) passed, new balance: {new_balance}")
    except InsufficientFundsError as e:
        print(f"withdraw(500, 700) failed: {e}")
