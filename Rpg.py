from Guerrier import Guerrier
from Monstre import Monstre

print("BIENVENUE DANS MON RPG! ")
print("--------------------")
print("Les règles sont simples : il y a 2 personnages qui s'affrontent. Un monstre et un guerrier.")
print("Le premier à 0 de pv a perdu la guerre. ")
print("--------------------")
print("Que la partie commence !")
print("--------------------")
nom = input("Cher guerrier, Quel est ton nom ?")
pv = 100
niveau = 25
guerrier1 = Guerrier(nom, pv, niveau)
print(f"Bien le bonjour valeureux combattant, voici tes caractéristiques:")
print("--------------------")
print(f"nom : {guerrier1.nom}")
print(f"point de vie : {pv}")
print(f"niveau : {niveau}")
print("--------------------")
monstre1 = Monstre("Gargamel", 100, 25)
print(f"Voici celles de ton adversaire:")
print("--------------------")
print(f"nom : {monstre1.nom}")
print(f"point de vie : {monstre1.pv}")
print(f"niveau : {monstre1.niveau}")
print("--------------------")
while monstre1.pv and guerrier1.pv >= 0:
    monstre1.attaquer(guerrier1)
    print("La créature vient de t'attaquer. Que souhaites-tu faire?")
    print("--------------------")
    print("1. Attaquer. (il perd 20 de pv.)")
    print("2. Défendre. (Tu perds 10 de pv et tu attaques en retour et la créature perd également 10 de pv.)")
    choix = input("Quel est ton choix ? ")
    if choix == "Attaquer":
        monstre1.pv -= 20
    if choix == "Défendre":
        guerrier1.pv -= 10
        monstre1.pv -= 10

if monstre1.pv <= 0:
    print("--------------------")
    print("Félicitation Bersker ! Tu as vaincu la bête féroce.")

else:
    print("--------------------")
    print("Le monstre t'a vaincu. Tu es mort.")
