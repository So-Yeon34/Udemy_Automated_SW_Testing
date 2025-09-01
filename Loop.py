# numbers = [1,3,5]
# # doubled = []
# # for num in numbers:
# #     doubled.append(num*2)
# doubled = [x*2 for x in numbers] #this has the same result as line 2~3
# print(doubled)
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# Starts_s = []
# for x in friends:
#     if x.startswith("S"):
#         Starts_s.append(x)
Starts_s = [x for x in friends if x.startswith("S")]
print(Starts_s)
print("friends: ", id(friends), "Starts_s: ", id(Starts_s)) #id() is memory address like pointer in C, if I define friends = starts_s, then they will be allocated in same address

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = []
for number in numbers:
    if (number%2 == 0):
        evens.append(number)
print(evens)

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)
for grade in grades:
    total += grade
print(total/amount)
friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in range(4):
#for friend in friends:
    print(f"{friend} is my friend.")
number = 7
while True:
    user_input = input("Would you like to play? (Y/n): " )
    if user_input == "n":
        break
    user_number = int(input("Guess our number: "))
    if user_number==number:
        print("You guessed correctly")
    elif number-user_number in (1,-1): #only 1 difference, or elif abs(number-user_number) == 1:
        print("You were off by one")
    else:
        print("Sorry, it's wrong")
