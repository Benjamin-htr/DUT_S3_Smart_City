from src.Carte import Carte
from src.aStar import aStar
from src.Cellule import Cellule

carte = Carte(10,10)
ast = aStar(carte)
print(ast.resolution(Cellule(2,2) , Cellule(9,9)))
