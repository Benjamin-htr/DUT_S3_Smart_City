from tkinter import *
from tkinter.font import Font
from classes.ScrollFrame import ScrollFrame

class Scoreboard:
    def __init__(self, window):
        self.window = window
        self.equipes = None

        self.bg='gray87'

        self.frames=[]

        self.dessinerScoreboard()

        self.scores = None

        #dictionnaire contenant les descriptions des equipes :
        self.descriptionEquipes = {}

        self.robotsCanvas={}

        self.robotsFormes={}

        #dictionnaire contenant les descriptions des robots :
        self.descriptionRobots = {}

    def dessinerScoreboard(self) :
        #on dessine le cadre :
        self.frame = Frame(self.window, height = 500, width=350, bg=self.bg, highlightbackground="gray65", highlightthickness=1)
        #on l'affiche :
        self.frame.grid(row=1, column =0, columnspan = 2, padx=10)
        self.frame.pack_propagate(False)
        self.frame.grid_propagate(False)

        #on nome le cadre ici Scoreboard :
        label = Label(self.frame, text = 'Scoreboard', bg=self.bg, font=Font(family="Helvetica",size=20,weight="bold"), borderwidth=1, relief='solid')
        label.pack(fill=X)

        """
        #on nome le cadre ici Scoreboard :
        label2 = Label(frame, text = 'Scoreboard', bg=bg, font=Font(family="Helvetica",size=14,weight="normal"), borderwidth=1, relief='solid', anchor=W)
        label2.pack(fill=X)
        """

    """def chargerDonnees(self, equipes) :
        self.equipes = equipes
        for i in range(len(self.equipes)) :
            name = self.equipes[i].name
            argent = self.equipes[i].argent
            chaine = name + ' : ' + str(argent)
            frame = Frame(self.frame, bg=self.bg, highlightbackground="black", highlightthickness=1)
            self.frames.append(frame)
            frame.pack(fill=X)
            canva = Canvas(frame, bg = self.equipes[i].color, height =19, width = 19, highlightthickness=0)
            canva.grid(row=0, column=0, padx = 5)
            equipe = Label(frame, text = chaine, bg=self.bg, font=Font(family="Helvetica",size=14,weight="normal"), anchor=W)
            equipe.grid(row=0, column = 1)"""

    def chargerDonnees(self, equipes) :
        self.ScoreFrame = ScrollFrame(self.frame, self.bg) # add a new scrollable frame.
        
        self.chargerEquipes(equipes)

        self.ScoreFrame.pack(fill="both", expand=True)

    def chargerEquipes(self, equipes) :
        self.equipes = equipes

        for i in range(len(self.equipes)) :
            name = self.equipes[i].name
            argent = self.equipes[i].argent
            chaine = name + ' : ' + str(argent)

            self.descriptionEquipes[self.equipes[i]] = StringVar()
            self.descriptionEquipes[self.equipes[i]].set(chaine)

            Equipeframe = Frame(self.ScoreFrame.viewPort, bg=self.bg, highlightbackground="black", highlightthickness=1)
            Equipeframe.pack(fill=X)

            NameEquipeFrame = Frame(Equipeframe, bg=self.bg)
            NameEquipeFrame.pack(fill=X)
            letter = Label(NameEquipeFrame, text=self.equipes[i].letter, bg=self.bg, font=Font(family="Fixedsys",size=24,weight="bold"), anchor=W)
            letter.grid(row=0, column=0)
            equipe = Label(NameEquipeFrame, textvariable = self.descriptionEquipes[self.equipes[i]], bg=self.bg, font=Font(family="Helvetica",size=14,weight="bold"), anchor=W)
            equipe.grid(row=0, column = 1)

            self.chargerRobots(Equipeframe, equipes[i])

                


    def chargerRobots(self, Equipeframe, equipe) :
        for j in range (len(equipe.robots)) :
            name = equipe.robots[j].nom
            argent = equipe.robots[j].argent
            batterie = equipe.robots[j].batterie
            chaine = name + ' : ' + str(argent)+'  batterie : '+ str(batterie)+'%'

            self.descriptionRobots[equipe.robots[j]] = StringVar()
            self.descriptionRobots[equipe.robots[j]].set(chaine)

            RobotFrame = Frame(Equipeframe, bg=self.bg)
            RobotFrame.pack(fill=X)


            self.robotsCanvas[equipe.robots[j]] = Canvas(RobotFrame, bg = self.bg, height =28, width = 28, highlightthickness=0)
            self.robotsFormes[equipe.robots[j]] = self.robotsCanvas[equipe.robots[j]].create_oval(2.5, 2.5, 24, 24, fill=equipe.robots[j].color, outline ='white')
            self.robotsCanvas[equipe.robots[j]].grid(row=0, column=0, padx = 5)
            


            Robot = Label(RobotFrame, textvariable = self.descriptionRobots[equipe.robots[j]], bg=self.bg, font=Font(family="Helvetica",size=11,weight="normal"), anchor=W)
            Robot.grid(row=0, column = 1)



    def resetScoreboard(self) :
        self.ScoreFrame.destroy()
        for i in range (len(self.frames)) :
            self.frames[i].destroy()

    def updateScoreboard(self, equipes) :
        for i in range(len(equipes)) :
            name = self.equipes[i].name
            argent = self.equipes[i].argent
            chaine = name + ' : ' + str(argent)

            self.descriptionEquipes[self.equipes[i]].set(chaine)

            for j in range (len(self.equipes[i].robots)) :
                robot = self.equipes[i].robots[j]
                name = robot.nom
                argent = robot.argent
                batterie = robot.batterie
                chaine = name + ' : ' + str(argent)+'  batterie : '+ str(batterie)+'%'

                self.descriptionRobots[robot].set(chaine)
                self.robotsCanvas[robot].itemconfigure(self.robotsFormes[robot], outline = robot.outline, width=2)


            

            


        