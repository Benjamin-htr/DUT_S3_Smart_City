import random
from classes.Carte import Carte
from classes.Cellule import Cellule
from classes.Chemin import Chemin
from classes.Tache import Tache

class Robot:

    def __init__(self, nom, cellule, carte, simulation):
        self.nom = nom
        self.cellule = cellule
        self.carte = carte
        self.simulation = simulation
        self.chemin = None
        self.destination = None

        #attribut permettant de connaitre l'objet de la destination du robot (lieuMission, stationRecharge ou tache)
        self.ObjetDestination = None

        self.tache = None
        self.coffre = []
        self.poidsMax = 100

        self.passéSurLieuDepart = False


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

        return tacheChoisi

    def getDestination(self):
        return self.destination

    def ajouterMarchandise(self, stock : list) -> None:
        self.coffre.append(stock)

    def deposerMarchandise(self) -> None:
        self.coffre = None

    
    #méthode permettant de savoir si le robot est arrivé sur la tache
    def estSurTache(self) -> bool :
        #si il est bien arrivé sur une tache :
        if (isinstance(self.ObjetDestination, Tache) and self.cellule.getPosition() == self.destination) :
            #si la tache existe encore dans la liste des tâches de simulation :
            if self.ObjetDestination in self.simulation.taches :
                #je la supprime (elle n'est plus disponible)
                self.ObjetDestination.supprimerForme()
                self.simulation.taches.remove(self.ObjetDestination)
                

                #je la définie comme étant la tâche du robot
                self.tache = self.ObjetDestination

                #je définie le lieu de depart de la tache comme etant le nouvel obj de destination du robot
                self.ObjetDestination = self.tache.getDepart()
                self.destination = self.tache.getDepart().getCellule().getPosition()
                self.setChemin(self.destination)


                return True
            
            #si la tache n'existe plus la liste des tâches de simulation (le robot est arrivé trop tard):
            elif (self.tache == None) :
                NearbyTache = self.choixTacheVolOiseau(self.simulation.getTaches())
                self.setChemin(NearbyTache.getCelluleTache().getPosition())
                self.ObjetDestination = NearbyTache

                return False
        else :
            return False


    def estSurLieuDepart(self) :
        arrive = False
        if (self.ObjetDestination == self.tache.getDepart()) and (self.cellule.getPosition() == self.destination) :
            if self.ObjetDestination in self.carte.lieu :
                self.ajouterMarchandise((self.ObjetDestination.getMarchandise()))
                self.tache.supprimerForme()
                self.carte.lieu.remove(self.ObjetDestination)

                #je définie le lieu d'arrivee de la tache comme etant le nouvelle obj de destination du robot
                self.ObjetDestination = self.tache.getArrivee()
                self.destination = self.tache.getArrivee().getCellule().getPosition()
                self.setChemin(self.destination)
                #print("lieu arrivee", self.destination)

                arrive = True

        return arrive 
            
    def estSurLieuArrive(self) :
        arrive = False
        if (self.ObjetDestination == self.tache.getArrivee()) and (self.cellule.getPosition() == self.destination) :
            if self.ObjetDestination in self.carte.lieu :
                self.deposerMarchandise()
                self.tache.supprimerForme()
                self.carte.lieu.remove(self.ObjetDestination)

                arrive = True

        return arrive
        

    def AccomplirTâche(self, cameraMoovable, scale, tailleX, tailleLieuxMission, zoom =None) :
        #s'il est arrivé sur la tâche :
        if self.estSurTache() :
            #si le zoom est activé et que j'ai déjà zoomé alors je réinitialise la caméra :
            if cameraMoovable and scale != 1 :
                 tailleX = zoom.resetZoom2()
            #s'il est arrivé sur la tache je dessine le lieu départ
            self.tache.dessinerLieu(0, tailleX, tailleLieuxMission, 'red')

        #s'il a auparavant recuperer une tache
        if self.tache != None :
            #s'il est arrivé sur le lieu de départ :
            if self.estSurLieuDepart() :
                self.passéSurLieuDepart = True
                #si le zoom est activé et que j'ai déjà zoomé alors je réinitialise la caméra :
                if cameraMoovable and scale != 1 :
                    tailleX = zoom.resetZoom2()
                #s'il est arrivé sur le lieu de départ je dessine le lieu d'arrivee
                self.tache.dessinerLieu(1, tailleX, tailleLieuxMission, 'green')

        #s'il a auparavant atteint le lieu de depart :
        if self.passéSurLieuDepart :
            #s'il a terminé la tâche :
            if self.estSurLieuArrive() :
                #je réinitialise les attributs d'instance :
                self.passéSurLieuDepart = False
                self.tache = None
                print('tache terminée !')
        



        

        
