from classes.Simulation import Simulation
from tkinter import *

class ControlSimulation:
    def __init__(self):
        self.simulation = None


    def creerSimulation(self, nbEquipes, nbRobotParEquipe, modeDeplacement, CanvasCarte, nbCells, densite, tailleStationRecharge, tailleLieuxMission):
        simulation = Simulation(CanvasCarte)
        simulation.generationCarte(nbEquipes, nbRobotParEquipe, modeDeplacement, nbCells, densite, tailleStationRecharge, tailleLieuxMission)
        self.simulation = simulation


    def creerRobot(self, name) -> None:
        self.simulation.ajouterRobot(name)

    def getRobots(self) -> list:
        return self.simulation.getRobots()

    def getTaches(self) -> list:
        return self.simulation.getTaches()