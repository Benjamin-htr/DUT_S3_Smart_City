class Marchandise:
    def __init__(self, nom : str, poids : float):
        self.nom = nom
        self.poids = poids

    def getNom(self) -> str:
        return self.nom

    def getPoids(self) -> float:
        return self.poids