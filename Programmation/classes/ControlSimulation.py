from classes.Simulation import Simulation

class ControlSimulation:
    def __init__(self):
        None

    def creerSimulation(self, nbLieuMission, nbStationRecharge):
        simulation = Simulation(nbLieuMission, nbStationRecharge)
        simulation.generationCarte()
        return simulation