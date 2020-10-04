from classes.Lieu import Lieu

class StationRecharge(Lieu):
    def __init__(self):
        super().__init__('R')

    def getSigne(self):
        return super().getSigne()