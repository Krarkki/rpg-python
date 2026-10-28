from Guerrier import Guerrier
from Monstre import Monstre

print("BIENVENUE DANS MON RPG! ")
print("Les règles sont simples : il y a 2 personnages qui s'affrontent. Un monstre et un guerrier.")
print("Le premier à 0 de pv a perdu la guerre. ")
print("Que la partie commence !")
print("Tu as 2 choix : Monstre et Guerrier.")
choix = input("Quel est ton choix ?")

if choix == "Monstre":
    guerrier1 = Guerrier("Charles III", 100, 17)
    nom = input("Cher monstre. Quel est ton nom ?")
    monstre1 = Monstre(nom, 150, 30)
    monstre1.attaquer(guerrier1)

if choix == "Guerrier":
    monstre1 = Monstre("Gorgon", 150, 30)
    nom = input("Cher guerrier. Quel est ton nom ?")
    guerrier1 = Guerrier(nom, 100, 17)
    guerrier1.attaquer(monstre1)

