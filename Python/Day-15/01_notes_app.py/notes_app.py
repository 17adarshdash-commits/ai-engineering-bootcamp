def add_notes():
    notes_to_add = input("Enter notes to be added: ")
    with open("notes.txt","a") as file:
        file.write(f"{notes_to_add}\n")
        print("Notes added.\n")

def view_notes():
    with open("notes.txt","r") as file:
        content = file.read()
        print(f"{content}\n")

while True:

    choice = int(input("1. Add Note\n2. View Notes\n3. Exit\nEnter choice: "))
    if choice == 1:
        add_notes()
        continue

    elif choice == 2:
        view_notes()
    
    elif choice == 3:
        print("Thanks for using the notes app!")
        break

    else:
        print("Invalid choice!")



    