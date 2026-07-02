inp = input("Enter string: ")
rev_inp = inp[::-1]

if inp == rev_inp:
    print("Palindrome")
else:
    print("Not Palindrome")