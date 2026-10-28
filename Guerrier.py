#from Monstre import Monstre

class Guerrier:
    def __init__(self, nom, pv, niveau):
        self.nom = nom
        self.pv = pv # point de vie
        self.niveau = niveau

    def attaquer(self, monstre):
        print(f"Le Guerrier {self.nom} a décidé que la meilleure défense c'est l'attaque. Et il attaque le monstre {monstre.nom}!")

    def defendre(self):
        print(f"Le Guerrier {self.nom} a choisit de se défendre!")



