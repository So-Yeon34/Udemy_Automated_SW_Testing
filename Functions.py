def divide(dividen, divisor):
    if divisor!=0:
        return dividen/divisor
    else:
        return "Wront Input"
result = divide(15,3)
print(result)
result = divide(15,0)*5
print(result)

def add(x,y):
    return x+y
result = add(3,5)     
print(result)

default_y = 3
def add(x, y=default_y):
    sum = x+y
    print(sum)    
add(2) #result = 5
default_y = 4
add(2) #result = 5, because y follows previous default_y value defined before creating the function

def add(x,y=8): #default value for y
    print(x+y)
add(5) #without y value, this code will be executed, because y has initial value
add(x=5,y=5)

def divide(dividened, divisor):
    if divisor != 0:
        print(dividened/divisor)
    else:
        print("Wrong input")
divide(15,3)
divide(15,0)
divide(dividened=0, divisor=15)

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")
say_hello(surname = "Bob", name = "Smith")
say_hello("Soyeon", "Kim")

def add(x,y):
    result = x+y
    print(x+y)
add(5,3)

def add_friend():
    friends.append("Rolf")
friends = [] #this is fine because before executing the function, friends list is defined.
add_friend()
add_friend()
add_friend()
print(friends)

friends = ["Rolf", "Bob"]
def add_freind():
    friend_name = input("Enter your friend name: ")
    #friends = friends + [friend_name]    #This friend list is different one from global list of friends, be careful!
    f = friends + [friend_name]
    print(f)
add_freind()

print("Welcome to the age in seconds program!")
def user_age_in_second():
    user_age = int(input("Enter your age: "))
    age_second = user_age * 365 * 34 * 60 * 60
    print(f"Your age in seconds is {age_second}sec.")
user_age_in_second()
print("Good Bye")
# def hello():
#     print("Hello")
#     print("Thanks")
# hello()