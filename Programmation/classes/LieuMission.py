from classes.Lieu import Lieu

class LieuMission(Lieu):
    def __init__(self):
        self.signe = 'M'

    def getSigne(self):
        return self.signe