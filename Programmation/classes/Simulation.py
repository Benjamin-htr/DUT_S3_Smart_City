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
    
    def generationCarte(self):
        carte = Carte(self.CanvasCarte)
        carte.creationCartes(self.nbLieuMission, self.nbStationRecharge)
        carte.dessinerCarte()
        self.carte = carte
        #self.robots.append(Robot('test',Cellule(1, 10),self.carte))
        self.afficher(carte)

    def afficher(self, carte):
        print(carte)

    def ajouterRobot(self, name) -> None:
        self.robots.append(Robot(name, Cellule(random.randint(0,19), random.randint(0,19)), self.carte))
        
    def getRobots(self) -> list:
        return self.robots
