import random

class Fenetre:
    def __init__(self, nom: str, borne_min: float, borne_max: float):
        self.nom = nom
        self.borne_min = borne_min
        self.borne_max = borne_max

    def generer_valeur(self) -> float:
        "Retourne une valeur aléatoire dans la fenêtre."
        return random.uniform(self.borne_min, self.borne_max)

    def contient(self, valeur: float) -> bool:
        "Vérifie si une valeur est dans la fenêtre."
        return self.borne_min <= valeur <= self.borne_max

    def __repr__(self):
        "Affichage des bornes"
        return f"Fenetre({self.nom}: [{self.borne_min}, {self.borne_max}])"
