secret = 7
num = int(input("Enter number: "))
while num != secret:
    print("Wrong guess!, try again")
    num = int(input("Enter number: "))
print("Congrats, you guessed correctly!")