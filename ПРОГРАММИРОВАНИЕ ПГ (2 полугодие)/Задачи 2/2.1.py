class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def title(self):
        return self.title

    def author(self):
        return self.author

book = Book("1967", "Mark Anderson")
print(book.title())
print(book.author())
