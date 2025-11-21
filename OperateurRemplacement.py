"""
Classe : OperateurRemplacement
Module : OperateurRemplacement.py
Description :
    Opérateur de remplacement "2 parmi 4".
    Parmi : (père, mère, enfant1, enfant2)
    on sélectionne les 2 meilleurs individus pour rester dans la population.

    Objectif :
        - préserver la diversité
        - éviter le remplacement systématique
"""

import random


class OperateurRemplacement:
    """Stratégie de remplacement 2 parmi 4."""

    def __init__(self, aBruit: float = 0.01):
        """
        Constructeur.
        :param aBruit: petite perturbation aléatoire ajoutée aux performances
                       pour éviter un déterminisme total.
        """
        self.bruit = aBruit

    #  MÉTHODE PRINCIPALE

    def remplacer(self, population, p1, p2, e1, e2):
        """
        Remplace deux individus dans la population.

        Stratégie :
            1. Évaluer les 4 candidats 
            2. Ajouter un bruit minime aux performances
            3. Trier du meilleur au moins bon
            4. Conserver les 2 meilleurs
            5. Remplacer P1 et P2 dans la population
        """

        # Étape 1 : ensemble des candidats
        candidats = [p1, p2, e1, e2]

        # Étape 2 : bruit pour casser le déterminisme
        def score(ind):
            return ind.performance + random.uniform(-self.bruit, self.bruit)

        # Étape 3 : tri (minimisation)
        candidats_tries = sorted(candidats, key=score)

        meilleurs = candidats_tries[:2]  # deux meilleurs

        # Étape 4 : remplacement dans la population
        # on remplace P1 et P2, pas les enfants
        index1 = population.individus.index(p1)
        index2 = population.individus.index(p2)

        population.individus[index1] = meilleurs[0]
        population.individus[index2] = meilleurs[1]

        print(f"[Remplacement] Conserver : {meilleurs[0]} et {meilleurs[1]}")

    # AFFICHAGE
 
    def __str__(self):
        return f"OperateurRemplacement(2-parmi-4, bruit={self.bruit})"


# TEST LOCAL


if __name__ == "__main__":
    print("=== Test local OperateurRemplacement ===")

    class IndividuTest:
        def __init__(self, perf):
            self.performance = perf
        def __str__(self):
            return f"I({self.performance})"

    # Population fictive
    class PopulationTest:
        def __init__(self):
            self.individus = []

    # Création
    pop = PopulationTest()
    p1 = IndividuTest(10)
    p2 = IndividuTest(20)
    e1 = IndividuTest(5)
    e2 = IndividuTest(12)

    pop.individus = [p1, p2]

    op = OperateurRemplacement()
    op.remplacer(pop, p1, p2, e1, e2)

    print("Nouvelle population :", pop.individus)
