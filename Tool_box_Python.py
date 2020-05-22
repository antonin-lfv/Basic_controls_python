'''' Tool box Python - Udemy '''

## Série d'exemples pour manipulation de données

# Import :
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import string
from datetime import datetime
from datetime import date

# Ordonner une chaîne de caractère :
chaine = 'Pierre, Julien, Anne, Marie, Lucien'

chaine_liste = chaine.split(', ')
chaine_en_ordre = ', '.join(chaine_liste.sort())
print(chaine_en_ordre)

# Créer une liste de nombres :
liste = list(range(10,29,2)) " de 10 à 28 avec un pas de 2

# Choisir un nombre aléatoire dans une liste :
rd.choice(liste)

# Compter le nombre d'occurrences d'une lettre dans une phrase :
lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"

print(phrase.lower().count(lettre_a_chercher)) " lower pour minuscules

# Récuperer 1 elément sur k dans une liste :
listek = list(range(100))
liste2[20:80:10]

# Concatener 2 listes :
liste + listek

# Avoir les elements communs à deux listes :
liste1 = set(liste)
liste2 = set(listek)
intersect = list(liste1.intersection(liste2))

# Trier une liste de Tuples :
liste3 = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
liste3.sort(key=lambda x: x[1]) "on trie par rapport à la note
print(liste3)

# Récupere une valeur dans un dictionnaire :
employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
employes.get("01", {}).get("identite", {}).get("prenom", "valeur_inconnue") "la 2e valeur du get est la valeur affichée en cas d'erreur

# Additionner les valeurs d'un dictionnaire :
employes2 = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
sum(employes2.values())

# Concatener des chaines de caractères :
prenom = "Pierre"
nom = "Dupont"
print(f"Bonjour je m'appelle {prenom} {nom} ")


# Inverser les lettres d'un mot :
mot = "Coucou"
mot[::-1]

# Mélanger les lettres d'un mot :
mot = list("bonjour")
rd.shuffle(mot)
"".join(mot)

# Additionner les chiffres d'un nombre :
nombre = 209812
sum([int(i) for i in str(nombre)])

# Remplacer un élément dans une liste :
liste4 = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
nom_a_chercher = "Julie"
nouveau_nom = "Julien"
[x.replace(nom_a_chercher, nouveau_nom) for x in liste4]

# Enlever les doublons d'une liste :
nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
nombres_sans_duplicats = []
for i in nombres:
    if i not in nombres_sans_duplicats:
        nombres_sans_duplicats.append(i)

# Ajouter des éléments dans un dictionnaire :
employes = {}
liste = ["Pierre","Marie","Adrien"]
i = 1
for element in liste:
    employes["id-{:02d}".format(i)] = element
    i += 1
print(employes)

# Créer un dictionnaire avec les lettres de l'alphabet :
alphabet = string.ascii_lowercase
indices = range(1, len(alphabet) + 1)
liste_zip = zip(indices, alphabet)
resultat = dict(liste_zip)
print(resultat)

# Encadrer un texte :
texte = "Vive les Maths"
longueur = len(texte)
symbole1 = "-"
symbole2 = "|"
print(symbole1*longueur)
for lettre in texte:
    print("{0}{1:^{2}}{0}".format(symbole2, lettre, longueur - 2))
print(symbole1*longueur)

# Ajouter un séparateur de milliers à un nombre :
def ajout_separateur(nombre):
    nombre = str(nombre)[::-1]
    resultat = ""
    for i, chiffre in enumerate(nombre, 1):
        chiffre_formatte = chiffre + "," if i % 3 == 0 and i != len(nombre) else chiffre
        resultat += chiffre_formatte
    return resultat[::-1]
nombre = 52039480394023
print(ajout_separateur(nombre))

# Calculer l'année de naissance à partir d'un âge donné :
age = 102
mois_de_naissance = 9
annee_actuelle = datetime.today().year
mois_actuel = datetime.today().month
resultat = annee_actuelle - age - (1 if mois_de_naissance > mois_actuel else 0)
print(resultat)

# Trier une liste d'employés :
employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]

alphabet = string.ascii_lowercase
employes_a_m = [e for e in employes if e[0].lower() in alphabet[:13]]
employes_n_z = [e for e in employes if e[0].lower() in alphabet[13:]]

print("Employés de A à M:", ", ".join(sorted(employes_a_m)))
print("Employés de N à Z:", ", ".join(sorted(employes_n_z)))

# Créer un octet aléatoire :
"".join(list([str(rd.choice(range(2))) for _ in range(8)]))

# Calculer nombre de jours entre 2 dates :
f_date = date(2014, 7, 2)
l_date = date(2018, 7, 11)
delta = l_date - f_date

print(delta.days)

#Créer un générateur de mot de passe :
def mot_de_passe():
    taille = int(input("taille :"))
    symboles = string.ascii_letters + string.digits + string.punctuation
    mdp = ''.join(rd.choice(symboles) for _ in range(taille))
    print(mdp)



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