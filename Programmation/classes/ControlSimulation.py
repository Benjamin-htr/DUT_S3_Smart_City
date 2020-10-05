from classes.Simulation import Simulation
from tkinter import *

class ControlSimulation:
    def __init__(self):
        None

    def creerSimulation(self, nbLieuMission, nbStationRecharge, CanvasCarte):
        simulation = Simulation(nbLieuMission, nbStationRecharge, CanvasCarte)
        simulation.generationCarte()
        return simulation