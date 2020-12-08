from classes.Carte import Carte
from classes.Robot import Robot
from classes.Cellule import Cellule
from classes.Tache import Tache
from classes.Enchere import Enchere
from classes.Equipe import Equipe
from tkinter import *
import random

class Simulation:
    def __init__(self, CanvasCarte):
        self.CanvasCarte = CanvasCarte
        self.robots = []
        self.taches = []
        self.equipes = []
        self.carte = None

        #lettres possibles pour les équipes :
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        #noms possibles pour les Equipes :
        self.EquipesNames=['Chicago Bulls', 'Los pollos hermanos', 'Les Dingus', 'La Nicoteam', 'TEAM TOURIST', 'Les Tontons Plaqueurs', 'Touch’ensemble', 'Les 100 Mêlées', 'Les déter-gens', 'San Antonio Spurs', 'Les Céréales Killers']

        #noms possibles pour les robots :
        self.RobotsNames=['Predator', 'Terminator', '007', 'Francis Lalanne', 'John Doe', 'Ca Caillus', 'Pol', 'Megaman', 'Bibendum chamallow', 'Jack Ouille', 'Terre I', 'Bonjour', 'Aurevoir', 'Vald', 'Miranda', 'Jacqueline', 'Severine', 'iron Max', 'Doraemon', 'Awesom-O', 'HK-47', 'ED-209', 'Bishop', 'H.E.L.P.eR', 'Clank', 'Daft Punk', 'Johnny 5', 'The Robot', 'Mr. Roboto', 'Mindstorms', 'Robbie', 'Astro Boy', 'The Iron Giant', 'Optimus Prime', 'Roomba', 'DJ Roomba', 'Rosie', 'K-9', 'Metropolis', 'ASIMO', 'GLaDOS', 'HAL 9000', 'Sojourner', 'Data', 'R2D2', 'Bender Bending', 'Wall-E', 'C3-Po']

        #couleurs possibles pour les robots :
        self.colors=['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender','lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4']

        self.numeroEnchere = 1

    def generationCarte(self, nbCells, densite, tailleStationRecharge, tailleLieuxMission):
        carte = Carte(self.CanvasCarte, nbCells)
        carte.creationCartes(densite)
        carte.dessinerCarte()
        self.carte = carte

        carte.dessinerStationsRecharges(tailleStationRecharge)

        #on génère les equipes :
        self.genererEquipes(2)

        #on génère les tâches :
        self.genererTaches()
        

        #self.afficher(carte)

    def genererEquipes(self, nbEquipes = 2) :
        nbRobots=self.carte.nx / 4

        for i in range (nbEquipes) :
            name = self.EquipesNames[random.randint(0,len(self.EquipesNames)-1)]
            self.EquipesNames.remove(name)
            letter = self.letters[0]
            self.letters.remove(letter)

            self.equipes.append(Equipe(name, letter))
            #for j in range(int(2)) :
            for j in range(int(nbRobots/nbEquipes)) :
                robotName = self.RobotsNames[random.randint(0,len(self.RobotsNames)-1)]
                color = self.colors[random.randint(0,len(self.colors)-1)]
                robot = self.ajouterRobot(robotName, color, self.equipes[i])

                



    def afficher(self, carte):
        print(carte)


    def ajouterRobot(self, name, color, equipe : Equipe) -> Robot :
        robot = equipe.ajouterRobot(name, color, self.carte.getCelluleRandom(), self.carte, self)
        self.robots.append(robot)
        return robot
        
        
    def getRobots(self) -> list:
        return self.robots

    def getTaches(self) -> list:
        return self.taches

    def getEncheres(self) -> list :
        liste = []
        for tache in self.taches :
            if type(tache) == Enchere :
                liste.append(tache)
        return liste


    def estPresent(self, cellule):
        estPresent = False
        for i in range(len(self.taches)):
            if (self.taches[i].getCelluleTache().getPosition() == cellule.getPosition()):
                estPresent = True
                break
        return estPresent
    
    def ajouterEnchere(self) -> None :
        enchere = Enchere(self.carte, self.numeroEnchere, self)
        self.taches.append(enchere)
        self.numeroEnchere += 1

    def ajouterTache(self) -> None:
        tache = Tache(self.carte)
        self.taches.append(tache)

    def genererTaches(self) :
        nbTachesTotal = len(self.robots*2)
        nbTachesSimples = round(nbTachesTotal*(40/100))
        
        nbTachesEncheres = round(nbTachesTotal*(60/100))
        

        
        for i in range(nbTachesSimples) :
            self.ajouterTache()
        for i in range(nbTachesEncheres) :
            self.ajouterEnchere()

        print("Nombre de taches simples au début :", nbTachesSimples)
        print("Nombre de taches à Enchère au début :", nbTachesEncheres)

        

    def launchStations(self, tailleX) :
        stations = self.carte.getStationRecharge()
        for station in stations :
            station.Recharger(tailleX)

    def checkEnchere(self, vitesse) :
        encheres = self.getEncheres()
        for enchere in encheres :
            enchere.checkEnchere(vitesse)
    
    def getEquipeGagnant(self) -> str:
        equipeGagnante = self.equipes[0]
        for equipe in self.equipes:
            if equipe.getArgent() >  equipeGagnante.getArgent():
                equipeGagnante = equipe
        return equipeGagnante

    def egalité(self) -> bool:
        egalité = True
        score = self.equipes[0].getArgent()
        for equipe in self.equipes:
            if equipe.getArgent() != score:
                egalité = False
        return egalité
            
