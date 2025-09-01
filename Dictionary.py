x=[(5,11)] #tuple inside list
x, y = 5, 11
t = 5,11
x,y = t
print(x,y)
student_attendance = {"Rolf": 96, "Bob": 80, "Anne" : 100}
#print(list(student_attendance.items())) #three different tuple
for t in student_attendance.items():
    print(t)
for a,b in student_attendance.items():
    print(f"{a}, {b}")
people = [("Bob", 43, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
# for name, age, profession in people:
#     print(f"Name:  {name}, Age: {age}, Profession: {profession}")
for x in people:
     print(f"Name:  {x[0]}, Age: {x[1]}, Profession: {x[2]}")
person = ("Bob", 43, "Mechanic")
name, _, profession = person #_ means "doesn't matter"
print(name, profession)
head, *tail = [1,2,3,4,5] #It means the first member is included at head, and the rest one are included at tail
print(head)
print(tail)
*head, tail = [1,2,3,4,5] 
print(head)
print(tail)

# friend_age = {"Rolf": 24, "Adam": 30, "Anne": 27}
# print(friend_age["Adam"])
# friend_age["Adam"] = 34
# print(friend_age["Adam"])
# friends = [
#     {"Name" : "Rolf", "Age" : 24},
#     {"Name" : "Adam", "Age" : 30},
#     {"Name" : "Anne", "Age" : 27},
# ]
# print(friends[1])
# print(friends[1]["Name"])
student_attendance = {"Rolf": 96, "Bob": 80, "Anne" : 100}
# # for x in student_attendance:
# #     print(f"{x} : {student_attendance[x]}")
# for x, y in student_attendance.items():
#     print(f"{x} : {y}")
# if "Bob" in student_attendance:
#     print(f"Bob : {student_attendance['Bob']}")
# else:
#     print("Bob is not a student in this class")
# attendance_values = student_attendance.values()
# print(sum(attendance_values)/len(attendance_values))
