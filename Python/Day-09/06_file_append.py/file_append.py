try:
    text = "I am learning File Handling."
    with open("/Users/adarshdash17/Desktop/ai-engineering-bootcamp/Python/Day-09/05_file_write.py/notes.txt","a") as f:
        f.write(text)
except FileNotFoundError:
    print("File not found.")