from classes.ControlSimulation import ControlSimulation

class GestionSimulation:
    def __init__(self, nbLieuMission, nbStationRecharge):
        self.nbLieuMission = nbLieuMission
        self.nbStationRecharge = nbStationRecharge
    
    def lancerSimulation(self):
        controlSimulation = ControlSimulation()
        sim = controlSimulation.creerSimulation(self.nbLieuMission, self.nbStationRecharge)
    
    def arreterSimulation(self):
        return None