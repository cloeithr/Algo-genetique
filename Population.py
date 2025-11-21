"""
Classe : Population
Module : Population.py
Description :
    Gère un ensemble d'individus dans l'algorithme génétique :
        - génération initiale
        - évaluation
        - sélection du meilleur
        - remplacement
"""

import random
from Individu import Individu
from Fenetre import Fenetre


class Population:
    """Représente une population d'individus."""

    def __init__(self, aTaille, aFenetres, aFonctionObjectif, aCodage=None):
        """
        :param aTaille: nombre total d'individus
        :param aFenetres: liste d'objets Fenetre
        :param aFonctionObjectif: fonction f(x) à optimiser
        :param aCodage: stratégie de codage (optionnelle)
        """
        self.taille = aTaille
        self.fenetres = aFenetres
        self.fonction_objectif = aFonctionObjectif
        self.codage = aCodage

        self.individus = []  # sera rempli par initialiser()


    # CRÉATION POPULATION


    def initialiser(self):
        """Génère une population initiale aléatoire."""
        self.individus = [
            Individu(self.fenetres, self.codage)
            for _ in range(self.taille)
        ]


    # ÉVALUATION


    def evaluer(self):
        """Évalue tous les individus."""
        for ind in self.individus:
            ind.evaluer(self.fonction_objectif)


    # MEILLEUR INDIVIDU


    def meilleur(self):
        """Retourne l'individu avec la plus petite performance."""
        return min(self.individus, key=lambda ind: ind.performance)


    # REMPLACEMENT


    def remplacer(self, index, nouvel_individu):
        """Remplace un individu à l'index donné."""
        self.individus[index] = nouvel_individu


    # AFFICHAGE
    

    def __str__(self):
        return "\n".join(str(ind) for ind in self.individus)


# TEST LOCAL (MAIN)


if __name__ == "__main__":
    print("=== Test de la classe Population ===")

    # 1) Création de fenêtres
    fen1 = Fenetre("x1", -5, 5)
    fen2 = Fenetre("x2", -5, 5)
    fenetres = [fen1, fen2]

    # 2) Fonction objectif simple
    def f_test(x):
        return sum(xi ** 2 for xi in x)

    # 3) Création population
    pop = Population(
        aTaille=5,
        aFenetres=fenetres,
        aFonctionObjectif=f_test
    )

    # 4) Initialisation
    print("\n--- Initialisation ---")
    pop.initialiser()
    print(pop)

    # 5) Évaluation
    print("\n--- Évaluation ---")
    pop.evaluer()
    print(pop)

    # 6) Meilleur individu
    print("\n--- Meilleur individu ---")
    print(pop.meilleur())
