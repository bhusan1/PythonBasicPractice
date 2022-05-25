## common way of using @classmethod
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)   ## we can use cls instead of Book also

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)

book = Book.hardcover("Harry Potter", 150)
light = Book.paperback("Python 101", 100)

print(book.name)        #Harry Potter
print(book)             # <Book Harry Potter, hardcover, weighing 150g>
print(light)            # <Book Python 101, paperback, weighing 100g>

