# ===============================
#  Fichier : Parabole.py
#  Auteur  : Mouna BENSAID
#  Rôle    : Fonction de performance (benchmark)
#  ===============================

class Parabole:
    """Fonction de performance : f(x1, x2, ..., xn) = somme des xi² (minimisation)."""

    @staticmethod
    def evaluate(coordonnees):
        """Calcule f(x) = Σ xi² pour une liste de coordonnées."""
        return sum(x ** 2 for x in coordonnees)

