import random

class Fenetre:
    """Représente une fenêtre de recherche [borne_min, borne_max] pour une variable donnée."""
    def __init__(self, anom: str, aborne_min: float, aborne_max: float):
        self.nom = anom
        self.borne_min = aborne_min
        self.borne_max = aborne_max

    def generer_valeur(self) -> float:
        "Retourne une valeur aléatoire dans la fenêtre."
        return random.uniform(self.borne_min, self.borne_max)

    def contient(self, valeur: float) -> bool:
        "Vérifie si une valeur est dans la fenêtre."
        return self.borne_min <= valeur <= self.borne_max

    def __repr__(self):
        "Affichage des bornes"
        return f"Fenetre({self.nom}: [{self.borne_min}, {self.borne_max}])"
