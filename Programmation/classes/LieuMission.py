from classes.Lieu import Lieu
from classes.Marchandise import Marchandise

class LieuMission(Lieu):
    def __init__(self, cellule ,stock = []):
        super().__init__(cellule)
        self.stock = []
        for element in stock:
            self.stock.append(Marchandise(element[0], element[1]))

    def getMarchandise(self) -> list:
        return self.stock