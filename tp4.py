import random
from dataclasses import dataclass
from math import pi


class Humain:
    def __init__(self):
        self.message = "patate"


class StringFoo:
    def __init__(self, message):
        self.message = message

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(f"`{self.message.upper()}")


class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def calcul_aire(self):
        return self.longueur * self.largeur

    def afficher_info(self):
        print(f"{self.longueur}{self.largeur}{self.calcul_aire()}")


print(Rectangle(2, 3).calcul_aire())


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return self.rayon ** 2 * pi

    def calcul_circonference(self):
        return self.rayon * 2 * pi


print(Cercle(10).calcul_aire())
print(Cercle(10).calcul_circonference())


@dataclass
class Personnage:
    force: int = random.randint(1, 20)
    dexterite: int = random.randint(1, 20)
    constitution: int = random.randint(1, 20)
    intelligence: int = random.randint(1, 20)
    sagesse: int = random.randint(1, 20)
    charisme: int = random.randint(1, 20)


class personnage:
    def __init__(self, nom):
        self.nombre_de_vie = random.randint(1, 10) + random.randint(1, 10)
        self.force_defense = random.randint(1, 6)
        self.force_attack = random.randint(1, 6)
        self.nom = nom
        self.caracteristique = Personnage()

    def dommage(self, dommage):
        self.nombre_de_vie -= dommage - self.force_defense

    def attack(self):
        return random.randint(1, 6) + self.force_attack

    def est_vivant(self):
        return self.nombre_de_vie > 0


moi = personnage("Henri")
print(f"{moi.nom} a {moi.nombre_de_vie} point(s) de vie")
print(f"{moi.nom} a {moi.force_attack} point(s) de vie")
print(f"{moi.nom} est  vivant: {moi.est_vivant()} ")
print(moi.__dict__)
