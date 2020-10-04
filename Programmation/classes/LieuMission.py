from classes.Lieu import Lieu

class LieuMission(Lieu):
    def __init__(self, stock = []):
        super().__init__('R')
        self.stock = stock

    def getSigne(self):
        return super().getSigne()