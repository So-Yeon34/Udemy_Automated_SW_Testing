name = input("Enter you name: ")
print(name)
size_input = input("How big is your house (in squre feet): ")
squre_feet = int(size_input)
squre_meters = squre_feet/10.8
print("squre feet: " ,squre_feet, ", squre_meters: ", squre_meters)
print(f"{squre_feet} squre feet is {squre_meters: .2f} squre meters")