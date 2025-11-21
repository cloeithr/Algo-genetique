"""
Classe : OperateurSelection
Module : OperateurSelection.py
Description :
    Opérateur de sélection pour l'algorithme génétique.
    Implémente une sélection par "roulette" adaptée à la MINIMISATION :

        - Plus la performance est FAIBLE plus l'individu a de chance d'être sélectionné.
        - On utilise des poids = 1 / (performance + epsilon).

    La méthode principale selectionner(population) renvoie deux parents.
"""

import random
from Fenetre import Fenetre
from Individu import Individu
from Population import Population

class OperateurSelection:
    """Opérateur de sélection par roulette (pour MINIMISATION)."""

    def __init__(self):
        """Constructeur (pas de paramètre pour l'instant)."""
        pass

    # SELECTION


    def selectionner(self, aPopulation):
        """
        Sélectionne deux parents dans la population à l'aide d'une roulette pondérée.

        :param aPopulation: objet Population, qui contient une liste d'individus
                            avec leur attribut 'performance' déjà évalué.
        :return: (parent1, parent2)
        """

        individus = aPopulation.individus

        # On récupère les performances (f(x)).
        performances = [ind.performance for ind in individus]

        # Sécurité : s'assurer qu'ils sont tous évalués
        if any(p is None for p in performances):
            raise ValueError("Tous les individus doivent avoir une performance avant la sélection.")

        # On veut faire une MINIMISATION :
        # → plus performance est PETITE → plus probabilité est GRANDE.
        epsilon = 1e-9
        poids = [1.0 / (p + epsilon) for p in performances]

        # On choisit deux parents (avec remise possible)
        parent1 = random.choices(individus, weights=poids, k=1)[0]
        parent2 = random.choices(individus, weights=poids, k=1)[0]

        print(f"[Selection] Parent1 : {parent1}")
        print(f"[Selection] Parent2 : {parent2}")

        return parent1, parent2


    # AFFICHAGE


    def __str__(self):
        return "OperateurSelection(roulette minimisation)"


# TEST LOCAL (MAIN)


if __name__ == "__main__":
    print("=== Test LOCAL de OperateurSelection ===")


    # 1) Fenêtres
    fen1 = Fenetre("x1", -5, 5)
    fen2 = Fenetre("x2", -5, 5)
    fenetres = [fen1, fen2]

    # 2) Fonction objectif simple (parabole)
    def f_test(x):
        return sum(v ** 2 for v in x)

    # 3) Création d'une population
    pop = Population(
        aTaille=5,
        aFenetres=fenetres,
        aFonctionObjectif=f_test
    )

    pop.initialiser()
    pop.evaluer()

    print("\nPopulation évaluée :")
    print(pop)

    # 4) Opérateur de sélection
    selec = OperateurSelection()

    print("\nSélection de deux parents :")
    p1, p2 = selec.selectionner(pop)

    print("\nParents retournés :")
    print("Parent 1 :", p1)
    print("Parent 2 :", p2)
