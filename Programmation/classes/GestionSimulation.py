from classes.ControlSimulation import ControlSimulation
from classes.Scoreboard import Scoreboard
from classes.AffichageEncheres import AffichageEncheres
from classes.Zoom import zoom
from classes.Tache import Tache
from classes.Enchere import Enchere
from tkinter import *
from tkinter import messagebox
import time
import random


class GestionSimulation:
    def __init__(self):
        self.zoom = None
        #creation de la fenêtre :
        self.window = Tk()

        #attribut précisant l'état de la simulation True ou False.
        self.EnCours=False
        #attribut précisant l'existance de la fenêtre de création de robot.
        self.WindowNewRobState=False
        #attribut précisant l'existance des options.
        self.WindowSettingState=False
        
        #controlSimulation (n'existe pas pour l'instant, sera créer lorsque l'utilisateur appuiera sur lancer simulation)
        self.controlSimulation = None
        



        #taille du robot :
        self.tailleRobot=65
        #densite des murs 0 -> il y en a moins mais pas aucun !, 100 -> il y en a plus 
        self.densite=60
        #taille des stations de recharges :
        self.tailleStationRecharge=45
        #taille des lieux de missions :
        self.tailleLieuxMission=55

        #taille des tâches :
        self.tailleTaches=30


        #nb de cellules (nb de cellule en largeur = nb de cellule en hauteur):
        self.nbCells=20

        #taille des cellules (utiles pour l'affichage de la carte)
        self.tailleX=0
        self.tailleY=0

        # niveaux de zoom (utile pour retailler la carte)
        self.scale = 1

        #peut on bouger la camero + zoom
        self.cameraMoovable = True



        #permet de savoir si la simulation est en pause ou non :
        self.pause=False
        self.textStartButton=StringVar()
        self.textStartButton.set("Lancer Simulation")


    

        #canvas :
        hauteur = 650
        largeur = 650


        #création du canvas
        self.CanvasCarte = Canvas(self.window, bg = 'black', height = hauteur, width = largeur)

        #affichage du canvas
        self.CanvasCarte.grid(row = 0, column = 2, rowspan=10, pady=25)
        
        
        #personnalisation de la fenêtre
        self.window.title('smart_City')
        self.window.geometry('1350x700')
        self.window.iconbitmap('logo.ico')
        self.window.resizable(height=False, width=False)

        #on créer le scoreboard :
        self.scoreboard=Scoreboard(self.window)

        #on créer l'affichage des encheres' :
        self.AffichageEncheres=AffichageEncheres(self.window)

        self.vitesse = 1000 #en miliseconde






    #ajoute le robot à la simulation (utilisée notamment dans nouveauRobot())
    def ajouterRobot(self, name) -> None:
        self.controlSimulation.creerRobot(name)

    #affiche les robots (utilisée au lancement de la simulation)
    def afficherRobots(self) :
        Robots = self.getRobots()
        for robot in Robots :
            robot.dessinerRobot(self.tailleX, self.tailleRobot)
        


    #fonction permettant d'afficher le déplacement du robot)
    def deplacement(self, typeDeplacement="random") :
        #si la simulation est stoppée on arrete le deplacement
        if self.EnCours == False :
            return

        robots=self.getRobots()
        #print("nb taches :", len(self.controlSimulation.simulation.getTaches()))
        if self.pause == False :
            self.controlSimulation.simulation.checkEnchere(self.vitesse)
            self.AffichageEncheres.updateAffichageEncheres(self.controlSimulation.simulation.getEncheres())
        for i in range(len(robots)):
        
            currentCell=robots[i].cellule
            #print(robots[i].nom, " :", currentCell)
            if typeDeplacement == "random" and self.pause == False :
                deplacement=robots[i].deplacementRandom(self.tailleX)
                #print(robots[i].nom, " :", deplacementRandom)

            elif typeDeplacement == "djikstra" and self.pause == False :
                #self.controlSimulation.simulation.robots[i].setChemin(robots[i].choixTacheDijkstra(self.getTaches()).getDepart().getCellule().getPosition())
                #print(self.controlSimulation.simulation.robots[i].chemin.chemin)
                tache = robots[i].AcquisitionTache(self.cameraMoovable, self.scale, self.tailleX, self.tailleLieuxMission, self.zoom)

                deplacement=robots[i].deplacement(self.tailleX)

                tacheAccompli = robots[i].AccomplirTâche(self.cameraMoovable, self.scale, self.tailleX, self.tailleLieuxMission, self.zoom)

                if type(tacheAccompli) == Tache :
                    self.controlSimulation.simulation.ajouterTache()
                elif type(tacheAccompli) == Enchere :
                    self.controlSimulation.simulation.ajouterEnchere()

                
                

                        
                #print("nb taches restantes :", len(self.controlSimulation.simulation.taches))
                #print("nb lieu :", len(self.controlSimulation.simulation.carte.lieu))
                    

                #print("Deplacement d"robots[i].getDestination())
            robots[i].checkBatterie(self.tailleX)
        if self.pause == False :
            self.scoreboard.updateScoreboard(self.controlSimulation.simulation.equipes)
            
            self.controlSimulation.simulation.launchStations(self.tailleX)

        self.CanvasCarte.after(self.vitesse, lambda : self.deplacement(typeDeplacement))


    def lancerSimulation(self):
        if (self.EnCours == False) :
            self.textStartButton.set("Mettre en pause")
            
            hauteur = 650
            largeur = 650

            #on créer le canvas :
            self.origX = self.CanvasCarte.xview()[0]
            self.origY = self.CanvasCarte.yview()[0]


            #on créer la simulation :
            controlSimulation = ControlSimulation()
            sim = controlSimulation.creerSimulation(self.CanvasCarte, self.nbCells, self.densite, self.tailleStationRecharge, self.tailleLieuxMission)
            self.controlSimulation = controlSimulation
        

            #elle est maintenant en cours :
            self.EnCours=True

            self.scoreboard.chargerDonnees(self.controlSimulation.simulation.equipes)
            self.AffichageEncheres.chargerDonnees(self.controlSimulation.simulation.getEncheres())

            #on calcule la taille des bords des cellules (taille du canvas 650 divisé par le nombre de cellule)
            self.tailleX=650/self.controlSimulation.simulation.carte.nx
            self.tailleY=self.tailleX


            #on affiche les robots :
            self.afficherRobots()
            

            # Tests
            #print(self.controlSimulation.simulation.carte.attenantes((2,2)))
            #print(self.controlSimulation.simulation.carte.resolution((1,1), (5,5)))
            #print(self.controlSimulation.simulation.robots[0].deplacement((5,5)))
            #self.controlSimulation.simulation.robots[0].setChemin((9,9))
            #print(self.controlSimulation.simulation.robots[0].deplacement())

            #on créer l'instance de zoom permettant de zoomer comme on le souhaite
            if self.cameraMoovable :
                self.zoom = zoom(self, self.window)

            #on lance le déplacement des robots (avec en paramètre l'algo utilisé (random par défaut ou djikstra))
            self.deplacement("djikstra")

        else :
            if self.pause == False :
                self.pause = True
                self.textStartButton.set("Lancer Simulation")
            else :
                self.pause = False
                self.textStartButton.set("Mettre en pause")
    
        
    def arreterSimulation(self):
        if (self.EnCours==True) :
            self.afficherGagnant()
            self.textStartButton.set("Lancer Simulation")
            self.pause=False
            self.EnCours=False
            if self.cameraMoovable :
                self.zoom.resetZoom2()
                del self.zoom
            self.CanvasCarte.delete("all")
            self.scoreboard.resetScoreboard()
            self.AffichageEncheres.resetAffichageEncheres()
            self.controlSimulation = None
            self.tailleX=0
            self.scale=1
            return None

    def afficherGagnant(self) -> None:
        windowGagnant = Toplevel(self.window)
        windowGagnant.title("Gagnant de la simulation")
        windowGagnant.geometry("300x50")
        windowGagnant.resizable(height=False, width=False)
        if self.controlSimulation.simulation.egalité():
            Label(windowGagnant, text="Toutes les équipes ont été aussi fortes !").pack()
            Label(windowGagnant, text="Il y a égalité").pack()
        else:
            equipeGagnante = self.controlSimulation.simulation.getEquipeGagnant()
            Label(windowGagnant, text="L'équipe gagnante :").pack()
            Label(windowGagnant, text=equipeGagnante.getName() + " avec " + str(equipeGagnante.getArgent()) + " points.").pack()

        
    """
    Cette méthode permet d'ouvrir la fenêtre permettant de créer un nouveau robot si elle n'existe pas déjà et si la simulation est 
    en cours. Si c'est le cas elle créer le robot et l'affiche.
    """
    def NouveauRobot(self):
        if self.WindowNewRobState == False and self.EnCours == True :
            self.WindowNewRobState = True
            newWindow = Toplevel(self.window) 
            newWindow.title("Nouveau robot") 
            newWindow.geometry("200x75")
            newWindow.resizable(height=False, width=False)
            Label(newWindow,  text ="Entrez le nom :").pack()
            value = StringVar()
            #value.set("texte par défaut")
            entree = Entry(newWindow, textvariable=value, width=30)
            entree.pack()

            #évènement lancé lorsque l'utilisateur appuie sur entrer :
            def EnregisterNom(event):
                #si l'utilisateur décide de confirmer son choix :
                if messagebox.askyesno("", "Confirmez vous votre choix de nom ?"):
                    #on rénitialise le zoom
                    if self.cameraMoovable :
                        self.zoom.resetZoom2()
            
                    print(entree.get())
                    name = entree.get()
                    #ajout du robot :
                    #on ajoute le robot à la simulation :
                    self.ajouterRobot(name)

                    liste=self.getRobots()
                    rob=liste[len(liste)-1]
                    #le robot cherche la tache la plus proche de lui :
                    NearbyTache = rob.choixTacheVolOiseau(self.getTaches())
                    #on définit cette tâche comme étant sa destination :
                    rob.setChemin(NearbyTache.getCelluleTache().getPosition())
                    rob.ObjetDestination = NearbyTache

                    x = rob.cellule.x
                    y = rob.cellule.y

                    #on dessine le robot :
                    rob.dessinerRobot(self.tailleX, self.tailleRobot, True)


                    newWindow.destroy()
                    self.WindowNewRobState = False
                    print(self.getRobots())


            def on_closing():
                if messagebox.askokcancel("Quit", "Voulez vous vraiment stopper la création d'un nouveau robot ?"):
                    newWindow.destroy()
                    self.WindowNewRobState = False

            newWindow.protocol("WM_DELETE_WINDOW", on_closing)
            entree.bind("<Return>", EnregisterNom)


    def getRobots(self) -> list:
        return self.controlSimulation.getRobots()

    def getTaches(self) -> list:
        return self.controlSimulation.getTaches()

    """
    Méthode permettant d'ouvrir la fenêtre des options si elle n'est pas déja ouverte :
    """
    def OpenSettings(self) :
        if self.WindowSettingState == False :
            self.WindowSettingState = True
            newWindow = Toplevel(self.window) 
            newWindow.title("Paramètres") 
            newWindow.resizable(height=False, width=False)
            #newWindow.overrideredirect(True) 
 
            Label(newWindow,  text ="Nombre de cellules de 10 à 100 :",width=25, anchor=W, justify=LEFT).grid(row=0, sticky=W)
            var1 = IntVar(newWindow)
            var1.set(self.nbCells)
            entree1 = Spinbox(newWindow, textvariable=var1, from_=10, to=100, width=10)
            entree1.grid(row=1, sticky=W)

            Label(newWindow,  text ="Densité labyrinthe (nb Murs en %) de 0 à 100 :",width=25,  wraplength=190, anchor=W, justify=LEFT).grid(row=2, sticky=W)
            var2 = IntVar(newWindow)
            var2.set(self.densite)
            entree2 = Spinbox(newWindow, textvariable=var2, from_=0, to=100, width=10)
            entree2.grid(row=3, sticky=W)

            Label(newWindow,  text ="Taille des robots (en %) de 30 à 100 :", wraplength=180, width=25, anchor=W, justify=LEFT).grid(row=4, sticky=W)
            var3 = IntVar(newWindow)
            var3.set(self.tailleRobot)
            entree3 = Spinbox(newWindow, textvariable=var3, from_=30, to=100, width=10)
            entree3.grid(row=5, sticky=W)

            Label(newWindow,  text ="Taille des stations des lieux de missions (en %) de 30 à 100 :", wraplength=190, width=25, anchor=W, justify=LEFT).grid(row=6, sticky=W)
            var4 = IntVar(newWindow)
            var4.set(self.tailleLieuxMission)
            entree4 = Spinbox(newWindow, textvariable=var4, from_=30, to=100, width=10)
            entree4.grid(row=7, sticky=W)

            Label(newWindow,  text ="Taille des stations de recharges (en %) de 30 à 100 :", wraplength=180, width=25, anchor=W, justify=LEFT).grid(row=8, sticky=W)
            var5 = IntVar(newWindow)
            var5.set(self.tailleStationRecharge)
            entree5 = Spinbox(newWindow, textvariable=var5, from_=30, to=100, width=10)
            entree5.grid(row=9, sticky=W)

            Confirmer = Button(newWindow, text='Confirmer', height = 1, width = 20, cursor="hand2", overrelief=GROOVE, command=lambda:Confirmer())
            Confirmer.grid(row= 10, pady=10)

            #enregistre les modifications effectuées
            def Confirmer() :
                self.tailleRobot=int(entree3.get())
                self.densite=int(entree2.get())
                self.tailleStationRecharge=int(entree5.get())
                self.tailleLieuxMission=int(entree4.get())
                self.nbCells=int(entree1.get())
                


            def on_closing():
                newWindow.destroy()
                self.WindowSettingState = False

            newWindow.protocol("WM_DELETE_WINDOW", on_closing)


    def afficherSimulation(self) :
            Gestion = Frame(self.window)
            Gestion.grid(row=0, column = 0, columnspan=2, padx = 10)
            #Bouton LancerSimulation :
            LancerSimulation = Button(Gestion, textvariable=self.textStartButton, height = 1, width = 20, cursor="hand2", overrelief=GROOVE, command=lambda:self.lancerSimulation())
            LancerSimulation.pack(side=LEFT)

            #Bouton ArreterSimulation :
            
            ArreterSimulation = Button(Gestion, text='Réinitialiser Simulation', height = 1, width = 20, cursor="hand2", overrelief=GROOVE, command=lambda:self.arreterSimulation())
            ArreterSimulation.pack(side=RIGHT)

            #Bouton création robot :
            #command=lambda:self.lancerSimulation()
            NouveauRobot = Button(self.window, text='Nouveau Robot', height = 1, width = 20, cursor="hand2", overrelief=GROOVE, command =lambda:self.NouveauRobot())
            #NouveauRobot.grid(row= 1, column=0, columnspan=2) 

            #Carte :
            #self.CanvasCarte.grid(row = 0, column = 2, rowspan=10, padx = 10, pady=25)

            #Bouton settings :
            icon=PhotoImage(file="settings.png")
            settings = Button(self.window, image = icon, height = 20, width = 20, cursor="hand2", overrelief=GROOVE, command =lambda:self.OpenSettings())
            settings.grid(row= 0, column=3) 

            self.window.mainloop()