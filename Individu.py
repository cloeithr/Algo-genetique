"""
Classe : Individu
Module : Individu.py
Description :
    Représente un individu dans l'algorithme génétique.
    Il contient :
        - une liste de Coordonnee
        - une stratégie de codage (optionnelle)
        - un génome (optionnel)
        - une performance
"""

from Coordonnee import Coordonnee
from Fenetre import Fenetre
import random


class Individu:

    def __init__(self, aFenetres, aCodage=None):
        """
        :param aFenetres: liste d'objets Fenetre
        :param aCodage: stratégie de codage (optionnelle)
        """
        self.fenetres = aFenetres
        self.codage = aCodage

        # Création des coordonnées
        self.coordonnees = [Coordonnee(f"X{i+1}", fen) for i, fen in enumerate(aFenetres)]

        # Initialisation aléatoire des valeurs réelles
        for c in self.coordonnees:
            c.valeur = c.fenetre.generer_valeur()

        # Génome (si codage utilisé)
        self.genome = None

        # Performance
        self.performance = None


    # ENCODAGE / DECODAGE 

    def encoder(self):
        """Encode les valeurs réelles dans un génome via la stratégie de codage."""
        if self.codage is None:
            raise NotImplementedError("Aucune stratégie de codage n'a été fournie.")
        valeurs = [c.valeur for c in self.coordonnees]
        self.genome = self.codage.encoder(valeurs)

    def decoder(self):
        """Décode un génome vers les valeurs réelles."""
        if self.codage is None:
            raise NotImplementedError("Aucune stratégie de codage n'a été fournie.")
        valeurs = self.codage.decoder(self.genome)
        for c, v in zip(self.coordonnees, valeurs):
            c.valeur = v


    # MUTATION 

    def muter(self, taux, amplitude=0.1):
        """Mutation des coordonnées réelles."""
        for c in self.coordonnees:
            c.muter(taux, amplitude)
        self.performance = None  # performance invalide après mutation


    # EVALUATION

    def evaluer(self, fonction_objectif):
        """Évalue l'individu avec une fonction f(x)."""
        valeurs = [c.valeur for c in self.coordonnees]
        self.performance = fonction_objectif(valeurs)
        return self.performance


    # AFFICHAGE

    def __str__(self):
        valeurs = ", ".join(f"{c.nom}={c.valeur:.4f}" for c in self.coordonnees)
        return f"Individu({valeurs}) -> perf={self.performance}"

    def __repr__(self):
        return self.__str__()


# TEST LOCAL (MAIN)


if __name__ == "__main__":
    print("Test LOCAL de la classe Individu")

    # Création de 2 fenêtres
    fen1 = Fenetre("x1", -5, 5)
    fen2 = Fenetre("x2", -5, 5)

    # Fonction de performance simple (parabole)
    def f_test(x):
        return sum(xi ** 2 for xi in x)

    # Création d'un individu
    ind = Individu([fen1, fen2])
    print("Individu initial :", ind)

    # Évaluation
    ind.evaluer(f_test)
    print("Après évaluation :", ind)

    # Mutation
    print("\nMutation...")
    ind.muter(taux=1.0)  # mutation forcée 100%
    print("Après mutation :", ind)

    # Nouvelle évaluation
    ind.evaluer(f_test)
    print("Performance finale :", ind.performance)
