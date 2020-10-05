from tkinter import *

#creation de la fenêtre :
window = Tk()

#personnalisation de la fenêtre
window.title('smart_City')
window.geometry('1350x700')
window.resizable(height=False, width=False)
window.iconbitmap("logo.ico")



#creation d'n canvas pour la carte:
hauteur = 650
largeur = 650
carte = Canvas(window, bg = 'black', height = hauteur, width = largeur)

"""
def echelle(carte : Canvas, nbEtage : int, hauteur : int, largeur : int, position : tuple) :
    Espace = hauteur/nbEtage
    y = 0
    carte.create_line(position[0], position[1], position[0]+largeur, position[1], fill = 'white')


    for i in range (nbEtage-1) :
        y += Espace
        carte.create_line(position[0], position[1]+y, position[0]+largeur, position[1]+y, fill = 'white')

position=(5,5)
echelle(carte, 50, 500, 50, position)
"""

#formation de la carte :
class UneCellule:
    """
    définition d'une cellule
    """
    
    def __init__(self,x, y):
        """
        créer une cellule positionnée en (x=ligne, y=colonne)
        """
        
        self.x = x
        self.y = y
        #les murs sont dans l'ordre : N, S, E, O. 
        #la valeur est à True si un mur est présent, False sinon
        self.murs = {'N': True, 'S': True, 'E': True, 'O': True}


########      
class Grille :
    """
    construction d'une grille de cellules
    """
    
    def __init__(self, nx, ny):
        """
        construction d'une grille de dimension (nx, ny)
        """
        self.hauteur = 650
        self.largeur = 650
        self.carte = Canvas(window, bg = 'black', height = hauteur, width = largeur)
        
        self.nx = nx
        self.ny = ny
        self.cadrillage = []
        for i in range(nx):
            GrilleLigne=[]
            for j in range(ny):
                GrilleLigne.append(UneCellule(i,j))
            self.cadrillage.append(GrilleLigne)
        
        
    def cellule(self, x, y):
        """
        retourne la cellule de la grille de position (x=ligne, y=colonne)
        """
        
        return self.cadrillage[x][y]
    
    def creationCarte(self):
        carte = self.carte
        # le contour du labyrinthe :
        x0 = 5
        y0 = 5
        #rectangle = carte.create_rectangle(x0, y0, largeur-2, hauteur-2, width = 5, outline = 'white')

        # taille des cellules :
        tailleY = self.hauteur/self.nx
        print(tailleY)
        tailleX = self.hauteur/self.ny
        print(tailleX)

        tabPosXEst = []
        tabPosYEst = []
        tabPosXSud = []
        tabPosYSud = []
        for a in range(self.nx) :
            tabPosYEst.append((self.hauteur/self.nx)*a)
            tabPosXSud.append((self.hauteur/self.nx)*a)
            
        for b in range(1, self.ny+1) :
            tabPosXEst.append((self.largeur/self.ny)*b)
            tabPosYSud.append((self.largeur/self.ny)*b)

        for x in range(self.nx) :
            for y in range(self.ny) :
                
                if self.cadrillage[x][y].murs['E'] :
                    bord = carte.create_line(tabPosXEst[y], tabPosYEst[x],tabPosXEst[y], tabPosYEst[x]+tailleY, fill = 'red')

                if self.cadrillage[x][y].murs['S'] :
                    bord = carte.create_line(tabPosXSud[y], tabPosYSud[x], tabPosXSud[y]+tailleX, tabPosYSud[x], fill = 'white')

        carte.pack(side = RIGHT, padx = 10)
        return None


carte = Grille(20, 20)
coord = (5, 7)
cell =carte.cellule(coord[0], coord[1])
cell.murs['S']=False
carte.creationCarte()


#carte.create_rectangle(x0, y0, largeur-2, hauteur-2, width = 5, outline = 'white')
#carte.create_line(50, 50, x0+5, 50, fill = 'white')



#affichage
window.mainloop()
