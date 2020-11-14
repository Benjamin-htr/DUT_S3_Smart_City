from classes.Carte import Carte
from classes.Robot import Robot
from classes.Cellule import Cellule
from tkinter import *
import random

class Simulation:
    def __init__(self, nbLieuMission, nbStationRecharge, CanvasCarte):
        self.nbLieuMission = nbLieuMission
        self.nbStationRecharge = nbStationRecharge
        self.CanvasCarte = CanvasCarte
        self.robots = []
        self.carte = None
    
    def generationCarte(self, nbCells, densite, tailleStationRecharge, tailleLieuxMission):
        carte = Carte(self.CanvasCarte, nbCells)
        carte.creationCartes(self.nbLieuMission, self.nbStationRecharge, densite, tailleStationRecharge, tailleLieuxMission)
        carte.dessinerCarte()
        self.carte = carte
        self.robots.append(Robot('test',Cellule(5, 5),self.carte))
        self.afficher(carte)

    def afficher(self, carte):
        print(carte)

    def ajouterRobot(self, name) -> None:
        nbCell=self.carte.nx
        self.robots.append(Robot(name, Cellule(random.randint(0,nbCell-1), random.randint(0,nbCell-1)), self.carte))
        
        
    def getRobots(self) -> list:
        return self.robots
