from src.aStar import aStar
from src.Dijkstra import Dijkstra
from src.Carte import Carte

import matplotlib.pyplot as plt
import time

timeAstar = []
#timeDijkstra = []
x = list(range(3,100))

for i in x:
    print(i)
    listeTempsAstar = []
    #listeTempsDijkstra = []

    for temps in range(30):

        carte = Carte(i,i)
        ast = aStar(carte)
        #dis = Dijkstra(carte)

        t0 = time.time()
        ast.resolution(carte.cellule(0,0), carte.cellule(i-1,i-1))
        t1 = time.time()

        listeTempsAstar.append(t1-t0)

        #t0 = time.time()
        #dis.resolution(carte.cellule(0,0), carte.cellule(i-1,i-1))
        #t1 = time.time()

        #listeTempsDijkstra.append(t1 - t0)

    timeAstar.append(sum(listeTempsAstar) / len(listeTempsAstar))
    #timeDijkstra.append(sum(listeTempsDijkstra) / len(listeTempsDijkstra))
    

"""
plt.bar(x,height = timeAstar, width = 0.2)
plt.show()

plt.bar(x,height = timeDijkstra, width = 0.2)
plt.show()
"""

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Comparaison Dijkstra Et A*')
ax1.plot(x, timeAstar)
ax2.plot(x, x)

plt.show(block=True)
