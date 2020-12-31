class Cellule:
    """
    définition d'une cellule
    """
    
    def __init__(self,x, y):
        """
        créer une cellule positionnée en (x=ligne, y=colonne)
        """
        if x < 0 or y < 0:
            raise("Les coordonnées de la cellule doivent etre positives.")
        self.x = x
        self.y = y
        #les murs sont dans l'ordre : N, S, E, O. 
        #la valeur est à True si un mur est présent, False sinon
        self.murs = {'N': True, 'S': True, 'E': True, 'O': True}

#Pour A star :
        self.coutCase = None
        self.coutHeuristique = None
        self.coutTotal = None
        self.parent = None
        
#end A Star
    

    def __str__(self):
        res = "x "+str(self.x)+" y: "+str(self.y)
        return res

    def murPresent(self, direction):
        return self.murs[direction]

    def getPosition(self) -> tuple:
        return (self.x, self.y)

#Pour A Star :
    def setHeuristique(self, cell) -> None :
         self.heuristique = (((cell.x-self.x)**2) + ((cell.y - self.y)**2)) ** 0.5

    def setParent(self, cell) -> None :
        self.parent = (cell.x, cell.y)


#end A Star
