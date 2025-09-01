student = { 'name': "Jose", 'school': "Computing", 'grade': (66,77,88) }
def average_grade(data):
    grades = data['grade']
    return sum(grades)/len(grades)
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grade'])
        count += len(student['grade'])
    return total/count
student_list = [
    { 'name': "Jose", 'school': "Computing", 'grade': (66,77,88) },
    { 'name': "Anne", 'school': "Biology", 'grade': (55,77,88,77) },
    { 'name': "Rolf", 'school': "Computing", 'grade': (66,77,88) }
]
print(average_grade_all_students(student_list))


def add(x,y):
    return x+y
nums = [3,5]
print(add(*nums))
print(add(x=3, y=5))
dic = {"x": 15, "y": 25}
print(add(dic["x"], dic["y"]))
print(add(**dic))

def add(*args):
    for arg in args:
        arg += arg
    return arg
print(add(1,2,3,4))

# def multiply(*args): #tuple input
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total
# print(multiply(1,2,3))


def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"
print(apply(1,2,3,4, operator="*"))