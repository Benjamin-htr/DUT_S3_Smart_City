from classes.ControlSimulation import ControlSimulation
from tkinter import *
from tkinter import messagebox
import time
import random


class GestionSimulation:
    def __init__(self, nbLieuMission, nbStationRecharge):
        self.nbLieuMission = nbLieuMission
        self.nbStationRecharge = nbStationRecharge


        #creation de la fenêtre :
        self.window = Tk()
        self.EnCours=False
        self.WindowNewRobState=False
        self.WindowSettingState=False
        self.controlSimulation = None
        self.dx=0
        self.dy=5
        self.colors=['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender','lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4']
        self.pointsRobots=[]

        self.diam=70
        self.densite=60
        self.tailleStationRecharge=50
        self.tailleLieuxMission=50
        self.nbCells=20
        self.tailleX=0
        self.tailleY=0

    

        #canvas :
        hauteur = 650
        largeur = 650
        self.CanvasCarte = Canvas(self.window, bg = 'black', height = hauteur, width = largeur)
        
        
        #personnalisation de la fenêtre
        self.window.title('smart_City')
        self.window.geometry('1350x700')
        #self.window.iconbitmap('logo.ico')
        self.window.resizable(height=False, width=False)

    def ajouterRobot(self, name) -> None:
        self.controlSimulation.creerRobot(name)


    def afficherRobots(self) :
        diamDeb=((100-self.diam)/2)/100
        diamFin=(((100-self.diam)/2)+self.diam)/100
        tailleX=self.tailleX
        tailleY=self.tailleY
        robots=self.getRobots()
        print(robots)
        for i in range(0, len(robots)) :
            x = robots[i].cellule.x
            y = robots[i].cellule.y
            color=self.colors[random.randint(0,len(self.colors)-1)]
            self.pointsRobots.append(self.CanvasCarte.create_oval(y*tailleY+(tailleY*diamDeb), x*tailleX+(tailleX*diamDeb), y*tailleY+(tailleY*diamFin), x*tailleX+(tailleX*diamFin), fill=color, outline='white'))
            

    def deplacement(self, typeDeplacement="random") :
        if self.EnCours == False :
            return

        #self.CanvasCarte.update()
        pointsRobots=self.pointsRobots
        robots=self.getRobots()

        for i in range(len(pointsRobots)) :
            currentCell=robots[i].cellule
            #print(robots[i].nom, " :", currentCell)
            if typeDeplacement == "random" :
                deplacement=robots[i].deplacementRandom()
                #print(robots[i].nom, " :", deplacementRandom)

            elif typeDeplacement == "djikstra" :
                self.controlSimulation.simulation.robots[i].setChemin((9,9))
                #print(self.controlSimulation.simulation.robots[i].chemin.chemin)
                deplacement=robots[i].deplacement()

            if deplacement =='N' :
                self.CanvasCarte.move(pointsRobots[i],0,-self.tailleX)
            elif deplacement =='S' :
                self.CanvasCarte.move(pointsRobots[i],0,self.tailleX)
            elif deplacement =='E' :
                self.CanvasCarte.move(pointsRobots[i],self.tailleX,0)
            elif deplacement =='O' :
                self.CanvasCarte.move(pointsRobots[i],-self.tailleX,0)
        self.CanvasCarte.after(1000, lambda : self.deplacement("djikstra"))

    """
    def deplacement(self) :
        self.CanvasCarte.update()
        pointsRobots=self.pointsRobots
        robots=self.getRobots()
        for i in range(len(pointsRobots)) :
            currentCell=robots[i].cellule
            directions=robots[i].deplacement((9, 9))
            #print(directions)
            #print(robots[i].nom, " :", currentCell)
        
            for p in range(len(directions)) :
                j = directions[p]
            #print(robots[i].nom, " :", deplacementRandom)
                if j =='N' :
                    robots[i].cellule = self.controlSimulation.simulation.carte.cellule(robots[i].cellule.x-1, robots[i].cellule.y)
                    self.CanvasCarte.move(pointsRobots[i],0,-32.5)
                elif j =='S' :
                    robots[i].cellule = self.controlSimulation.simulation.carte.cellule(robots[i].cellule.x+1, robots[i].cellule.y)
                    self.CanvasCarte.move(pointsRobots[i],0,32.5)
                elif j =='E' :
                    robots[i].cellule = self.controlSimulation.simulation.carte.cellule(robots[i].cellule.x, robots[i].cellule.y+1)
                    self.CanvasCarte.move(pointsRobots[i],32.5,0)
                elif j =='O' :
                    robots[i].cellule = self.controlSimulation.simulation.carte.cellule(robots[i].cellule.x, robots[i].cellule.y-1)
                    self.CanvasCarte.move(pointsRobots[i],-32.5,0)
                currentCell=robots[i].cellule
                time.sleep(1)
                self.CanvasCarte.update()
        """  


    #boutons interface :
    def lancerSimulation(self):
        if (self.EnCours != True) :
            
            controlSimulation = ControlSimulation()
            sim = controlSimulation.creerSimulation(self.nbLieuMission, self.nbStationRecharge, self.CanvasCarte, self.nbCells, self.densite, self.tailleStationRecharge, self.tailleLieuxMission)
            self.controlSimulation = controlSimulation
            self.tailleX=650/self.controlSimulation.simulation.carte.nx
            self.tailleY=self.tailleX
            self.EnCours=True
            self.afficherRobots()

            # Tests
            #print(self.controlSimulation.simulation.carte.attenantes((2,2)))
            #print(self.controlSimulation.simulation.carte.resolution((1,1), (5,5)))
            #print(self.controlSimulation.simulation.robots[0].deplacement((5,5)))
            #self.controlSimulation.simulation.robots[0].setChemin((9,9))
            #print(self.controlSimulation.simulation.robots[0].deplacement())

            self.deplacement("djikstra")
    
        
    def arreterSimulation(self):
        self.EnCours=False
        self.CanvasCarte.delete("all")
        self.pointsRobots=[]
        
        return None
        
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

            def EnregisterNom(event):
                if messagebox.askyesno("", "Confirmez vous votre choix de nom ?"):
                    print(entree.get())
                    name = entree.get()
                    #ajout du robot :
                    diamDeb=((100-self.diam)/2)/100
                    diamFin=(((100-self.diam)/2)+self.diam)/100
                    tailleX=self.tailleX
                    tailleY=self.tailleY

                    color=self.colors[random.randint(0,len(self.colors)-1)]
                    self.ajouterRobot(name)
                    liste=self.getRobots()
                    rob=liste[len(liste)-1]
                    x = rob.cellule.x
                    y = rob.cellule.y
                    self.pointsRobots.append(self.CanvasCarte.create_oval(y*tailleY+(tailleY*diamDeb), x*tailleX+(tailleX*diamDeb), y*tailleY+(tailleY*diamFin), x*tailleX+(tailleX*diamFin), fill=color, outline='white'))


                    newWindow.destroy()
                    self.WindowNewRobState = False
                    print(self.getRobots())


            def on_closing():
                if messagebox.askokcancel("Quit", "Voulez vous vraiment stopper la création d'un nouveau robot ?"):
                    newWindow.destroy()
                    self.WindowNewRobState = False

            newWindow.protocol("WM_DELETE_WINDOW", on_closing)
            entree.bind("<Return>", EnregisterNom)


    
    
    def ajouterRobot(self, name) -> None:
        self.controlSimulation.creerRobot(name)


    def getRobots(self) -> list:
        return self.controlSimulation.getRobots()

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
            var3.set(self.diam)
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

            def Confirmer() :
                self.diam=int(entree3.get())
                self.densite=int(entree2.get())
                self.tailleStationRecharge=int(entree5.get())
                self.tailleLieuxMission=int(entree4.get())
                self.nbCells=int(entree1.get())
                


            def on_closing():
                newWindow.destroy()
                self.WindowSettingState = False

            newWindow.protocol("WM_DELETE_WINDOW", on_closing)





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

            #Carte :
            self.CanvasCarte.grid(row = 0, column = 2, rowspan=10, padx = 10, pady=25)

            #Bouton settings :
            #icon=PhotoImage(file="classes/icons/settings.png")
            settings = Button(self.window, height = 20, width = 20, cursor="hand2", overrelief=GROOVE, command =lambda:self.OpenSettings())
            settings.grid(row= 0, column=3) 

            self.window.mainloop()