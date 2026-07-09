try:
    text = "Python is awesome."
    with open("/Users/adarshdash17/Desktop/ai-engineering-bootcamp/Python/Day-09/05_file_write.py/notes.txt","w") as f:
        f.write(text)
except FileNotFoundError:
    print("File not found.")