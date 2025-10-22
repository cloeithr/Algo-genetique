# ===============================
#  Fichier : test_bouchon_performance.py
#  Auteur  : Mouna BENSAID
#  Objectif : Tester les classes Parabole et Performance avec un individu fictif
#  ===============================

from Parabole import Parabole
from Performance import Performance


# ==== Classe bouchon pour simuler un Individu ====
class IndividuBouchon:
    """Simule un individu avec une méthode decode()."""
    def __init__(self, coordonnees):
        self.coordonnees = coordonnees
        self.performance = None

    def decode(self):
        """Retourne les coordonnées simulées."""
        return self.coordonnees


# ==== Tests ====
if __name__ == "__main__":
    print("=== TEST BOUCHON : PARABOLE ET PERFORMANCE ===")

    # Création de quelques individus fictifs
    ind1 = IndividuBouchon([0, 0])
    ind2 = IndividuBouchon([1, 2])
    ind3 = IndividuBouchon([-3, 4])

    # Test direct de la fonction Parabole
    print("\n--- Test Parabole ---")
    print("f(0,0) =", Parabole.evaluate([0, 0]))
    print("f(1,2) =", Parabole.evaluate([1, 2]))
    print("f(-3,4) =", Parabole.evaluate([-3, 4]))

    # Test de la classe Performance
    print("\n--- Test Performance ---")
    for ind in [ind1, ind2, ind3]:
        perf = Performance.evaluer(ind)
        print(f"Coordonnées : {ind.coordonnees} -> Performance = {perf}")
