name = input("What's your name? ")
print("How old are you?", end=' ') # the end=' 'at the end of the line tells print to not end the line with a newline character and go to the next line.
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"Hey {name}, so, you're {age} old, {height} tall and {weight} heavy.")
