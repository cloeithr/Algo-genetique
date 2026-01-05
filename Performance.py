"""
Classe : Performance
Module : Performance.py
Description :
    Classe contenant la fonction objectif de l'algorithme génétique.
    Cette classe NE DOIT PAS modifier l'individu.
    Son rôle : retourner la valeur f(x) = Σ xi² (parabole).
"""

import math

class Performance:
    """Fonction objectif : parabole multi-dimensionnelle."""

    @staticmethod
    def evaluate(coordonnees):
        """Calcule f(x) = somme des xi²."""
        return sum(x ** 2 for x in coordonnees)
    
    # Première fonction dans benchmarks
    @staticmethod
    def schaffer(coordonnees):
        """Fonction de test Schaffer : f(x,y) = -x*sin(sqrt(|x|)) - y*sin(sqrt(|y|))"""
        x, y = coordonnees
        return -x * math.sin(math.sqrt(abs(x))) - y * math.sin(math.sqrt(abs(y)))



# TEST LOCAL

if __name__ == "__main__":
    print("=== Test de la classe Performance ===")

    coords = [2, -3, 1]
    print("Coordonnées :", coords)
    print("f(x) =", Performance.evaluate(coords))
