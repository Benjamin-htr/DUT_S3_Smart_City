from classes.ControlSimulation import ControlSimulation
from tkinter import *

class GestionSimulation:
    def __init__(self, nbLieuMission, nbStationRecharge):
        self.nbLieuMission = nbLieuMission
        self.nbStationRecharge = nbStationRecharge
        #creation de la fenêtre :
        self.window = Tk()
        self.EnCours=False
        self.controlSimulation = None
        

        #canvas :
        hauteur = 650
        largeur = 650
        self.CanvasCarte = Canvas(self.window, bg = 'black', height = hauteur, width = largeur)
        self.CanvasCarte.grid(row = 0, column = 2, rowspan=10, padx = 10, pady=25)
        
        #personnalisation de la fenêtre
        self.window.title('smart_City')
        self.window.geometry('1350x700')
        self.window.resizable(height=False, width=False)
        self.window.iconbitmap("logo.ico")


    def lancerSimulation(self):
        if (self.EnCours != True) :
            controlSimulation = ControlSimulation()
            sim = controlSimulation.creerSimulation(self.nbLieuMission, self.nbStationRecharge, self.CanvasCarte)
            self.controlSimulation = controlSimulation
            self.EnCours=True

        
    def arreterSimulation(self):

        self.EnCours=False
        self.CanvasCarte.delete("all")
        return None
        

    def afficherSimulation(self) :
        #Bouton LancerSimulation :
        LancerSimulation = Button(self.window, text='Lancer Simulation', height = 1, width = 20, command=lambda:self.lancerSimulation())
        LancerSimulation.grid(row= 0, column=0)

        #Bouton ArreterSimulation :
        ArreterSimulation = Button(self.window, text='Arreter Simulation', height = 1, width = 20, command=lambda:self.arreterSimulation())
        ArreterSimulation.grid(row= 0, column=1)

        self.window.mainloop()
    

    def ajouterRobot(self, name) -> None:
        self.controlSimulation.creerRobot(name)