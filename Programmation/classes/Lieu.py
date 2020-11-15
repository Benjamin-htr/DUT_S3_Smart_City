from classes.Cellule import Cellule

class Lieu:

    def __init__(self, cellule):
        self.cellule = cellule
    
    def getCellule(self) -> Cellule:
        return self.cellule