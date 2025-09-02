from operator import itemgetter

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend/ divisor

def calculate(*values, operator): #value tupple, operator : key word
    return operator(*values)

result = calculate(20, 4, operator=divide)
# result = calculate(20, 4, operator=divide) #error occurs because the number of arguments doesn't match
print(result)

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},   
]

'''
def get_freind_name(friend):
    return friend["name"]

#print(search(friends, "Bob Smith", get_freind_name)) #Run time error
print(search(friends, "Rolf Smith", get_freind_name)) #Run time error
'''

'''
#lambda function
print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
'''

#itemgetter function
print(search(friends, "Rolf Smith", itemgetter("name"))) #from operator import itemgetter