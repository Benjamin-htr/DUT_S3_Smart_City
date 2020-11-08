from src.Position import Position

class Cellule:
    
    def __init__(self, x : int, y : int):
        self.position = Position(x,y)
        self.murs = {'N': True, 'S': True, 'E': True, 'O': True}

    def murPresent(self, direction):
        print(self.murs)
        return self.murs[direction]

    def getPosition(self) -> tuple:
        return (self.position.x, self.position.y)

    def __eq__(self, other):
        return self.position == other.position