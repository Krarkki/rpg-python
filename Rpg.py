from Guerrier import Guerrier
from Monstre import Monstre

print("BIENVENUE DANS MON RPG! ")
print("--------------------")
print("Les règles sont simples : il y a 2 personnages qui s'affrontent. Un monstre et un guerrier.")
print("Le premier à 0 de pv a perdu la guerre. ")
print("--------------------")
print("Que la partie commence !")
print("--------------------")
print("Tu as 2 choix : Monstre et Guerrier.")
choix = input("Quel est ton choix ?")

if choix == "Monstre":
    guerrier1 = Guerrier("Charles III", 100, 25)
    nom = input("Cher monstre, quel est ton nom ?")
    pv = 100
    niveau = 25
    monstre1 = Monstre(nom, pv, niveau)
    print("--------------------")
    print(f"Salutations, créature des ténèbres! Voici tes caractéristiques:")
    print("--------------------")
    print(f"nom : {nom}")
    print(f"point de vie : {pv}")
    print(f"niveau : {niveau}")
    print("--------------------")
    monstre1.attaquer(guerrier1)

if choix == "Guerrier":
    monstre1 = Monstre("Gorgon", 100, 25)
    nom = input("Cher guerrier, Quel est ton nom ?")
    pv = 100
    niveau = 25
    guerrier1 = Guerrier(nom, pv, niveau)
    print("--------------------")
    print(f"Bien le bonjour valeureux combattant, voici tes caractéristiques:")
    print("--------------------")
    print(f"nom : {nom}")
    print(f"point de vie : {pv}")
    print(f"niveau : {niveau}")
    print("--------------------")
    guerrier1.attaquer(monstre1)

