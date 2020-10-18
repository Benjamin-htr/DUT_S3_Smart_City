from classes.Simulation import Simulation
from tkinter import *

class ControlSimulation:
    def __init__(self):
        self.simulation = None


    def creerSimulation(self, nbLieuMission, nbStationRecharge, CanvasCarte):
        simulation = Simulation(nbLieuMission, nbStationRecharge, CanvasCarte)
        simulation.generationCarte()
        self.simulation = simulation


    def creerRobot(self, name) -> None:
        self.simulation.ajouterRobot(name)

    def getRobots(self) -> list:
        return self.simulation.getRobots()
