from classes.Carte import Carte
from tkinter import *

class Simulation:
    def __init__(self, nbLieuMission, nbStationRecharge, CanvasCarte):
        self.nbLieuMission = nbLieuMission
        self.nbStationRecharge = nbStationRecharge
        self.CanvasCarte = CanvasCarte
    
    def generationCarte(self):
        carte = Carte(self.CanvasCarte)
        carte.creationCartes(self.nbLieuMission, self.nbStationRecharge)
        carte.dessinerCarte()
        self.afficher(carte)

    def afficher(self, carte):
        print(carte)

