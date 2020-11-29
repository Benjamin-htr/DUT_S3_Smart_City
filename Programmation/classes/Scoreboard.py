from tkinter import *
from tkinter.font import Font

class Scoreboard:
    def __init__(self, window):
        self.window = window
        self.equipes = None

        self.bg='gray87'

        self.frames=[]

        self.dessinerScoreboard()

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

    def chargerDonnees(self, equipes) :
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
            equipe.grid(row=0, column = 1)

    def resetScoreboard(self) :
        for i in range (len(self.frames)) :
            self.frames[i].destroy()

    def updateScoreboard(self, equipes) :
        self.resetScoreboard()
        self.chargerDonnees(equipes)
            

            


        