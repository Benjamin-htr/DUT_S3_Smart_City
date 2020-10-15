from classes.ControlSimulation import ControlSimulation
from tkinter import *
from tkinter import messagebox

class GestionSimulation:
    def __init__(self, nbLieuMission, nbStationRecharge):
        self.nbLieuMission = nbLieuMission
        self.nbStationRecharge = nbStationRecharge
        #creation de la fenêtre :
        self.window = Tk()
        self.EnCours=False
        self.WindowNewRobState=False
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

    #boutons interface :
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
        
    def NouveauRobot(self):
        if self.WindowNewRobState == False :
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

            def EnregisterNom(event):
                if messagebox.askyesno("", "Confirmez vous votre choix de nom ?"):
                    print(entree.get())
                    newWindow.destroy()
                    self.WindowNewRobState = False


            def on_closing():
                if messagebox.askokcancel("Quit", "Voulez vous vraiment stopper la création d'un nouveau robot ?"):
                    newWindow.destroy()
                    self.WindowNewRobState = False

            newWindow.protocol("WM_DELETE_WINDOW", on_closing)
            entree.bind("<Return>", EnregisterNom)





    def afficherSimulation(self) :
        #Bouton LancerSimulation :
        LancerSimulation = Button(self.window, text='Lancer Simulation', height = 1, width = 20, cursor="hand2", overrelief=GROOVE, command=lambda:self.lancerSimulation())
        LancerSimulation.grid(row= 0, column=0)

        #Bouton ArreterSimulation :
        ArreterSimulation = Button(self.window, text='Arreter Simulation', height = 1, width = 20, cursor="hand2", overrelief=GROOVE, command=lambda:self.arreterSimulation())
        ArreterSimulation.grid(row= 0, column=1)

        #Bouton création robot :
        #command=lambda:self.lancerSimulation()
        NouveauRobot = Button(self.window, text='Nouveau Robot', height = 1, width = 20, cursor="hand2", overrelief=GROOVE, command =lambda:self.NouveauRobot())
        NouveauRobot.grid(row= 1, column=0, columnspan=2)

        self.window.mainloop()

    
    

    def ajouterRobot(self, name) -> None:
        self.controlSimulation.creerRobot(name)

    def getRobots(self) -> list:
        self.controlSimulation.getRobots()