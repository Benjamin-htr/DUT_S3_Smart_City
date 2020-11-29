from classes.Robot import Robot

class Equipe:
    
    def __init__(self, name : str):
        self.name = name
        self.argent = 0
        self.robots = []
        
    def ajouterRobot(self, nom, cellule, carte, simulation) -> Robot:
        robot = Robot(nom,cellule,carte,simulation)
        self.robots.append(robot)
        return robot

    def getRobots(self) -> list:
        return self.robots

    def getArgent(self) -> int:
        return self.argent

    def getName(self) -> str:
        return self.name

    def ajouterArgent(self, argent : int) -> None:
        self.argent += argent