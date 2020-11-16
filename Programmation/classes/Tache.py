from classes.Cellule import Cellule
from classes.Lieu import Lieu
from classes.Carte import Carte
import random

class Tache:
    def __init__(self, carte : Carte):
        self.carte = carte
        self.temps = 60 #A gerer plus tard
        self.recompense = random.randint(100,200)
        self.celluleTache = self.carte.getCelluleRandom()
        self.lieuDepart = self.carte.ajouterLieuMission()
        self.lieuArrivee = self.carte.ajouterLieuMission()

    def getDepart(self) -> Lieu:
        return self.lieuDepart

    def getArrivee(self) -> Lieu:
        return self.lieuArrivee

    def getTemps(self) -> int:
        return self.temps

    def getCelluleTache(self) -> Cellule:
        return self.celluleTache