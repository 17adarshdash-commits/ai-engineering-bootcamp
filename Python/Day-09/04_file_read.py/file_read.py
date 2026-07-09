try:
    with open ("/Users/adarshdash17/Desktop/ai-engineering-bootcamp/Python/Day-09/04_file_read.py/sample.txt","r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found.")