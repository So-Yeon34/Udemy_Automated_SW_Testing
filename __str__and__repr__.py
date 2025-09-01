class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({"name": name, "price" : price})

    def stock_price(self):
        # total = 0
        # for item in self.items:
        #     total += item["price"]
        # return total
        return sum(item["price"] for item in self.items)

store = Store(" ")
store.add_item("Bob", 500)
store.add_item("Susan", 800)
print(store.stock_price())
print(store.items)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def __str__(self):
    #     return "hello" #print(bob) -> "output string "hello""
    # def __str__(self):
    #     return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"
    
bob =Person("Bob", 35)
#print(bob) #address for bob

print(bob)