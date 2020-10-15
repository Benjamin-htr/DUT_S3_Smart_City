from classes.Cellule import Cellule
from classes.StationRecharge import StationRecharge
from classes.LieuMission import LieuMission
from random import *
from tkinter import *

class Carte :
    """
    construction d'une grille de cellules
    """
    
    def __init__(self, CanvasCarte):
        """
        construction d'une grille de dimension (nx, ny)
        """

        self.carte = CanvasCarte
        self.nx = 20 #Constante
        self.ny = 20 #Constante
        self.cadrillage = []
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
                if self.cadrillage[x][y].lieu != None:
                    res = ' ' + self.cadrillage[x][y].lieu.getSigne() + ' |'
                    laby_l.append(res)
                elif self.cadrillage[x][y].murs['E']:
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
                    carte.create_line(tabPosXEst[y], tabPosYEst[x],tabPosXEst[y], tabPosYEst[x]+tailleY, fill = 'white')

                if self.cadrillage[x][y].murs['S'] :
                    carte.create_line(tabPosXSud[y], tabPosYSud[x], tabPosXSud[y]+tailleX, tabPosYSud[x], fill = 'white')

        carte.grid(row = 0, column = 2, rowspan=10, padx = 10, pady=25)
        return carte


    def creationCartes(self, nbLieuMission, nbStationRecharge) :
        carte = self.carte
        hauteur = 650
        largeur = 650
        tailleY = hauteur/self.nx
        tailleX = largeur/self.ny
        #On créait une grille rempli de cellule
        for i in range (self.nx) :
            for j in range (self.ny) :
                rand = randint(0, 1)
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
        
        #On efface des murs aléatoirement
        for i in range(220):
            x = randint(0,self.nx-2)
            y = randint(0,self.ny-2)
            if not (x == self.nx-1 and y == self.ny-1) :
                if i%2 == 0:
                    self.effaceMur((x, y), 'S')
                else:
                    self.effaceMur((x,y), 'E')
        #On ajoute des stations de recharge
        for i in range(nbLieuMission):
            x = randint(0,self.nx-1)
            y = randint(0,self.ny-1)
            self.cellule(x, y).setLieu(StationRecharge())
            #carte.create_oval(y*tailleY+10, x*tailleX+10, y*tailleY+22, x*tailleX+22, fill='blue')

        #On ajoute des lieux de mission
        for i in range(nbStationRecharge):
            x = randint(0,self.nx-1)
            y = randint(0,self.ny-1)
            self.cellule(x, y).setLieu(LieuMission())
            #carte.create_oval(y*tailleY+10, x*tailleX+10, y*tailleY+22, x*tailleX+22, fill='red')

        self.cellule(0,0).setLieu(Robot("Jean",))

        

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

    def murPresentCell(self, direction, position) -> bool:
        x = position.getPosition()[0]
        y = position.getPosition()[1]
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