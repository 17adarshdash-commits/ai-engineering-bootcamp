def add_notes():
    notes_to_add = input("Enter notes to be added: ")
    with open("notes.txt","a") as file:
        file.write(f"{notes_to_add}\n")
        print("Notes added.\n")

def view_notes():
    with open("notes.txt","r") as file:
        content = file.read()
        print(f"{content}\n")

def delete_notes():
    with open("notes.txt","w") as file:
        pass

    print("Notes Deleted.")

while True:

    choice = int(input("1. Add Note\n2. View Notes\n3. Delete Notes\n4. Exit \n\nEnter choice: "))
    if choice == 1:
        add_notes()
        continue

    elif choice == 2:
        view_notes()
    
    elif choice == 3:
        delete_notes()
        pass

    elif choice == 4:
        print("Thanks for using the Notes App.")
        break

    else:
        print("Invalid choice!")



    