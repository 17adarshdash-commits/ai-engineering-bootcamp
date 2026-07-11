class Book:
    def __init__(self, title, author, availability = True):
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.availability == True:
            print("Book borrowed successfully.")
            self.availability = False
        else:
            print("Book is not available.")

    def return_book(self):
        if not self.availability:
            print("Book returned.")
            self.availability = True
        else:
            print("Book already present in library.")

my_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
my_book.borrow_book()
my_book.return_book()
