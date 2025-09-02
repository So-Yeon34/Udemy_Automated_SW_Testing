def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.") #debugging
    return dividend/divisor

students = [
    {"name": "Bob", "grades": [75,90]},
#    {"name": "Rolf", "grades": []},
    {"name": "Rolf", "grades": [90, 90]},
    {"name": "Jen", "grades": [100,90]}
]

try:
    for student in students:
        name = student["name"]
        grade = student["grades"]
        average = divide(sum(grade), len(grade))
        print(f"{name} averaged {average}")

except ZeroDivisionError:
    print(f"Error: {name} has no grades!")
else:
    print("--All student averages calculated --")
finally:
    print("--End of student average calculation")



# def divide(dividend, divisor):
#     # if divisor == 0:
#     #     print("Divisor cannot be 0.")
#     #     return
    
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0.") #debugging
#         '''
#         Example error types
#         raise TypeError
#         raise ValueError
#         raise RuntimeError
#         '''
#     return dividend/divisor

# #divide(15,0)

# # #grades = [78, 99, 85, 100]
# # grades = []
# # print("Welcome to the average grade program")
# # try: #When exceptions occur, skip this and go to except statement.
# #     average = divide(sum(grades), len(grades))
# #     print(f"The average grade is {average}")
# # #except ZeroDivisionError:
# # except ZeroDivisionError as e: #if error occurs, do execute this statement.
# #     print("There are no grades yet in your list.")
# #     print(e)

# grades = []
# print("Welcome to the average grade program")
# try:
#     average = divide(sum(grades), len(grades))
# except ZeroDivisionError as e: #if error occurs, do execute this statement.
#     print("There are no grades yet in your list.")
#     print(e)
# else:
#     print(f"The average grade is {average}") #if no error happen, then execute this statement.
# finally:
#     print("Thank you")