from classes.Cellule import Cellule
from classes.Lieu import Lieu
from classes.Carte import Carte
import random

class Tache:
    def __init__(self, carte : Carte, recompense = random.randint(100,200)):
        self.carte = carte
        self.temps = 60 #A gerer plus tard
        self.recompense = recompense
        self.lieuDepart = self.carte.ajouterLieuMission([ ("Patate1", 20), ("Patate2", 25)])
        self.lieuArrivee = self.carte.ajouterLieuMission()

        self.form=None

    def getDepart(self) -> Lieu:
        return self.lieuDepart

    def getArrivee(self) -> Lieu:
        return self.lieuArrivee

    def getTemps(self) -> int:
        return self.temps


    def dessinerLieu(self, lieu, tailleX, tailleLieuMission, couleur) :
        if lieu == 0 :
            x = self.lieuDepart.cellule.getPosition()[0]
            y = self.lieuDepart.cellule.getPosition()[1]
        elif lieu == 1 :
            x = self.lieuArrivee.cellule.getPosition()[0]
            y = self.lieuArrivee.cellule.getPosition()[1]

        tailleY=tailleX

        diam=tailleLieuMission
        diamDeb=((100-diam)/2)/100
        diamFin=(((100-diam)/2)+diam)/100

        x0=self.carte.carte.canvasx(y*tailleY+(tailleY*diamDeb))
        y0=self.carte.carte.canvasy(x*tailleX+(tailleX*diamDeb))
        x1=self.carte.carte.canvasx(y*tailleY+(tailleY*diamFin))
        y1=self.carte.carte.canvasy(x*tailleX+(tailleX*diamFin))

        #print("coord du lieu :", x, y, "coord de la forme :", x0, y0, x1, y1)
        
      
        self.form = self.carte.carte.create_rectangle(x0, y0, x1, y1, fill=couleur, tags='form')

    def supprimerForme(self) -> None :
        self.carte.carte.delete(self.form)