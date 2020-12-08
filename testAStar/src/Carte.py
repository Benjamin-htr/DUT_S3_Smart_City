from src.Cellule import Cellule
import random

class Carte:

    def __init__(self, nx : int, ny : int):
        self.nx = nx
        self.ny = ny

        self.carte = []
        for i in range(self.nx):
            grilleLigne=[]
            for j in range(self.ny):
                cel = Cellule(i,j)
                grilleLigne.append(cel)
            self.carte.append(grilleLigne)
        self.creationCartes()

    def __str__(self):
        laby_lignes = ['+---' * self.ny+'+']
        
        for x in range(self.nx):
            laby_l = ['|']
            for y in range(self.ny):
                #Si la cellule a un lieu alors on affiche son signe dans la cellule
                if self.carte[x][y].murs['E']:
                    laby_l.append('   |')
                else:
                    laby_l.append('    ')
            laby_lignes.append(''.join(laby_l))
            laby_l = ['+']
            for y in range(self.ny):
                if self.carte[x][y].murs['S']:
                    laby_l.append('---+')
                else:
                    laby_l.append('   +')
            laby_lignes.append(''.join(laby_l))
        return '\n'.join(laby_lignes)

    def creationCartes(self) :

        for i in range (self.nx) :
            for j in range (self.ny) :
                rand = random.randint(0, 1)
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
        for i in range(int(self.nx * self.ny / 1.5)) :
            x = random.randint(0,self.nx-2)
            y = random.randint(0,self.ny-2)
            if not (x == self.nx-1 and y == self.ny-1) :
                if i%2 == 0:
                    self.effaceMur((x, y), 'S')
                else:
                    self.effaceMur((x,y), 'E')


    def effaceMur(self, coord, orientation) :
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


    def cellule(self, x, y):
        return self.carte[x][y]

    def getHauteur(self):
        return self.ny

    def getLargeur(self):
        return self.nx