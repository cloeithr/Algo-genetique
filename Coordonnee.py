"""
Classe : Coordonnee
Module : Coordonnee.py
Description :
    Représente une variable réelle x_i appartenant à une fenêtre de recherche.
    Chaque coordonnée sait se générer, se muter et rester dans ses bornes.
"""

import random
from Fenetre import Fenetre


class Coordonnee:
    """Représente une variable réelle dans une fenêtre donnée."""

    def __init__(self, aNom: str, aFenetre: Fenetre):
        """
        Constructeur.
        :param aNom: nom de la coordonnée (ex : "x1")
        :param aFenetre: objet Fenetre associé
        """
        self.nom = aNom
        self.fenetre = aFenetre
        self.valeur = self.fenetre.generer_valeur()


    def muter(self, aTauxMutation: float, aAmplitude: float = 0.1):
        """
        Applique une mutation à la coordonnée si le tirage le permet.
        :param aTauxMutation: probabilité de mutation
        :param aAmplitude: pourcentage de la fenêtre utilisé pour la variation
        """
        if random.random() < aTauxMutation:
            # Amplitude basée sur la taille de la fenêtre.
            plage = (self.fenetre.borne_max - self.fenetre.borne_min) * aAmplitude
            delta = random.uniform(-plage, plage)

            nouvelle = self.valeur + delta

            # On reste dans la fenêtre
            self.valeur = max(self.fenetre.borne_min,
                              min(nouvelle, self.fenetre.borne_max))



    def generer_aleatoire(self):
        """Regénère une nouvelle valeur dans la fenêtre."""
        self.valeur = self.fenetre.generer_valeur()


    def __str__(self):
        return f"{self.nom} = {self.valeur:.4f}"

    def __repr__(self):
        return f"Coordonnee({self.nom}, valeur={self.valeur:.4f})"



#TEST LOCAL 

if __name__ == "__main__":
    print("Test de la classe Coordonnee")

    # Création d'une fenêtre
    fen = Fenetre("x1", -10, 10)

    # Création d'une coordonnée
    c = Coordonnee("x1", fen)
    print("Valeur initiale p:", c)

    # Test mutationgfhjfghgfht
    print("\nMutation (taux=1.0 pour être sûr de muter) :")
    c.muter(aTauxMutation=1.0)
    print("Après mutation :", c)

    # Test regénération
    print("\nRegénération :")
    c.generer_aleatoire()
    print("Nouvelle valeur deff:", c)
