numbers = []
def add_num():
    num = float(input("Enter number: "))
    numbers.append(num)
    print("Number added\n")

def done():
    print(f"Largest: {max(numbers)}")
    print(f"Smallest: {min(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers)}")
    print(f"Count: {len(numbers)}")


while True:
    choice = input("Type add to add number, done to exit: ")

    if choice == "add" or choice == "Add":
        add_num()
        continue

    elif choice == "done":
        done()
        print("Program complete!")
        break

    else:
        print("Invalid choice.")
        continue