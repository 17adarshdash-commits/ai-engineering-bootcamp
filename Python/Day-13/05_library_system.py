class LibraryItem:
    def __init__(self, title, item_id, available):
        self.title = title
        self.__item_id = item_id
        self.__available = available

    def set_availability(self, status):
        self.__available = status

    def get_item_id(self):
        return self.__item_id
    
    def is_available(self):
        return self.__available
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Item ID: {self.get_item_id()}")
        print(f"Availability: {self.is_available()}")
        

class Book(LibraryItem):
    def __init__(self, title, item_id, available, author):
        super().__init__(title, item_id, available)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")

class Magazine(LibraryItem):
    def __init__(self, title, item_id, available, issue_number):
        super().__init__(title, item_id, available)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")

book = Book("Python Crash Course", 101, "Available", "Eric Matthes")
magazine = Magazine("National Geographic", 25, "Not Available", 202)

book.display_info()

print()

magazine.display_info()