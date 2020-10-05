from classes.Carte import Carte

class Simulation:
    def __init__(self, nbLieuMission, nbStationRecharge, CanvasCarte):
        self.nbLieuMission = nbLieuMission
        self.nbStationRecharge = nbStationRecharge
        self.CanvasCarte = CanvasCarte
    
    def generationCarte(self):
        carte = Carte()
        carte.creationCartes(self.nbLieuMission, self.nbStationRecharge)
        carte.dessinerCarte(self.CanvasCarte)
        self.afficher(carte)

    def afficher(self, carte):
        print(carte)

