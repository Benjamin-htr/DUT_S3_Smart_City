from tkinter import *
from tkinter.font import Font
from classes.ScrollFrame import ScrollFrame

class AffichageEncheres:
    def __init__(self, window):
        self.window = window

        self.Encheres = None

        self.bg='gray87'

        self.dessinerAffichageEncheres()

        self.EncheresFrames = []

        

       
    

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
            self.EncheresFrames.append(enchere.dessinerEnchere(self.ScrollFrame.viewPort, self.bg))



    def updateAffichageEncheres(self, encheres) :
        for enchere in encheres :
            enchere.dessinerEnchere(self.ScrollFrame.viewPort, self.bg)  
            enchere.updateEnchereFrame(self.bg)
        
            
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







        