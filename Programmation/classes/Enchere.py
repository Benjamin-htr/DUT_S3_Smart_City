from classes.Tache import Tache
from classes.Carte import Carte
from tkinter import *
from tkinter.font import Font
from classes.ScrollFrame import ScrollFrame
import random

class Enchere(Tache):
    def __init__(self, carte : Carte, numero, simulation) :
        super().__init__(carte, random.randint(300,500))
        self.simulation = simulation
        self.numero = numero
        self.participants = []
        self.duree = 10 #en seconde

        self.offres = {}

        self.nomGagnant = "Aucun"


        self.EnchereFrame = None
        self.EnchereTime = None
        self.EnchereGagnant = None
        
        self.robotFrame = {}
        self.descriptionRobots = {}




    def arriveeParticipant(self, robot) :
        if robot not in self.participants and self.duree > 1:
            #print("arrive de", robot.nom, "dans enchere numero", self.numero)
            robot.EnchereEnCours = True
            self.participants.append(robot)
        


    def checkEnchere(self, vitesse) :
        if len(self.participants) >= 1 :
            self.JouerEnchere()
            self.duree -= vitesse/1000
            


    """def JouerEnchere(self) :
        retour = False
        if len(self.participants) == 1 :
            self.nomGagnant = self.participants[0].nom
            
        if self.duree <= 0 and len(self.participants) == 1 :
            self.nomGagnant = self.participants[0].nom
            self.participants[0].gagnant = True
            retour = True
            self.enchereTerminée()


        if len(self.participants) >= 2 :
            for robot in self.participants :
                if robot not in self.offres :
                    self.offres[robot] = self.Encherir(robot)

            self.gagnant = min(self.offres, key=self.offres.get)

            self.nomGagnant = self.gagnant.nom
        
        if self.duree <= 0 and len(self.participants) >= 2 :
            self.gagnant.gagnant = True
            self.enchereTerminée()"""

    def JouerEnchere(self) :
        retour = False
        if len(self.participants) == 1 :
            self.nomGagnant = self.participants[0].nom

        
        elif len(self.participants) >= 2 :
            for robot in self.participants :
                if robot not in self.offres :
                    self.offres[robot] = self.Encherir(robot)

            self.gagnant = min(self.offres, key=self.offres.get)

            self.nomGagnant = self.gagnant.nom
            
        if self.duree == 0 :
            if len(self.participants) == 1 :
                self.nomGagnant = self.participants[0].nom
                self.gagnant = self.participants[0]
                self.gagnant.gagnant = True
                retour = True
                #print("1er elif ", "enchere no ", self.numero, "gagnat :", self.gagnant.nom)
                self.gagnant.affecterTache(self)
                self.enchereTerminée()

            elif len(self.participants) >= 2 :
                self.gagnant.gagnant = True
                #print("2eme elif ", "enchere no ", self.numero, "gagnat :", self.gagnant.nom)
                self.gagnant.affecterTache(self)
                self.enchereTerminée()
            
            
    def enchereTerminée(self) :
        for i in range(len(self.participants)) :
            self.participants[i].offre = "Aucune"
            self.participants[i].EnchereEnCours = False
            #print(self.participants[i].nom, " : ", self.participants[0].EnchereEnCours)

        self.EnchereFrame.pack_forget()
        self.EnchereFrame.destroy()
        #self.simulation.taches.remove(self)
        del self





    def Encherir(self, robot) -> int :
        offre = random.randint(int(self.recompense*(80/100)), self.recompense)
        robot.offre = offre
        return offre



    def dessinerEnchere(self, root, bg) :
        if len(self.participants) >= 1 and self.EnchereFrame == None :
            chaine = 'Enchere' + ' ' + str(self.numero)

            self.EnchereFrame = Frame(root, bg='red', highlightbackground="black", highlightthickness=1)
            self.EnchereFrame.pack(fill=X)

            EnchereName = Label(self.EnchereFrame, text=chaine, bg=bg, font=Font(family="Helvetica",size=24,weight="bold"), anchor=W)
            EnchereName.pack(fill=X)

            chaine = 'Temps Restant :' + ' ' + str(self.duree)

            self.EnchereTime = StringVar()
            self.EnchereTime.set(chaine)

            EnchereTime = Label(self.EnchereFrame, textvariable=self.EnchereTime, bg=bg, font=Font(family="Helvetica",size=18,weight="normal"), anchor=W)
            EnchereTime.pack(fill=X)

            chaine = 'En tête :' + ' ' + self.nomGagnant

            self.EnchereGagnant = StringVar()
            self.EnchereGagnant.set(chaine)

            EnchereGagnant = Label(self.EnchereFrame, textvariable=self.EnchereGagnant, bg=bg, font=Font(family="Helvetica",size=14,weight="normal"), anchor=W)
            EnchereGagnant.pack(fill=X)

            self.chargerRobots(bg)

            return self.EnchereFrame

    
    def chargerRobots(self, bg) :
        for robot in self.participants :
            #print(self.robotFrame)
            if robot not in self.robotFrame and self.EnchereFrame != None :
                name = robot.nom
                offre = robot.offre
                chaine = name + ' offre : ' + str(offre)

                self.descriptionRobots[robot] = StringVar()
                self.descriptionRobots[robot].set(chaine)

                self.robotFrame[robot] = Frame(self.EnchereFrame, bg=bg)
                RobotFrame = self.robotFrame[robot]
                RobotFrame.pack(fill=X)


                canva = Canvas(RobotFrame, bg = bg, height =28, width = 28, highlightthickness=0)
                canva.create_oval(2.5, 2.5, 24, 24, fill=robot.color, outline ='white')
                canva.grid(row=0, column=0, padx = 5)
                    


                Robot = Label(RobotFrame, textvariable = self.descriptionRobots[robot], bg=bg, font=Font(family="Helvetica",size=11,weight="normal"), anchor=W)
                Robot.grid(row=0, column = 1)


    def updateEnchereFrame(self, bg) :
        if self.EnchereFrame != None :
            #print(self.EnchereFrame)
            self.chargerRobots(bg)

            chaine = 'Temps Restant :' + ' ' + str(self.duree)
            self.EnchereTime.set(chaine)

            chaine = 'En tête :' + ' ' + self.nomGagnant  
            self.EnchereGagnant.set(chaine)

            for robot in self.participants :
                name = robot.nom
                offre = robot.offre
                chaine = name + ' offre : ' + str(offre)

                self.descriptionRobots[robot].set(chaine)




        