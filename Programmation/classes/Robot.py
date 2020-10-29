import random
from classes.Carte import Carte
from classes.Cellule import Cellule

class Robot:

    def __init__(self, nom, cellule, carte):
        self.nom = nom
        self.cellule = cellule
        self.carte = carte

    def deplacementRandom(self) :
        #Choisir une direction
        direction = self.choisirDirection()
        #On verifie qu'il a pas de mur
        while (self.verificationMur(direction)):
            direction = self.choisirDirection()
        #On va sur cette case
        if direction == 'N':
            self.cellule = self.carte.cellule(self.cellule.x-1, self.cellule.y)
        elif direction == 'S':
            self.cellule = self.carte.cellule(self.cellule.x+1, self.cellule.y)
        elif direction == 'O':
            self.cellule = self.carte.cellule(self.cellule.x, self.cellule.y-1)
        elif direction == 'E':
            self.cellule = self.carte.cellule(self.cellule.x, self.cellule.y+1)
        return direction


    def deplacement(self, positionArr : tuple) -> list:
        cheminPosition = self.carte.resolution(self.cellule.getPosition() , positionArr)

        cheminDirection = []
        for indexCase in range(1 ,len(cheminPosition)):
            if cheminPosition[indexCase][0] == cheminPosition[indexCase-1][0] -1:
                cheminDirection.append('N')

            elif cheminPosition[indexCase][0] == cheminPosition[indexCase-1][0] +1:
                cheminDirection.append('S')

            elif cheminPosition[indexCase][1] == cheminPosition[indexCase-1][1] -1:
                cheminDirection.append('O')

            elif cheminPosition[indexCase][1] == cheminPosition[indexCase-1][1] +1:
                cheminDirection.append('E')

        return cheminDirection

                


    def choisirDirection(self):
        directions = ['N', 'S', 'E', 'O']
        return random.choice(directions)

    def verificationMur(self, direction) -> bool:
        return self.carte.murPresentCell(direction, self.cellule)