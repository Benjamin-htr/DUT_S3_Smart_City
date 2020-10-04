class Cellule:
    """
    définition d'une cellule
    """
    
    def __init__(self,x, y, lieu = None):
        """
        créer une cellule positionnée en (x=ligne, y=colonne)
        """
        if x < 0 or y < 0:
            raise("Les coordonnées de la cellule doivent etre positives.")
        self.x = x
        self.y = y
        self.lieu = lieu
        #les murs sont dans l'ordre : N, S, E, O. 
        #la valeur est à True si un mur est présent, False sinon
        self.murs = {'N': True, 'S': True, 'E': True, 'O': True}
    
    def setLieu(self, lieu):
        self.lieu = lieu

    def __str__(self):
        if self.lieu == None:
            res = "aaa"
        else:
            res = self.lieu.getSigne()
        return res
