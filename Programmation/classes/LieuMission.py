from classes.Lieu import Lieu

class LieuMission(Lieu):
    def __init__(self, cellule ,stock = []):
        super().__init__(cellule)
        self.stock = stock

    def getMarchandise(self) -> list:
        return self.stock