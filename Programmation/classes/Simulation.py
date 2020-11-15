from classes.Carte import Carte
from classes.Robot import Robot
from classes.Cellule import Cellule
from classes.Tache import Tache
from tkinter import *
import random

class Simulation:
    def __init__(self, CanvasCarte):
        self.nbLieuMission = None
        self.nbStationRecharge = None
        self.CanvasCarte = CanvasCarte
        self.robots = []
        self.taches = []
        self.carte = None
    
    def generationCarte(self, nbCells, densite, tailleStationRecharge, tailleLieuxMission):
        carte = Carte(self.CanvasCarte, nbCells)
        carte.creationCartes(densite)
        carte.dessinerCarte(tailleStationRecharge, tailleLieuxMission)
        self.carte = carte

        #on ajoute les robots :
        for i in range(int(self.carte.nx / 2)):
            self.robots.append(Robot('test',self.carte.getCelluleRandom(),self.carte))
            #print("Position initiale robot", self.robots[i].cellule.getPosition())

        #on ajoute les tâches :
        for i in range(int((self.carte.nx / 2) * 1.5)):
            self.ajouterTache()

        
        for robot in self.robots:
            #robot.setChemin(robot.choixTacheDijkstra(self.getTaches()).getCelluleTache().getPosition())
            NearbyTache = robot.choixTacheVolOiseau(self.getTaches())

            robot.setChemin(NearbyTache.getCelluleTache().getPosition())
            
            robot.ObjetDestination = NearbyTache
            #print("Destination robot : ", robot.destination)

        self.afficher(carte)


    def afficher(self, carte):
        print(carte)

    def ajouterRobot(self, name) -> None:
        nbCell=self.carte.nx
        self.robots.append(Robot(name, Cellule(random.randint(0,nbCell-1), random.randint(0,nbCell-1)), self.carte))
        
        
    def getRobots(self) -> list:
        return self.robots

    def getTaches(self) -> list:
        return self.taches

    def estPresent(self, cellule):
        estPresent = False
        for i in range(len(self.taches)):
            if (self.taches[i].getCelluleTache().getPosition() == cellule.getPosition()):
                estPresent = True
                break
        return estPresent

    def ajouterTache(self) -> None:
        tache = Tache(self.carte)
        while self.estPresent(tache.getCelluleTache()):
            tache = Tache(self.carte)
        self.taches.append(tache)
