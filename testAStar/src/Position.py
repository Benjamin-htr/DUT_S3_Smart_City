class Position:

    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y

    def monter(self):
        self.y += 1

    def descendre(self):
        self.y -= 1

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def setX(self, x : int):
        self.x = x

    def setY(self, y : int):
        self.y = y

    def __eq__(self, other):
        return self.x == other[0] and self.y == other[1]