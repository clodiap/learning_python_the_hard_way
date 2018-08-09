# Exercise 6: Strings and Text

# assignement variable (integer)
types_of_people = 10
# assignement variable (string) incluant une autre variable
x = f"There are {types_of_people} types of people."

# assignement variable (string)
binary = "binary"
# assignement variable (string)
do_not = "don't"
# assignement variable (string) incluant 2 autres variables
y = f"Those who know {binary} and those who {do_not}." #a string inside a string

# affiche à l'écran le contenu de la variable x
print(x)
# affiche à l'écran le contenu de la variable y
print(y)

# affiche à l'écran un texte et le contenu de la variable x
print(f"I said: {x}") #a string inside a string
# affiche à l'écran un texte et le contenu de la variable y
print(f"I also said: {y}") #a string inside a string

# assignement variable (booléen)
hilarious = False
# assignement variable (string)
joke_evaluation = "Isn't that joke so funny?! {}"

# affiche à l'écran un texte et le contenu des variables joke_evaluation et hilarious
print(joke_evaluation.format(hilarious))

# assignement variable (string)
w = "This is the left side of …"
# assignement variable (string)
e = "a string with a right side."

# affiche à l'écran les 2 variables w et e (concaténation)
print(w + e)
