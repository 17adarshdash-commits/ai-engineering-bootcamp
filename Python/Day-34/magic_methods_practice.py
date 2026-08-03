class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.author, self.pages) == (other.title, other.author, other.pages)

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages


if __name__ == "__main__":
    book1 = Book("Dune", "Frank Herbert", 412)
    book2 = Book("Dune", "Frank Herbert", 412)
    book3 = Book("The Hobbit", "J.R.R. Tolkien", 310)

    print(book1)          # __str__
    print(repr(book1))    # __repr__
    print(len(book1))     # __len__
    print(book1 == book2) # __eq__
    print(book1 < book3)  # __lt__
