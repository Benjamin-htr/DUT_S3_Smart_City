from classes.ControlSimulation import ControlSimulation
from tkinter import *

class GestionSimulation:
    def __init__(self, nbLieuMission, nbStationRecharge):
        self.nbLieuMission = nbLieuMission
        self.nbStationRecharge = nbStationRecharge
        #creation de la fenêtre :
        self.window = Tk()

        #personnalisation de la fenêtre
        self.window.title('smart_City')
        self.window.geometry('1350x700')
        self.window.resizable(height=False, width=False)
        self.window.iconbitmap("logo.ico")

        #canvas :
        hauteur = 650
        largeur = 650
        self.CanvasCarte = Canvas(self.window, bg = 'black', height = hauteur, width = largeur)

        
    
    def lancerSimulation(self):
        controlSimulation = ControlSimulation()
        sim = controlSimulation.creerSimulation(self.nbLieuMission, self.nbStationRecharge, self.CanvasCarte)
        self.window.mainloop()
    
    def arreterSimulation(self):
        return None