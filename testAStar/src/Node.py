from src.Carte import Carte
from src.Cellule import Cellule

class Node:
    def __init__(self, parent=None, cellule=None):
        self.parent = parent
        self.cellule = cellule
        self.position = (cellule.getPosition()[0],cellule.getPosition()[1])

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def setParamG(self, g):
        self.g = g

    def setParamH(self, h):
        self.h = h

    def setParamF(self):
        self.f = self.g + self.h