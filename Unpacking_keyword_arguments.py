student = {"name": "Rolf", "grades": (89,90,93,78,90)}
def average(sequence):
    return sum(sequence)/ len(sequence)
print(average(student["grades"]))

def average_V2(**sequence):
    return sum(sequence["grades"])/len(sequence["grades"])
print(average_V2(**student))


def myfunction(**kwargs):
    print(kwargs)

# myfunction(**"Bob") #Error
# myfunction(**None) #Error

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3,4, name="Bob", age=25)

def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg} : {value}")
print_nicely(name ="Bob", age=25)

def named(**kwargs): #dictionary unpacking
    print(kwargs)
named(name="Bob", age = 25)
details = {"name": "Bob", "age": 25}
named(**details)

# def named(name, age): #dictionary unpacking
#     print(name, age)

# details = {"name": "Bob", "age": 25}
# named(**details)