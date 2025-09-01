class ClassTest:
    def instnce_method(self):
        print(f"Called instance_method of {self}")
              
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method.")
# test = ClassTest()
# test1 = ClassTest()
# test.instnce_method()
# ClassTest.instnce_method(test1)
ClassTest.class_method() #ClassTest.class_method(ClassTest)
ClassTest.static_method()

class Store:
    def __init__(self, name):
        self.name = name
        self.item = []

    def add_item(self, name, price):
        self.item.append({"name": name, "price": price})

    def stock_price(self):
        total = 0
        for item in self.item:
            total += item["price"]
        return total
    
    @classmethod
    def franchise(cls, store):
        return cls(store.name + "-franchise")
    

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f"{store.name.upper()}, total stock price: {store.stock_price()}"
    
store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyborad", 160)
Store.franchise(store)
Store.franchise(store2)

Store.store_details(store)
print(Store.store_details(store2))
print(store2.__dict__)

class Book:
    TYPES = ("Hardcover", "Paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
#      return Book(name, Book.TYPES[0], page_weight + 100)
      return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
#        return Book(name, Book.TYPES[1], page_weight)
        return cls(name, cls.TYPES[1], page_weight)
    
# book = Book("Harry Potter", "Hardcover", 1500)
#print(book.__dict__)
book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
print(book)
print(light)