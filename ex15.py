# Reading files

from sys import argv

# passer les arguments à l'ouverture du script
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# fermer les documents qu'on a ouverts
txt.close()
txt_again.close()
