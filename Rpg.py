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
    print(f"Voici les caractéristiques de ton adversaire le Berserker:")
    print(f"nom : {guerrier1.nom}")
    print(f"point de vie : {guerrier1.pv}")
    print(f"niveau : {guerrier1.niveau}")
    monstre1.attaquer(guerrier1)
    guerrier1.pv -=  20
    print(f"point de vie du Berserker: {guerrier1.pv}")

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
    print(f"Voici les caractéristiques de ton adversaire la bête sauvage:")
    print(f"nom : {monstre1.nom}")
    print(f"point de vie : {monstre1.pv}")
    print(f"niveau : {monstre1.niveau}")
    print("--------------------")
    print("La créature vient de t'attaquer. Que souhaites-tu faire?")
    print("--------------------")
    print("1. Attaquer. (il perd 20 de pv.)")
    print("2. Défendre. (Tu perds 10 de pv et tu attaques en retour et la créature perd également 10 de pv.)")
    print("3. Te soigner. (Tu perds 5 de pv et tu attaques en retour et la créature perd 15 de pv. )")
    print("--------------------")
    print("ATTENTION ! Toi et le créature féroce ne pouvez attaquer que 2 fois de suite.")
    reponse = input("Quel est ton choix?")
    if reponse == "Attaquer":
        guerrier1.attaquer(monstre1)
        monstre1.pv -= 20
    elif reponse == "Défendre":
        guerrier1.pv -= 10
        monstre1.pv -= 10
    elif reponse == "Me soigner":
        guerrier1.pv -= 5
        monstre1.pv -= 15

