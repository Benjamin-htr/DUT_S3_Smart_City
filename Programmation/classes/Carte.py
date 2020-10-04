from classes.Cellule import Cellule
from random import *

class Carte :
    """
    construction d'une grille de cellules
    """
    
    def __init__(self):
        """
        construction d'une grille de dimension (nx, ny)
        """
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
    
    def __str__(self):
        """
        retourne une chaine représentant le labyrinthe
        Attention : seuls les murs Est et Sud d'une cellule sont représentés
        """
        laby_lignes = ['+---' * self.ny+'+']
        
        for x in range(self.nx):
            laby_l = ['|']
            for y in range(self.ny):
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

    def creationCartes(self) :
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
        #On détruit des murs aléatoirement
        for i in range(randint(100,110)):
            x = randint(0,self.nx-1)
            y = randint(0,self.ny-1)
            if not (x == self.nx-1 and y == self.ny-1) :
                if i%2 == 0:
                    self.effaceMur((x, y), 'S')
                else:
                    self.effaceMur((x,y), 'E')
    
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