"""
Classe : Fenetre
Module : Fenetre.py
Description :
    Représente une fenêtre de recherche [borne_min, borne_max]
    pour une variable réelle d'un individu.
"""

import random


class Fenetre:
    """Représente une fenêtre de recherche d'une coordonnée."""

    def __init__(self, aNom: str, aBorneMin: float, aBorneMax: float):
        """
        Constructeur.
        :param aNom: nom de la variable (ex : "x1")
        :param aBorneMin: borne inférieure de la fenêtre
        :param aBorneMax: borne supérieure de la fenêtre
        """
        self.nom = aNom
        self.borne_min = aBorneMin
        self.borne_max = aBorneMax

    def generer_valeur(self) -> float:
        """Retourne une valeur aléatoire dans la fenêtre."""
        return random.uniform(self.borne_min, self.borne_max)

    def contient(self, valeur: float) -> bool:
        """Vérifie si une valeur est dans la fenêtre."""
        return self.borne_min <= valeur <= self.borne_max

    def __str__(self):
        """Affichage lisible de la fenêtre."""
        return f"{self.nom} ∈ [{self.borne_min}, {self.borne_max}]"

    def __repr__(self):
        return f"Fenetre({self.nom}, {self.borne_min}, {self.borne_max})"


# TEST LOCAL 

if __name__ == "__main__":
    print("Test de la classe Fenetre ")

    f = Fenetre("x1", -10, 10)
    print("Fenêtre :", f)

    val = f.generer_valeur()
    print("Valeur générée :", val)

    print("Contient cette valeur ? ", f.contient(val))
    print("Contient 999 ? ", f.contient(999))
