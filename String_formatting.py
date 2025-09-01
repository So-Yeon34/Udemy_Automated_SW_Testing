longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Tom", "Monday")
print(formatted)

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

name2 = "Bob"
# greeting2 = (f"Hello, {name2}")
print((f"Hello, {name2}"))
name3 = "Sam"
print((f"Hello, {name3}"))