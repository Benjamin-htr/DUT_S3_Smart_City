from tkinter import *
from tkinter.font import Font
from classes.ScrollFrame import ScrollFrame

class AffichageEncheres:
    def __init__(self, window):
        self.window = window

        self.Encheres = None

        self.bg='gray87'

        self.dessinerAffichageEncheres()

        self.Enchereframe = {}

        self.EnchereTime = {}

        self.EnchereGagnant = {}

        self.robotFrame = {}

        #dictionnaire contenant les descriptions des robots :
        self.descriptionRobots = {}

    

    def dessinerAffichageEncheres(self) :
        #on dessine le cadre :
        self.frame = Frame(self.window, height = 500, width=270, bg=self.bg, highlightbackground="gray65", highlightthickness=1)
        #on l'affiche :
        self.frame.grid(row=1, column =4, padx=10)
        self.frame.pack_propagate(False)
        self.frame.grid_propagate(False)

        #on nome le cadre ici Scoreboard :
        label = Label(self.frame, text = 'Encheres', bg=self.bg, font=Font(family="Helvetica",size=20,weight="bold"), borderwidth=1, relief='solid')
        label.pack(fill=X)

    def chargerDonnees(self, encheres) :
        self.ScrollFrame = ScrollFrame(self.frame, self.bg) # add a new scrollable frame.
        
        self.chargerEncheres(encheres)

        self.ScrollFrame.pack(fill="both", expand=True)


    def chargerEncheres(self, encheres) :
        for enchere in encheres :
            self.chargerEnchere(enchere)


    def chargerEnchere(self, enchere) :
        if len(enchere.participants) >= 1 :
            numero = enchere.numero
            chaine = 'Enchere' + ' ' + str(numero)

            self.Enchereframe[enchere] = Frame(self.ScrollFrame.viewPort, bg=self.bg, highlightbackground="black", highlightthickness=1)
            Enchereframe = self.Enchereframe[enchere]
            Enchereframe.pack(fill=X)

            EnchereName = Label(Enchereframe, text=chaine, bg=self.bg, font=Font(family="Helvetica",size=24,weight="bold"), anchor=W)
            EnchereName.pack(fill=X)

            time=enchere.duree
            chaine = 'Temps Restant :' + ' ' + str(time)

            self.EnchereTime[enchere] = StringVar()
            self.EnchereTime[enchere].set(chaine)

            EnchereTime = Label(Enchereframe, textvariable=self.EnchereTime[enchere], bg=self.bg, font=Font(family="Helvetica",size=18,weight="normal"), anchor=W)
            EnchereTime.pack(fill=X)

            gagnant=enchere.nomGagnant
            chaine = 'En tête :' + ' ' + gagnant

            self.EnchereGagnant[enchere] = StringVar()
            self.EnchereGagnant[enchere].set(chaine)

            EnchereGagnant = Label(Enchereframe, textvariable=self.EnchereGagnant[enchere], bg=self.bg, font=Font(family="Helvetica",size=14,weight="normal"), anchor=W)
            EnchereGagnant.pack(fill=X)

            RobotsFrame = Frame(Enchereframe, bg=self.bg, highlightbackground="black", highlightthickness=0)
            RobotsFrame.pack(fill=X)

            self.chargerRobots(Enchereframe, enchere)

    def chargerRobots(self, Enchereframe, enchere) :
        for robot in enchere.participants :
            if robot not in self.robotFrame :
                name = robot.nom
                offre = robot.offre
                chaine = name + ' offre : ' + str(offre)

                self.descriptionRobots[robot] = StringVar()
                self.descriptionRobots[robot].set(chaine)

                self.robotFrame[robot] = Frame(Enchereframe, bg=self.bg)
                RobotFrame = self.robotFrame[robot]
                RobotFrame.pack(fill=X)


                canva = Canvas(RobotFrame, bg = self.bg, height =28, width = 28, highlightthickness=0)
                canva.create_oval(2.5, 2.5, 24, 24, fill=robot.color, outline ='white')
                canva.grid(row=0, column=0, padx = 5)
                


                Robot = Label(RobotFrame, textvariable = self.descriptionRobots[robot], bg=self.bg, font=Font(family="Helvetica",size=11,weight="normal"), anchor=W)
                Robot.grid(row=0, column = 1)


    def updateAffichageEncheres(self, encheres) :
        for enchere in encheres :
            if enchere not in self.Enchereframe :
                self.chargerEnchere(enchere)

        key_copy = tuple(self.Enchereframe.keys())
        for enchere in key_copy :
            if enchere not in encheres :
                self.deleteEnchereFrame(self.Enchereframe[enchere], enchere)

        for enchere in self.Enchereframe :
            time=enchere.duree
            chaine = 'Temps Restant :' + ' ' + str(time)
            self.EnchereTime[enchere].set(chaine)

            gagnant=enchere.nomGagnant
            chaine = 'En tête :' + ' ' + gagnant
            self.EnchereGagnant[enchere].set(chaine)

            self.chargerRobots(self.Enchereframe[enchere], enchere)

            for robot in enchere.participants :
                name = robot.nom
                offre = robot.offre
                chaine = name + ' : offre : ' + str(offre)

                self.descriptionRobots[robot].set(chaine)
                #self.robotsCanvas[robot].itemconfigure(self.robotsFormes[robot], outline = robot.outline, width=2)
            
    def deleteEnchereFrame(self, Encherframe, enchere) :
        self.Enchereframe[enchere].destroy()
        self.Enchereframe.pop(enchere, False)
        self.EnchereTime.pop(enchere, False)
        self.EnchereGagnant.pop(enchere, False)
        for robot in enchere.participants :
            self.robotFrame.pop(robot, False)
            self.descriptionRobots.pop(robot, False)


    def resetAffichageEncheres(self) :
        self.ScrollFrame.destroy()







        