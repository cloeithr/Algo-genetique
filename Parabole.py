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


if __name__ == '__main__':
    from Parabole import Parabole

    # Exemple de coordonnées
    coordonnees = [2, -3, 1]

    # Évaluer la fonction parabole
    fitness = Parabole.evaluate(coordonnees)

    print(f"Coordonnées : {coordonnees}")
    print(f"Valeur de la fonction Parabole : {fitness}")
