#composition
class BookShelf:
    def __init__(self, *books):
        self.books = books
    def __str__(self):
        return f"BookShelf with {len(self.books)} books"

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"
    
book = Book("Harry Poter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)

class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"BookShelf with {self.quantity} books"
    
shelf = BookShelf(300)

class Book(BookShelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        #return f"{super().__str__()}, Book {self.name}"
        return f"Book {self.name}" #overwrite -> we can use composition

book = Book("Harry Poter", 120)
print(shelf)
print(book)