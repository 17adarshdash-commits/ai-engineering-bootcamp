import random
num = random.randint(1,100)
while True:
    guess = int(input("Enter your guess: "))

    if num == guess:
        print("Correct guess!")
        break

    elif num > guess:
        print("Guess is too low.")
        continue

    else:
        print("Guess is too high.")
        continue

print("Game over!")


    