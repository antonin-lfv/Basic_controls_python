'''' Tool box Python '''

## Series of examples for data manipulation

# Import :
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import string
from datetime import datetime
from datetime import date

# sorting a string :
string = 'Pierre, Julien, Anne, Marie, Lucien'

string_list = string.split(', ')
sorted_string = ', '.join(string_list.sort())
print(sorted_string)

# Create a list of numbers :
list = list(range(10,29,2)) " de 10 à 28 avec un pas de 2

# Choose a random number from a list :
rd.choice(list)

# Counting the number of occurrences of a letter in a sentence :
letter_to_find = "o"
sentence = "hello everybody"

print(sentence.lower().count(letter_to_find)) " lower for lowercase

# Retrieve 1 item on k in a list :
listk = list(range(100))
list2[20:80:10]

# concatenate 2 lists :
list + listk

# Having  common elements of two lists :
list1 = set(list)
list2 = set(listk)
intersect = list(list1.intersection(list2))

# Sorting a list of Tuples :
list3 = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
list3.sort(key=lambda x: x[1]) "we sort by mark
print(list3)

# Retrieving a value from a dictionary :
employes = {"01": {"identity": {"name": "Pierre", "surname": "Dupont"}}}
employes.get("01", {}).get("identity", {}).get("name", "Unknow_value") "the 2nd value of the get is the value displayed in case of error

# Adding values from a dictionary :
employes2 = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
sum(employes2.values())

# concatenate strings :
name = "Pierre"
surname = "Dupont"
print(f"hello I'm {name} {surname} ")


# Invert the letters of a word :
word = "hello"
word[::-1]

# Mixing the letters of a word :
word = list("hello")
rd.shuffle(word)
"".join(word)

# Adding the digits of a number :
number = 209812
sum([int(i) for i in str(number)])

# Replacing an item in a list :
list4 = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
name_to_find = "Julie"
new_name = "Julien"
[x.replace(name_to_find, new_name) for x in list4]

# Removing duplicates from a list :
numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
numbers_without_duplicates = []
for i in numbers:
    if i not in numbers_without_duplicates:
        numbers_without_duplicates.append(i)

# Adding items to a dictionary :
employes = {}
list = ["Pierre","Marie","Adrien"]
i = 1
for element in list:
    employes["id-{:02d}".format(i)] = element
    i += 1
print(employes)

# Create a dictionary with the letters of the alphabet :
alphabet = string.ascii_lowercase
indices = range(1, len(alphabet) + 1)
list_zip = zip(indices, alphabet)
result = dict(list_zip)
print(result)

# Framing a text :
text = "Vive les Maths"
length = len(text)
symbol1 = "-"
symbol2 = "|"
print(symbol1*length)
for letter in text:
    print("{0}{1:^{2}}{0}".format(symbol2, letter, length - 2))
print(symbol1*length)

# Adding a thousand separator to a number :
def adding_separator(number):
    number = str(number)[::-1]
    result = ""
    for i, digit in enumerate(number, 1):
        digit_form = digit + "," if i % 3 == 0 and i != len(number) else digit
        result += digit_form
    return result[::-1]
number = 52039480394023
print(adding_separator(number))

# Calculating the year of birth from a given age :
age = 102
month_of_birth = 9
current_year = datetime.today().year
current_month = datetime.today().month
result = current_year - age - (1 if month_of_birth > current_month else 0)
print(result)

# Sort a list of employees :
employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]

alphabet = string.ascii_lowercase
employes_a_m = [e for e in employes if e[0].lower() in alphabet[:13]]
employes_n_z = [e for e in employes if e[0].lower() in alphabet[13:]]

print("Employes from A to M:", ", ".join(sorted(employes_a_m)))
print("Employes from N to Z:", ", ".join(sorted(employes_n_z)))

# Create a random byte :
"".join(list([str(rd.choice(range(2))) for _ in range(8)]))

# Calculate number of days between 2 dates :
f_date = date(2014, 7, 2)
l_date = date(2018, 7, 11)
delta = l_date - f_date

print(delta.days)

# password generator :
def password():
    length = int(input("length :"))
    symbols = string.ascii_letters + string.digits + string.punctuation
    pw = ''.join(rd.choice(symbols) for _ in range(length))
    print(pw)


# Compter le nombre d'occurrence d'un mot dans un texte :
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

mot = "elit"

lorem = lorem.replace(",", "").replace(".", "")
lorem = lorem.lower()

lorem_split = lorem.split()
print(lorem_split.count(mot))

# Inverser l'ordre des mots dans une phrase :
phrase = "Bonjour tout le monde"
phrase_split = phrase.split()
resultat = []

for mot in reversed(phrase_split):
    resultat.append(mot)

resultat_formate = " ".join(resultat).capitalize()
print(resultat_formate)

# Compter le nombre de phrases dans un texte :
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(lorem.count("."))

# Compter le nombre d'occurrence de chaque lettre de l'alphabet :
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

alphabet = string.ascii_lowercase
resultat = dict(zip(alphabet, [0] * len(alphabet)))

for lettre in lorem.lower():
    if resultat.get(lettre) is not None:
        resultat[lettre] += 1
print(dict(resultat))

# Créer une classe pour gérer des voitures :
class Voiture(object):
    def __init__(self, marque, prix, couleur):
    self.marque = marque
    self.prix = prix
    self.couleur = couleur

super_voiture = Voiture("Lamborghini", 150000, "rouge")
print(super_voiture.marque)
print(super_voiture.prix)
print(super_voiture.couleur)
