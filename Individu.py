"""
Classe : Individu
Module : Individu.py
Description :
    Représente un individu de l'algorithme génétique.
    Un individu contient :
        - une liste de Coordonnee
        - une stratégie de codage (optionnelle)
        - une performance évaluée par une fonction objectif

    Il sait :
        - encoder / décoder ses coordonnées
        - muter
        - se croiser via un opérateur externe
        - s'auto-évaluer
"""

import random
from Coordonnee import Coordonnee
from Fenetre import Fenetre
from Performance import Performance


class Individu:

    def __init__(self, aFenetres, aCodage=None):
        """
        Constructeur.
        :param aFenetres: liste d'objets Fenetre (une par coordonnée)
        :param aCodage: stratégie de codage (optionnelle)
        """
        self.fenetres = aFenetres
        self.coordonnees = [Coordonnee(f"X{i+1}", fen) for i, fen in enumerate(aFenetres)]
        self.codage = aCodage

        self.code = None        # représentation codée (binaire, mantisse/exposant…)
        self.performance = None

    #   ENCODAGE / DÉCODAGE


    def encoder(self):
        """Encode les coordonnées en représentation interne (si codage fourni)."""
        if self.codage:
            valeurs = [c.valeur for c in self.coordonnees]
            self.code = self.codage.encoder(valeurs)

    def decoder(self):
        """Décode la représentation interne vers les coordonnées (si codage fourni)."""
        if self.codage and self.code is not None:
            valeurs = self.codage.decoder(self.code)
            for c, v in zip(self.coordonnees, valeurs):
                c.valeur = v


    #   MUTATION


    def muter(self, aTauxMutation, aAmplitude=0.1):
        """
        Applique une mutation à chaque coordonnée.
        :param aTauxMutation: probabilité de mutation
        :param aAmplitude: amplitude relative de la mutation
        """
        for c in self.coordonnees:
            c.muter(aTauxMutation, aAmplitude)

        # performance invalide après mutation
        self.performance = None

    #   PERFORMANCE


    def evaluer(self, aFonctionObjectif):
        """Évalue l'individu et stocke la performance."""
        valeurs = [c.valeur for c in self.coordonnees]
        self.performance = aFonctionObjectif(valeurs)
        return self.performance


    #   AFFICHAGE


    def __str__(self):
        coords = ", ".join(str(c) for c in self.coordonnees)
        return f"Individu({coords}) → perf = {self.performance}"

    def __repr__(self):
        return self.__str__()



# TEST LOCAL 

if __name__ == "__main__":
    print("Test de la classe Individu ")

    # Création de 2 fenêtres
    fen1 = Fenetre("x1", -5, 5)
    fen2 = Fenetre("x2", -5, 5)

    # Création d'un individu
    ind = Individu([fen1, fen2])
    print("Individu généré :", ind)

    # Évaluation
    ind.evaluer(Performance.evaluate)
    print("Après évaluation :", ind)

    # Mutation
    print("\nMutation…")
    ind.muter(aTauxMutation=1.0)  # mutation forcée
    print("Après mutation :", ind)

    # Réévaluation
    ind.evaluer(Performance.evaluate)
    print("Performance finale :", ind.performance)
