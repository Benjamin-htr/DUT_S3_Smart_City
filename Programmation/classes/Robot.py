import random
from classes.Carte import Carte
from classes.Cellule import Cellule

class Robot:

    def __init__(self, nom, cellule, carte):
        self.nom = nom
        self.cellule = cellule
        self.carte = carte

    def deplacementRandom(self) -> Cellule:
        #Choisir une direction
        direction = self.choisirDirection()
        #On verifie qu'il a pas de mur
        while (self.verificationMur(direction))
            direction = self.choisirDirection()
        #On va sur cette case
        if direction == 'N':
            cellule = self.carte.cellule(self.x-1, self.y)
        elif direction == 'S':
            cellule = self.carte.cellule(self.x+1, self.y)
        elif direction == 'O':
            cellule = self.carte.cellule(self.x, self.y-1)
        elif direction == 'E':
            cellule = self.carte.cellule(self.x, self.y+1)
        return cellule


    def choisirDirection(self):
        directions = ['N', 'S', 'E', 'O']
        return random.choice(directions)

    def verificationMur(self, direction) -> bool:
        return self.carte.murPresentCell(direction, self.position)