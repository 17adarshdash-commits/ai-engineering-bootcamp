inp = input("Enter email id: ")

split = inp.find('@')
username = inp[0:split]
domain = inp[split + 1: ]

print(f"Username: {username}")
print(f"Domain: {domain}")