class Book:
    def __init__(self, title, author):

        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

# Example usage of the classes
book1 = Book("1967", "Mark Anderson")
book2 = Book("Brave New World", "John Beston")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.remove_book(book1)

found_book = library.search_by_title("Brave New World")
if found_book:
    print(found_book.get_author())  # Output: Aldous Huxley
else:
    print("Book not found")
