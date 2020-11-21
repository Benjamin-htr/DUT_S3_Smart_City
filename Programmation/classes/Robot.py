import random
from classes.Carte import Carte
from classes.Cellule import Cellule
from classes.Chemin import Chemin
from classes.Tache import Tache

class Robot:

    def __init__(self, nom, cellule, carte):
        self.nom = nom
        self.cellule = cellule
        self.carte = carte
        self.chemin = None
        self.destination = None
        self.tache = None
        self.coffre = None
        self.poidsMax = 100

    def deplacementRandom(self) :
        #Choisir une direction
        direction = self.choisirDirection()
        #On verifie qu'il a pas de mur
        while (self.verificationMur(direction)):
            direction = self.choisirDirection()
        #On va sur cette case
        if direction == 'N':
            self.cellule = self.carte.cellule(self.cellule.x-1, self.cellule.y)
        elif direction == 'S':
            self.cellule = self.carte.cellule(self.cellule.x+1, self.cellule.y)
        elif direction == 'O':
            self.cellule = self.carte.cellule(self.cellule.x, self.cellule.y-1)
        elif direction == 'E':
            self.cellule = self.carte.cellule(self.cellule.x, self.cellule.y+1)
        return direction


    def setChemin(self, positionArr) -> None:
        #print('setchemin')
        resolution = self.carte.resolution(self.cellule.getPosition() , positionArr)
        #print("Resolution" ,resolution)
        self.destination = resolution[len (resolution) - 1]
        self.chemin = Chemin(resolution)


    def deplacement(self) -> str:
        if not(self.chemin.vide()): 
            #print('rentré')
            direction = self.chemin.prochainePosition()
            
            if direction == 'N':
                self.cellule = self.carte.cellule(self.cellule.x-1, self.cellule.y)
            elif direction == 'S':
                self.cellule = self.carte.cellule(self.cellule.x+1, self.cellule.y)
            elif direction == 'O':
                self.cellule = self.carte.cellule(self.cellule.x, self.cellule.y-1)
            elif direction == 'E':
                self.cellule = self.carte.cellule(self.cellule.x, self.cellule.y+1)

            return direction

    def choisirDirection(self):
        directions = ['N', 'S', 'E', 'O']
        return random.choice(directions)

    def verificationMur(self, direction) -> bool:
        return self.carte.murPresentCell(direction, self.cellule)

    def choixTacheDijkstra(self, listTache : list) -> Tache:
        distanceTache = []
        for tache in listTache:
            distanceTache.append(len(self.carte.resolution(self.cellule.getPosition() , tache.getCelluleTache().getPosition())))
        distanceMin = min(distanceTache)
        tacheChoisi = listTache[ distanceTache.index( distanceMin ) ]
        self.tache = tacheChoisi

        return tacheChoisi

    def choixTacheVolOiseau(self, listTache : list) -> Tache:
        distanceTache = []
        for tache in listTache:
            x1 = self.cellule.x
            y1 = self.cellule.y
            x2 = tache.getCelluleTache().x
            y2 = tache.getCelluleTache().y
            distanceTache.append( abs((((x2-x1)**2) + ((y2 - y1)**2)) ** 0.5) )
        distanceMin = min(distanceTache)
        tacheChoisi = listTache[ distanceTache.index( distanceMin ) ]
        self.tache = tacheChoisi

        return tacheChoisi

    def getDestination(self):
        return self.destination

    def ajouterMarchandise(self, stock : list) -> None:
        self.coffre.append(stock)