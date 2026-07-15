import datetime

current_time = datetime.datetime.now()

with open("log.txt","a") as file:
    file.write(f"{current_time} - Program Started\n")
    print("Log written successfully.")
