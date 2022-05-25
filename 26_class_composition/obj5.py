## composition is counterpart to inheritance
## composition is used much more than inheritance in python
## composition means in this example--> Bookshelf has many books  || whereas inheritance is Book is a Bookshelf

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

print(shelf)
# BookShelf with 2 books.
