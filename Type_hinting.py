class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_types: str, weight: int):
        self.name = name
        self.book_types = book_types
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_types}, {self.weight} g>"
    
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)
    
book = Book("Harry Potter", " ", 160)
book.book_types = book.hardcover("HarryPoter", 160)

print(book)


from typing import List # , Tuple, Set, etc...

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

class BookSehlf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self)->str:
        return f"BookShelf with {len(self.books)} books"

from typing import List

def list_avg(sequence : list) -> float:
    return sum(sequence)/len(sequence)

list = [1,2,3]
print(list_avg(list))
