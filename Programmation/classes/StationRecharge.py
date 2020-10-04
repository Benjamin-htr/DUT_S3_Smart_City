from classes.Lieu import Lieu

class StationRecharge(Lieu):
    def __init__(self):
        self.signe = 'R'

    def getSigne(self):
        return self.signe