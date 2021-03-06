from classes.Cellule import Cellule
from classes.StationRecharge import StationRecharge
from classes.LieuMission import LieuMission
import random
from tkinter import *

class Carte :
    """
    construction d'une grille de cellules
    """
    
    def __init__(self, CanvasCarte, nbCells):
        """
        construction d'une grille de dimension (nx, ny)
        """

        self.carte = CanvasCarte
        self.nx = nbCells
        self.ny = self.nx
        self.cadrillage = []
        self.lieu = []
        for i in range(self.nx):
            GrilleLigne=[]
            for j in range(self.ny):
                cel = Cellule(i,j)
                GrilleLigne.append(cel)
            self.cadrillage.append(GrilleLigne)
        
    def cellule(self, x, y):
        """
        retourne la cellule de la grille de position (x=ligne, y=colonne)
        """
        
        return self.cadrillage[x][y]
    
    #Permet d'afficher la carte
    def __str__(self):
        """
        retourne une chaine représentant le labyrinthe
        Attention : seuls les murs Est et Sud d'une cellule sont représentés
        """
        laby_lignes = ['+---' * self.ny+'+']
        for x in range(self.nx):
            laby_l = ['|']
            for y in range(self.ny):
                #Si la cellule a un lieu alors on affiche son signe dans la cellule
                #if self.cadrillage[x][y].lieu != None:
                #    res = ' ' + self.cadrillage[x][y].lieu.getSigne() + ' |'
                #    laby_l.append(res)
                if self.cadrillage[x][y].murs['E']:
                    laby_l.append('   |')
                else:
                    laby_l.append('    ')
            laby_lignes.append(''.join(laby_l))
            laby_l = ['+']
            for y in range(self.ny):
                if self.cadrillage[x][y].murs['S']:
                    laby_l.append('---+')
                else:
                    laby_l.append('   +')
            laby_lignes.append(''.join(laby_l))
        return '\n'.join(laby_lignes)

    def dessinerCarte(self) :
        carte = self.carte

        hauteur = 650
        largeur = 650
        # taille des cellules :
        tailleY = hauteur/self.nx
        tailleX = largeur/self.ny

        tabPosXEst = []
        tabPosYEst = []
        tabPosXSud = []
        tabPosYSud = []
        for a in range(self.nx) :
            tabPosYEst.append((hauteur/self.nx)*a)
            tabPosXSud.append((hauteur/self.nx)*a)
            
        for b in range(1, self.ny+1) :
            tabPosXEst.append((largeur/self.ny)*b)
            tabPosYSud.append((largeur/self.ny)*b)


        for x in range(self.nx) :
            for y in range(self.ny) :
                
                if self.cadrillage[x][y].murs['E'] :
                    carte.create_line(tabPosXEst[y], tabPosYEst[x],tabPosXEst[y], tabPosYEst[x]+tailleY, fill = 'white', tags='form')

                if self.cadrillage[x][y].murs['S'] :
                    carte.create_line(tabPosXSud[y], tabPosYSud[x], tabPosXSud[y]+tailleX, tabPosYSud[x], fill = 'white', tags='form')



        #carte.grid(row = 0, column = 0, rowspan=10, padx = 10, pady=25)
        return carte

    def dessinerStationsRecharges(self, tailleStationRecharge) :
        hauteur = 650
        largeur = 650
        # taille des cellules :
        tailleY = hauteur/self.nx
        tailleX = largeur/self.ny

        diam=tailleStationRecharge
        diamDeb=((100-diam)/2)/100
        diamFin=(((100-diam)/2)+diam)/100
        StationsRecharges = self.getStationRecharge()
        

        for StationRecharge in (StationsRecharges) :
            x = StationRecharge.getCellule().getPosition()[0]
            y = StationRecharge.getCellule().getPosition()[1]
            self.carte.create_rectangle(y*tailleY+(tailleY*diamDeb), x*tailleX+(tailleX*diamDeb), y*tailleY+(tailleY*diamFin), x*tailleX+(tailleX*diamFin), fill='blue', tags='form')


    def creationCartes(self, densite) :
        carte = self.carte
        hauteur = 650
        largeur = 650
        tailleY = hauteur/self.nx
        tailleX = largeur/self.ny
        #On créait une grille rempli de cellule
        for i in range (self.nx) :
            for j in range (self.ny) :
                rand = random.randint(0, 1)
                cell=self.cellule(i, j)
                if not (i == self.nx-1 and j == self.ny-1) :
                    if j == self.ny-1 :
                        self.effaceMur((i, j), 'S')
                    elif i == self.nx-1 :
                        self.effaceMur((i, j), 'E')
                    else :
                        if rand == 0 :
                            self.effaceMur((i, j), 'S')
                        else :
                            self.effaceMur((i, j), 'E')
        percent=100-densite
        #On efface des murs aléatoirement
        for i in range(round((self.nx*self.nx)*(percent/100))):
            x = random.randint(0,self.nx-2)
            y = random.randint(0,self.ny-2)
            if not (x == self.nx-1 and y == self.ny-1) :
                if i%2 == 0:
                    self.effaceMur((x, y), 'S')
                else:
                    self.effaceMur((x,y), 'E')

        #on ajoute les stations de recharges :
        for i in range(int(self.nx/2)):
            self.ajouterStationRecharge()
    

        #diam=tailleStationRecharge
        #diamDeb=((100-diam)/2)/100
        #diamFin=(((100-diam)/2)+diam)/100
        #On ajoute des stations de recharge
        #for i in range(nbLieuMission):
        #    x = random.randint(0,self.nx-1)
        #    y = random.randint(0,self.ny-1)
        #    self.cellule(x, y).setLieu(StationRecharge())
        #    carte.create_oval(y*tailleY+(tailleY*diamDeb), x*tailleX+(tailleX*diamDeb), y*tailleY+(tailleY*diamFin), x*tailleX+(tailleX*diamFin), fill='blue', tags='form')

        #diam=tailleLieuxMission
        #diamDeb=((100-diam)/2)/100
        #diamFin=(((100-diam)/2)+diam)/100
        #On ajoute des lieux de mission
        #for i in range(nbStationRecharge):
        #    x = random.randint(0,self.nx-1)
        #    y = random.randint(0,self.ny-1)
        #    lieuMission = LieuMission()
        #    carte.create_oval(y*tailleY+(tailleY*diamDeb), x*tailleX+(tailleX*diamDeb), y*tailleY+(tailleY*diamFin), x*tailleX+(tailleX*diamFin), fill='red', tags='form')

    def getCelluleRandom(self):
        return self.cellule(random.randint(0,self.nx - 1), random.randint(0, self.ny - 1))

    def estPresent(self, cellule):
        estPresent = False
        for i in range(len(self.lieu)):
            if (self.lieu[i].getCellule().getPosition() == cellule.getPosition()):
                estPresent = True
                break
        return estPresent

    
    def ajouterLieuMission(self, stock = []):
        cel = self.getCelluleRandom()
        while self.estPresent(cel):
            cel = self.getCelluleRandom()
        lieuMission = LieuMission(cel, stock)
        self.lieu.append(lieuMission)
        return lieuMission

    def ajouterStationRecharge(self):
        cel = self.getCelluleRandom()
        while self.estPresent(cel):
            cel = self.getCelluleRandom()
        self.lieu.append(StationRecharge(cel))

    #Efface un mur d'une cellule
    def effaceMur (self, coord, orientation) :
        cell=self.cellule(coord[0], coord[1])
        cell.murs[orientation] = False

        if orientation == 'N' and coord[0] != 0 :
            cell2=self.cellule(coord[0]-1, coord[1])
            cell2.murs['S'] = False
            
        elif orientation == 'S' and coord[0] != self.nx-1 :
            cell2=self.cellule(coord[0]+1, coord[1])
            cell2.murs['N'] = False
            
        elif orientation == 'O' and coord[1] != 0:
            cell2=self.cellule(coord[0], coord[1]-1)
            cell2.murs['E'] = False
            
        elif orientation == 'E' and coord[1] != self.ny-1 :
            cell2=self.cellule(coord[0], coord[1]+1)
            cell2.murs['O'] = False

    def murPresentCell(self, direction, cellule) -> bool:
        x = cellule.getPosition()[0]
        y = cellule.getPosition()[1]
        cell = self.cellule(x, y)

        murPresent = True
        if direction == 'N' and not(cell.murPresent(direction)) and not(self.cellule(x-1, y).murPresent('S')) and x != 0:
            murPresent = False
        elif direction == 'S' and not(cell.murPresent(direction)) and not(self.cellule(x+1, y).murPresent('N')) and x != self.nx - 1:
            murPresent = False
        elif direction == 'E' and not(cell.murPresent(direction)) and not(self.cellule(x, y+1).murPresent('O')) and y != self.ny - 1:
            murPresent = False
        elif direction == 'O' and not(cell.murPresent(direction)) and not(self.cellule(x, y-1).murPresent('E')) and y != 0:
            murPresent = False
        return murPresent


    def distance(self, positionDep : tuple) -> list:
        dist = []
        for i in range(self.nx):
            dist.append([])
            for j in range(self.ny):
                dist[i].append(-1)

        File = list()
        dist[positionDep[0]][positionDep[1]] = 0
        File.append(positionDep)

        while len(File) != 0:
            k = File[0]
            liste = self.attenantes(k)
            for i in range(len(liste)):
                if dist[liste[i][0]][liste[i][1]] == -1:
                    File.append(liste[i])
                    dist[liste[i][0]][liste[i][1]] = dist[k[0]][k[1]]+1

            del File[0]

        return dist

    def getDistance(self, positionDep : tuple, positionArr) -> int:
        dist = []
        for i in range(self.nx):
            dist.append([])
            for j in range(self.ny):
                dist[i].append(-1)

        File = []
        dist[positionDep[0]][positionDep[1]] = 0
        File.append(positionDep)

        while dist[positionArr[0]][positionArr[1]] == -1:
            k = File[0]
            liste = self.attenantes(k)
            for i in range(len(liste)):
                if dist[liste[i][0]][liste[i][1]] == -1:
                    File.append(liste[i])
                    dist[liste[i][0]][liste[i][1]] = dist[k[0]][k[1]]+1

            del File[0]
        return dist[positionArr[0]][positionArr[1]]


    def attenantes(self, coord : tuple) -> list:
        cell = self.cellule(coord[0], coord[1])
        liste = []
        direction = ['N', 'S', 'E', 'O']

        for direc in direction:
            if direc == 'N' and coord[0] != 0 and cell.murPresent('N') == False:
                liste.append((cell.getPosition()[0] - 1 , cell.getPosition()[1]))
            if direc == 'S' and coord[0] != self.nx - 1 and cell.murPresent('S') == False:
                liste.append((cell.getPosition()[0] + 1 , cell.getPosition()[1]))
            if direc == 'E' and coord[1] != self.ny - 1 and cell.murPresent('E') == False:
                liste.append((cell.getPosition()[0] , cell.getPosition()[1] + 1))
            if direc == 'O' and coord[1] != 0 and cell.murPresent('O') == False:
                liste.append((cell.getPosition()[0] , cell.getPosition()[1] - 1))

        return liste

    def resolution(self, positionDep : tuple, positionArr : tuple) -> list:
        D = self.distance(positionDep)
        x = self.nx
        y = self.ny
        a = positionArr[0]
        b = positionArr[1]
        rep = [(a,b)]
        while (positionDep[0],positionDep[1]) != (a,b):
            att = self.attenantes((a,b))
            for i in att:
                if D[a][b]-1 == D[i[0]][i[1]] and (0,0) != (a,b):
                    a = i[0]
                    b = i[1]
                    rep = [(a,b)] + rep
        return rep

    def getLieuMission(self) -> list:
        lesLieuxMissions = []
        for lieu in self.lieu:
            if isinstance(lieu, LieuMission):
                lesLieuxMissions.append(lieu)
        return lesLieuxMissions

    def getStationRecharge(self) -> list:
        lesStationsRecharges = []
        for lieu in self.lieu:
            if isinstance(lieu, StationRecharge):
                lesStationsRecharges.append(lieu)
        return lesStationsRecharges
