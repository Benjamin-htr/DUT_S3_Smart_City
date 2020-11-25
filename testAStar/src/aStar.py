from src.Carte import Carte
from src.Cellule import Cellule
from src.Node import Node
import heapq

class aStar:
    def __init__(self, carte : Carte):
        self.carte = carte
        print(self.carte)

    def heuristique(self, a : Cellule, b : Cellule):
        (x1, y1) = a.getPosition()
        (x2, y2) = b.getPosition()
        return abs(x1 - x2) + abs(y1 - y2)

    def voisins(self, cel : Cellule): 
        h = self.carte.getHauteur() 
        l = self.carte.getLargeur()
        ls = [] 
        if cel.getPosition()[0]-1 >= 0 and not(cel.murPresent('O')):
            ls.append((cel.getPosition()[0]-1, cel.getPosition()[1])) 

        if cel.getPosition()[0]+1 < h  and not(cel.murPresent('E')): 
            ls.append((cel.getPosition()[0]+1, cel.getPosition()[1]))

        if cel.getPosition()[1]-1 >= 0  and not(cel.murPresent('N')): 
            ls.append((cel.getPosition()[0], cel.getPosition()[1] - 1)) 

        if cel.getPosition()[1]+1 < l  and not(cel.murPresent('S')): 
            ls.append((cel.getPosition()[0], cel.getPosition()[1] + 1))

        return ls

    def resolution(self, source : Cellule, target : Cellule):
        start = Node(None, source)
        end= Node(None, target)

        list_O = []
        list_F = []

        heapq.heappush(list_O,((self.heuristique(source,target)),start))

        while len(list_O) > 0 :
            current=heapq.heappop(list_O)
            current=current[1]
            list_F=[current]+list_F
            if current.position == end.position:
                chemin = []
                while current.position!=start.position:
                    chemin.append(current.position)
                    current = current.parent
                chemin.append(current.position)
                return chemin[::-1]
            vois = self.voisins(current.position)
            children=[]
            for i in vois:
                newNode = Node(current, i)
                children.append(newNode)
            for child in children:
                if child not in list_F:
                    child.g=current.g+1
                    child.h = self.heuristique(child.position,target)
                    child.f = child.g + child.h
                    for openNode in list_O:
                        if child == openNode[1] and child.g < openNode[1].g:
                            openNode[1].g=child.g
                            openNode[1].g=child.f
                            openNode[0]=openNode[1].f
                    if (child.f,child) not in list_O:
                        heapq.heappush(list_O,(child.f,child))
