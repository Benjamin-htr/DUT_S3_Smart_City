from classes.Lieu import Lieu

class StationRecharge(Lieu):
    def __init__(self, cellule):
        super().__init__(cellule)
        self.garage = []
        self.tauxDeRecharge = 10

    def arriveeRobot(self, robot) :
        self.garage.append(robot)

    def departRobot(self, robot) :
        self.garage.remove(robot)

    def Recharger(self, tailleX) :
        if (len(self.garage) > 0) :
            for robot in (self.garage) :
                if robot.batterie < 90 :
                    robot.batterie += self.tauxDeRecharge
                elif robot.batterie < 100 :
                    robot.batterie = 100
            
                        
            

    
