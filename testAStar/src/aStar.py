from src.Carte import Carte
from src.Cellule import Cellule
from src.Node import Node
import heapq

# code loic

class aStar:
    def __init__(self, carte : Carte):
        self.carte = carte

    def heuristique(self, a : Cellule, b : Cellule):
        (x1, y1) = a.getPosition()
        (x2, y2) = b.getPosition()
        return abs(x1 - x2) + abs(y1 - y2)

    def voisins(self, cel : Cellule): 
        h = self.carte.getHauteur() 
        l = self.carte.getLargeur()
        ls = [] 
        if cel.getPosition()[0]-1 >= 0 and not(cel.murPresent('N')):
            ls.append(self.carte.cellule(cel.getPosition()[0]-1, cel.getPosition()[1]))

        if cel.getPosition()[0]+1 < h  and not(cel.murPresent('S')): 
            ls.append(self.carte.cellule(cel.getPosition()[0]+1, cel.getPosition()[1]))

        if cel.getPosition()[1]-1 >= 0  and not(cel.murPresent('O')): 
            ls.append(self.carte.cellule(cel.getPosition()[0], cel.getPosition()[1]-1))

        if cel.getPosition()[1]+1 < l  and not(cel.murPresent('E')): 
            ls.append(self.carte.cellule(cel.getPosition()[0], cel.getPosition()[1]+1))

        return ls


    def resolution(self, source : Cellule, target : Cellule):
        start = Node(None, source)
        end= Node(None, target)

        #OPEN
        list_O = []
        #CLOSED
        list_F = []
        #On ajoute la node start dans OPEN
        list_O.append(start)

        current = list_O[0]

        #While qui s'arrete si on trouve la node end
        while current.position != end.position and len(list_O) > 0:

            #affecter à current la node avec le F le plus faible
            current = list_O[0]
            ind=0

            for i in range(len(list_O)):
                if list_O[i].f < current.f:
                    current = list_O[i]
                    ind = i
                    
            #On supprime current dans OPEN
            list_O.pop(ind)

            #On ajoute current dans CLOSED
            list_F.append(current)

            #pour chaque voisin dans voisins de la node current
            voisins = self.voisins(current.cellule)

            for voisin in voisins:

                NODE = Node(current, voisin)

                #Si voisin est dans CLOSED
                if NODE in list_F:

                    #passer au prochain voisin
                    continue

                #CALCUL F (g,h)
                NODE.setParamG(current.g+1)
                NODE.setParamH(self.heuristique(NODE.cellule,target))
                NODE.setParamF()
                
                #Si le nouveau chemin vers voisin est plus petit ou que voisin n'est pas dans OPEN
                if NODE not in list_O:
                    list_O.append(NODE)

                else:
                    inf = False
                    ind = 0
                    for j in range(len(list_O)):
                        if NODE.position == list_O[j].position:
                            if NODE.g < list_O[j].g:

                                #On modifie F du voisin
                                list_O[j].setParamG(NODE.g)
                                list_O[j].setParamF()
                                
                                #On modifie parent du voisin à current
                                NODE.parent = current

        #Renvoie du chemin si current = end
        chemin = []
        while current.position != start.position:
                chemin.append(current.position)
                current = current.parent
                
        chemin.append(current.position)
        return chemin[::-1]