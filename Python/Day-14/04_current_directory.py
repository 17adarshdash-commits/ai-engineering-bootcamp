import os

print(f"Current directory: {os.getcwd()}")

path = input("Enter filename: ")

if os.path.exists(path):
    print("File exists.")
else:
    print("File doesn't exist.")