import random
from classes.Carte import Carte
from classes.Cellule import Cellule
from classes.Chemin import Chemin
from classes.Tache import Tache
from classes.Enchere import Enchere
from classes.StationRecharge import StationRecharge
from tkinter.font import Font

class Robot:

    def __init__(self, nom, color, cellule, carte, simulation, equipe):
        self.nom = nom
        self.color = color
        self.cellule = cellule
        self.carte = carte
        self.simulation = simulation
        self.chemin = None
        self.destination = None
        self.equipe = equipe
        self.perteBatterie = random.randint(1,2)

        #attribut permettant de connaitre l'objet de la destination du robot (lieuMission, stationRecharge ou tache)
        self.ObjetDestination = None

        self.tache = None
        self.coffre = []
        self.poidsMax = 100

        self.passéSurLieuDepart = False

        self.form = None
        self.form2 = None

        self.argent=0

        self.outline='white'

        self.batterie=random.randint(85, 100)

        self.enRecharge = False

        self.gagnant = False

        self.offre = "Aucune"

        self.EnchereEnCours = False

        self.NearbyGagnant = False

        




    def dessinerRobot(self, tailleX, tailleRobot, nouveau = False) :
        font = Font(family="Fixedsys",size=14,weight="bold")
        
        x = self.cellule.x
        y = self.cellule.y
        tailleY=tailleX

        diam=tailleRobot
        diamDeb=((100-diam)/2)/100
        diamFin=(((100-diam)/2)+diam)/100

        x0=(y*tailleY+(tailleY*diamDeb))
        y0=(x*tailleX+(tailleX*diamDeb))
        x1=(y*tailleY+(tailleY*diamFin))
        y1=(x*tailleX+(tailleX*diamFin))

        xText=y*tailleY+(tailleY/2)
        yText=x*tailleX+(tailleX/2)

        if nouveau :
            #on calcule les coordonnées relatives au canvas :
            x0=self.carte.carte.canvasx(y*tailleY+(tailleY*diamDeb))
            y0=self.carte.carte.canvasy(x*tailleX+(tailleX*diamDeb))
            x1=self.carte.carte.canvasx(y*tailleY+(tailleY*diamFin))
            y1=self.carte.carte.canvasy(x*tailleX+(tailleX*diamFin))

        self.form = self.carte.carte.create_oval(x0, y0, x1, y1, fill=self.color, tags='form')
        self.form2 = self.carte.carte.create_text(xText, yText,text=self.equipe.letter, fill='black', font=font)

    def supprimerForme(self) -> None :
         self.carte.carte.delete(self.form)
         self.form=None

    def deplacementRandom(self, tailleX) :
        #Choisir une direction
        direction = self.choisirDirection()
        #On verifie qu'il a pas de mur
        while (self.verificationMur(direction)):
            direction = self.choisirDirection()
        #On va sur cette case
        if direction == 'N':
            #on met à jour ses coordonnées :
            self.cellule = self.carte.cellule(self.cellule.x-1, self.cellule.y)
            #on met à jour son affichage sur la carte :
            self.carte.carte.move(self.form,0,-tailleX)
            self.carte.carte.move(self.form2,0,-tailleX)
        elif direction == 'S':
            self.cellule = self.carte.cellule(self.cellule.x+1, self.cellule.y)
            self.carte.carte.move(self.form,0,tailleX)
            self.carte.carte.move(self.form2,0,-tailleX)
        elif direction == 'O':
            self.cellule = self.carte.cellule(self.cellule.x, self.cellule.y-1)
            self.carte.carte.move(self.form,-tailleX,0)
            self.carte.carte.move(self.form2,0,-tailleX)
        elif direction == 'E':
            self.cellule = self.carte.cellule(self.cellule.x, self.cellule.y+1)
            self.carte.carte.move(self.form,tailleX,0)
            self.carte.carte.move(self.form2,0,-tailleX)

        self.batterie -= 2

        return direction

    def setChemin(self, positionArr) -> None:
        #print('setchemin')
        resolution = self.carte.resolution(self.cellule.getPosition() , positionArr)
        #print("Resolution" ,resolution)
        self.destination = resolution[len (resolution) - 1]
        self.chemin = Chemin(resolution)

    def deplacement(self, tailleX) -> str:
        if not(self.chemin.vide()): 
            #print('rentré')
            direction = self.chemin.prochainePosition()
            
            if direction == 'N':
                #on met à jour ses coordonnées :
                self.cellule = self.carte.cellule(self.cellule.x-1, self.cellule.y)
                #on met à jour son affichage sur la carte :
                self.carte.carte.move(self.form,0,-tailleX)
                self.carte.carte.move(self.form2,0,-tailleX)
            elif direction == 'S':
                self.cellule = self.carte.cellule(self.cellule.x+1, self.cellule.y)
                self.carte.carte.move(self.form,0,tailleX)
                self.carte.carte.move(self.form2,0,tailleX)
            elif direction == 'O':
                self.cellule = self.carte.cellule(self.cellule.x, self.cellule.y-1)
                self.carte.carte.move(self.form,-tailleX,0)
                self.carte.carte.move(self.form2,-tailleX,0)
            elif direction == 'E':
                self.cellule = self.carte.cellule(self.cellule.x, self.cellule.y+1)
                self.carte.carte.move(self.form,tailleX,0)
                self.carte.carte.move(self.form2,tailleX,0)

            self.batterie -= self.perteBatterie


            

            return direction

    def choisirDirection(self):
        directions = ['N', 'S', 'E', 'O']
        return random.choice(directions)

    def verificationMur(self, direction) -> bool:
        return self.carte.murPresentCell(direction, self.cellule)

    def PlusProcheDijkstra(self, liste : list, recherche) -> Tache:
        distance = []
        for obj in liste:
            if recherche == "Tache":
                distance.append(self.carte.getDistance(self.cellule.getPosition(), obj.lieuDepart.getPosition()))
            elif recherche == "Station":
                distance.append(self.carte.getDistance(self.cellule.getPosition(), obj.getCellule().getPosition()))

        distanceMin = min(distance)
        objChoisi = liste[ distance.index( distanceMin ) ]

        if recherche == "Station":
            return (objChoisi, distanceMin)
        return objChoisi

    def PlusProcheVolOiseau(self, liste : list, recherche):
        distance = []
        
        for obj in liste:
            x1 = self.cellule.x
            y1 = self.cellule.y
            if recherche == "Tache" :
                x2 = obj.lieuDepart.cellule.getPosition()[0]
                y2 = obj.lieuDepart.cellule.getPosition()[1]
            elif recherche == "Station" :
                x2 = obj.cellule.getPosition()[0]
                y2 = obj.cellule.getPosition()[1]

            distance.append( (((x2-x1)**2) + ((y2 - y1)**2)) ** 0.5) 
        distanceMin = min(distance)
        tacheChoisi = liste[ distance.index( distanceMin ) ]

        return tacheChoisi



    def getDestination(self):
        return self.destination

    def ajouterMarchandise(self, stock : list) -> None:
        self.coffre.append(stock)

    def deposerMarchandise(self) -> None:
        self.coffre = []

    #méthode permettant au robot d'Acquérir une tache
    def AcquisitionTache(self, cameraMoovable, scale, tailleX, tailleLieuxMission, zoom) -> bool :
        retour = False
        if self.tache == None and self.EnchereEnCours == False :
            #tache la plus proche :
            NearbyTache = self.PlusProcheVolOiseau(self.simulation.getTaches(), "Tache")
            
            if type(NearbyTache) == Tache :
                self.gagnant = True
                retour = NearbyTache
            
            
            elif type(NearbyTache) == Enchere and self.EnchereEnCours == False and self.gagnant == False:
                self.setChemin(self.cellule.getPosition())
                NearbyTache.arriveeParticipant(self)

                retour = NearbyTache
            
        
            if self.gagnant :
                #je la définie comme étant la tâche du robot
                self.tache = NearbyTache

                #je la supprime de la liste des tâches de la simulation
                if type(self.tache) == Tache :
                    self.simulation.taches.remove(self.tache)
                        

                #je définie le lieu de depart de la tache comme etant le nouvel obj de destination du robot
                self.ObjetDestination = self.tache.getDepart()
                self.destination = self.tache.getDepart().getCellule().getPosition()
                self.setChemin(self.destination)

                #si le zoom est activé et que j'ai déjà zoomé alors je réinitialise la caméra :
                if cameraMoovable and scale != 1 :
                    tailleX = zoom.resetZoom2()
                #Je dessine le lieu départ
                self.tache.dessinerLieu(0, tailleX, tailleLieuxMission, 'red')
                self.outline='red'
                self.carte.carte.itemconfigure(self.form, outline = 'red', width = tailleX/10)

                self.gagnant = False

        #print("robot :", self.nom,"enchereEnCours :", self.EnchereEnCours)
        return retour
    
    

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
        retour = False

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
                self.outline='green'
                self.carte.carte.itemconfigure(self.form, outline = 'green', width = tailleX/10)

        #s'il a auparavant atteint le lieu de depart :
        if self.passéSurLieuDepart :
            #s'il a terminé la tâche :
            if self.estSurLieuArrive() :
                #on ajoute la recompense à son equipe :
                self.equipe.ajouterArgent(self.tache.recompense)
                #on ajoute la recompense au robot :
                self.argent += (self.tache.recompense)
                #je réinitialise les attributs d'instance :
                self.passéSurLieuDepart = False
                retour = self.tache
                self.tache = None
                self.outline='white'
                self.carte.carte.itemconfigure(self.form, outline = 'white', width = tailleX/tailleX)
                print('Tache terminée ! ', self.equipe.name, ' argent : ', self.equipe.argent)
                return retour
        
    def checkBatterie(self, tailleX):
        if self.batterie < 0:
            print("J'ai moins 0 en batterie enculé : " + str(self.batterie) )
        stations = self.carte.getStationRecharge()
        stationPlusProche = self.PlusProcheVolOiseau(stations, "Station")
        distance = len(self.carte.resolution(self.cellule.getPosition(), stationPlusProche.getCellule().getPosition()))

        if (distance + 1) * self.perteBatterie > self.batterie - 2*self.perteBatterie:
            if not isinstance(self.ObjetDestination, StationRecharge) :
                self.PreviousObjetDestination = self.ObjetDestination
                self.PreviousDestination = self.destination
                self.PreviousOutline = self.outline

                self.ObjetDestination = stationPlusProche
                self.destination = stationPlusProche.getCellule().getPosition()
                self.setChemin(self.destination)  

            self.outline='blue'
            self.carte.carte.itemconfigure(self.form, outline = 'blue', width = tailleX/10)


            #self.ObjetDestination = stationPlusProche
            #self.destination = stationPlusProche.getCellule().getPosition()


            #self.setChemin(self.destination)


            if (self.enRecharge == False) :
                self.estSurStation()

        if self.batterie >= 100 :
            self.rechargeFinie(tailleX)


    def rechargeFinie(self, tailleX) :
        if (isinstance(self.ObjetDestination, StationRecharge) and (self.cellule.getPosition() == self.destination)) :
            self.enRecharge=False
            self.ObjetDestination.departRobot(self)

            self.outline=self.PreviousOutline
            self.carte.carte.itemconfigure(self.form, outline = self.outline, width = tailleX/10)
                

            self.ObjetDestination = self.PreviousObjetDestination
            self.destination = self.PreviousDestination
            self.setChemin(self.destination)



    def estSurStation(self) :
        #self.enRecharge=False
        if (isinstance(self.ObjetDestination, StationRecharge) and (self.cellule.getPosition() == self.destination)) :
            if self.ObjetDestination in self.carte.lieu :
                self.ObjetDestination.arriveeRobot(self)
                self.enRecharge=True









        

        
