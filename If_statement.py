friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends) #check if there is Jen in the list, friends or not. So, there is Jen for the member of friends, the result will be true.
movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recentely: ")
print(user_movie in movies_watched)
if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet")
number = 7
user_input = input("Enter 'y' if you'd like to play: " ).lower()
if user_input == 'y': #or if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number==number:
        print("You guessed correctly")
    elif number-user_number in (1,-1): #only 1 difference, or elif abs(number-user_number) == 1:
        print("You were off by one")
    else:
        print("Sorry, it's wrong")

day_of_week = input("What day of the week is it today?: ").lower() #.lower() only lower case is true
if day_of_week == "Monday" : 
    print("A")
elif day_of_week == "Tuesday":
    print("B")
else:
    print("C")
print("This always runs")

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]
print(friends == abroad) # True, because it means comparing each members, and they have the same member.
print(friends is abroad) # Fase, because both two list are allocated with different memory area.

my_list = [10, 40, 50]
add = 0
for index in my_list:
    add += index 
print(add)
my_tuple = (0,) #for init, comman must be in there