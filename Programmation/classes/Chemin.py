from classes.Cellule import Cellule

class Chemin:

    def __init__(self, chemin : list):
        self.chemin = chemin
        self.positionToDirection()

    def positionToDirection(self):
        cheminDirection = []
        for indexCase in range(1 ,len(self.chemin)):
            if self.chemin[indexCase][0] == self.chemin[indexCase-1][0] -1:
                cheminDirection.append('N')

            elif self.chemin[indexCase][0] == self.chemin[indexCase-1][0] +1:
                cheminDirection.append('S')

            elif self.chemin[indexCase][1] == self.chemin[indexCase-1][1] -1:
                cheminDirection.append('O')

            elif self.chemin[indexCase][1] == self.chemin[indexCase-1][1] +1:
                cheminDirection.append('E')
        self.chemin = cheminDirection

    def prochainePosition(self) -> Cellule:
        pos = self.chemin[0]
        del self.chemin[0]
        return pos
    
    def vide(self) -> bool:
        return len(self.chemin) == 0