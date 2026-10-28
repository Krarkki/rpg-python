#from Guerrier import Guerrier

class Monstre:
    def __init__(self, nom, pv, niveau):
        self.nom = nom
        self.pv = pv # point de vie
        self.niveau = niveau

    def attaquer(self, guerrier):
        print(f"Le Monstre {self.nom} lance une attaque contre le Guerrier {guerrier.nom}.")

    def defendre(self):
        print(f"Le Monstre {self.nom} a choisit de se défendre!")

#monstre = Monstre("Gorgon", 100, 25)