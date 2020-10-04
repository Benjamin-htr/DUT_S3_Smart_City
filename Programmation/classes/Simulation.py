from classes.Carte import Carte

class Simulation:
    def __init__(self, nbLieuMission, nbStationRecharge):
        self.nbLieuMission = nbLieuMission
        self.nbStationRecharge = nbStationRecharge
    
    def generationCarte(self):
        carte = Carte()
        carte.creationCartes(self.nbLieuMission, self.nbStationRecharge)
        self.afficher(carte)

    def afficher(self, carte):
        print(carte)

