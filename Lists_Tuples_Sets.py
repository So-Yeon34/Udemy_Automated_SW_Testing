friend = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local_friend = friend.difference(abroad)
local_friend2 = abroad.difference(friend)
# print(local_friend)
# print(local_friend2) #empty set
union_friend = abroad.union(friend)
# print(union_friend)
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)

list = ["Bob", "Rolf", "Anne"]
tuple = ("Bob", "Rolf", "Anne")
set = {"Bob", "Rolf", "Anne"}
list[0] = "Smith"
# print(list)
# tuple[0] = "Smith" error becuase tuple cannot be modified
# set[0] = "Smith" error becuase set doesn't allow the notation
list.append("Bob")
print(list)
#tuple.append("Smith") error because tuple cannot be modified
list.remove("Bob")
print(list)
#set.append("Smith") error because set isn't allowed append, so I have to use add instead of append
set.add("Smith")
set.add("Smith")
print(set) #It is not allowed to duplicate.