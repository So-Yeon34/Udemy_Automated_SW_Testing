users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]
# for user in users:
#     if user[1] == "Bob":
#         print(users)
# print(username_mapping)
# print(username_mapping["Bob"])
username_mapping = {user[1] : user for user in users}
print(username_mapping)
username_input = input("Enter your name: ")
password_input = input("Enter your password: ")
_, username, password = username_mapping[username_input]
if password == password_input:
    print("Correct!")
else:
    print("Wrong") 

def double(x):
    return x*2
sequence = [1,3,5]
doubled = [double(x) for x in sequence]
doubled_2 = list(map(double, sequence))
print(doubled)
print(doubled_2)
doubled_3 = [(lambda x: x*2)(x) for x in sequence]
doubled_4 = list(map(lambda x: x*2, sequence))
print(doubled_3)
print(doubled_4)

# result = lambda x,y : x+y
# print(result(3,5))
print((lambda x,y:x+y)(5,8))