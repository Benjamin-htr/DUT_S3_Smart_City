from classes.Tache import Tache
from classes.Carte import Carte
import random

class Enchere(Tache):
    def __init__(self, carte : Carte, numero) :
        super().__init__(carte, random.randint(300,500))
        self.numero = numero
        self.participants = []
        self.duree = 20 #en seconde

        self.offres = {}

        self.nomGagnant = "Aucun"


    def arriveeParticipant(self, robot) :
        if robot not in self.participants :
            robot.EnchereEnCours = True
            self.participants.append(robot)
        




    def checkEnchere(self, vitesse) :
        if len(self.participants) >= 1 :
            self.JouerEnchere()
            self.duree -= vitesse/1000
            


    def JouerEnchere(self) :
        retour = False
        if len(self.participants) == 1 :
            self.nomGagnant = self.participants[0].nom
            
        if self.duree <= 0 and len(self.participants) == 1 :
            self.nomGagnant = self.participants[0].nom
            self.participants[0].gagnant = True
            retour = True
            self.enchereTerminée()


        elif len(self.participants) >= 2 :
            for robot in self.participants :
                if robot not in self.offres :
                    self.offres[robot] = self.Encherir(robot)

            self.gagnant = min(self.offres, key=self.offres.get)

            self.nomGagnant = self.gagnant.nom
        
        if self.duree <= 0 and len(self.participants) >= 2 :
            self.gagnant.gagnant = True
            self.enchereTerminée()
            
            
    def enchereTerminée(self) :
        for i in range(len(self.participants)) :
            self.participants[0].offre = "Aucune"
            self.participants[0].EnchereEnCours = False
            del self.participants[0]
        del self




    def Encherir(self, robot) -> int :
        offre = random.randint(int(self.recompense*(80/100)), self.recompense)
        print('tic', offre)
        robot.offre = offre
        return offre



        