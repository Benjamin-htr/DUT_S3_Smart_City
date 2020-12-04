from classes.Robot import Robot

class Equipe:
    
    def __init__(self, name : str, letter):
        self.name = name
        self.argent = 0
        self.robots = []
        self.letter = letter
        
    def ajouterRobot(self, nom, color, cellule, carte, simulation) -> Robot:
        robot = Robot(nom,color,cellule,carte,simulation, self)
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