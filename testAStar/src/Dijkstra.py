from src.Carte import Carte
from src.Cellule import Cellule

class Dijkstra:

    def __init__(self, carte : Carte):
        self.carte = carte

    def resolution(self, source : Cellule, target : Cellule):
        return self.carte.dijkstra(source, target)