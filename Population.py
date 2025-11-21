"""
Classe : Population
Module : Population.py
Description :
    Gère un ensemble d'individus dans l'algorithme génétique :
        - génération initiale
        - évaluation
        - sélection du meilleur
        - remplacement d'individus
"""

from Individu import Individu
from Fenetre import Fenetre
from Performance import Performance
import random






class Population:
    """Représente l'ensemble d'une population d'individus."""

    def __init__(self, aTaille, aFenetres, aFonctionObjectif, aCodage=None):
        """
        Constructeur.
        :param aTaille: nombre d'individus dans la population
        :param aFenetres: liste d'objets Fenetre
        :param aFonctionObjectif: fonction f(x) à minimiser
        :param aCodage: stratégie de codage (optionnelle)
        """
        self.taille = aTaille
        self.fenetres = aFenetres
        self.fonction_objectif = aFonctionObjectif
        self.codage = aCodage

        self.individus = []  # sera rempli dans initialiser()

 

    def initialiser(self):
        """Crée une population initiale aléatoire."""
        self.individus = []

        for _ in range(self.taille):
            ind = Individu(self.fenetres, self.codage)
            self.individus.append(ind)



    def evaluer(self):
        """Évalue tous les individus de la population."""
        for ind in self.individus:
            ind.evaluer(self.fonction_objectif)


    def meilleur(self):
        """Retourne l'individu avec la meilleure performance (minimisation)."""
        return min(self.individus, key=lambda ind: ind.performance)



    def remplacer(self, index, nouvel_individu):
        """
        Remplace un individu de la population à l'index donné.
        """
        self.individus[index] = nouvel_individu



    def __str__(self):
        return "\n".join(str(ind) for ind in self.individus)



# TEST LOCAL 

if __name__ == "__main__":
    print("=== Test de la classe Population ===")



    # Création de 2 fenêtres pour les coordonnées
    fen1 = Fenetre("x1", -5, 5)
    fen2 = Fenetre("x2", -5, 5)
    fenetres = [fen1, fen2]

    # Population de 5 individus
    pop = Population(aTaille=5, aFenetres=fenetres, aFonctionObjectif=Performance.evaluate)

    # Initialisation
    print("\nInitialisation :")
    pop.initialiser()
    print(pop)

    # Évaluation
    print("\nÉvaluation :")
    pop.evaluer()
    print(pop)

    # Meilleur individu
    print("\nMeilleur individu :")
    print(pop.meilleur())
