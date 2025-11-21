"""
Classe : OperateurSelection
Module : OperateurSelection.py
Description :
    Représente l'opérateur de sélection des individus dans l'algorithme génétique :
        - Sélection par roulette (proportionnelle)
        - Pour une MINIMISATION ⇒ on inverse les performances
"""

import random

class OperateurSelection:
    """Opérateur de sélection basé sur la roulette proportionnelle."""

    def __init__(self):
        """Constructeur vide : pas de paramètre nécessaire."""
        pass

    def selectionner(self, aPopulation):
        """
        Sélectionne 2 parents dans la population.
        La méthode utilise une roulette proportionnelle :
            - plus la performance est FAIBLE → meilleur l'individu
            - comme minimisation : poids = 1 / (performance + epsilon)
        """

        individus = aPopulation.individus

        # Récupération des performances
        perfs = [ind.performance for ind in individus]

        # Sécurité : éviter la division par zéro
        epsilon = 1e-9

        # MINIMISATION  on transforme la performance en poids inverse
        poids = [(1 / (p + epsilon)) for p in perfs]

        # Sélection proportionnelle
        parent1 = random.choices(individus, weights=poids, k=1)[0]
        parent2 = random.choices(individus, weights=poids, k=1)[0]

        print(f"[Sélection] Parent1 = {parent1}")
        print(f"[Sélection] Parent2 = {parent2}")

        return parent1, parent2



    def __str__(self):
        return "OperateurSelection(roulette)"



#TEST LOCAL


if __name__ == "__main__":
    print("Test de OperateurSelection")

    import random

    # Classe Individu fictive pour test
    class IndividuTest:
        def __init__(self, nom, perf):
            self.nom = nom
            self.performance = perf

        def __str__(self):
            return f"{self.nom}(perf={self.performance})"

    # Population fictive
    class PopTest:
        def __init__(self):
            self.individus = [
                IndividuTest("A", 10),
                IndividuTest("B", 4),
                IndividuTest("C", 1),   # meilleur
                IndividuTest("D", 20)
            ]

    pop = PopTest()
    sel = OperateurSelection()

    parent1, parent2 = sel.selectionner(pop)

    print("\nParents sélectionnés :")
    print(parent1)
    print(parent2)
