# Exercise 5: More Variables and Printing

name = 'Claudia P.'
age = 28 # a little lie ;)
height = 164 # cm
height_inches = round(height * 0.3937008)
weight = 51 # kg
weight_pounds = round(weight * 2.204623)
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"She's {height} cm or {height_inches} inches tall.")
print(f"She's {weight} kg or {weight_pounds} pounds heavy.")
print("Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
