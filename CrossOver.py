"""
Classe : OperateurCrossOver
Module : OperateurCrossOver.py
Description :
    Réalise un croisement multipoint entre deux individus.
    Si un codage binaire existe → croisement sur le code.
    Sinon → croisement réel sur les coordonnées.
"""

import random
from Fenetre import Fenetre
from Individu import Individu

class OperateurCrossOver:

    def __init__(self, aNbPoints=2):
        """
        :param aNbPoints: nombre de points de coupure pour le multipoint.
        """
        self.nb_points = aNbPoints


    #   CROISEMENT BINAIRE

    def _croiser_binaire(self, code1: str, code2: str):
        """
        Croisement multipoint entre deux chaînes binaires.
        """
        taille = len(code1)

        # Points de coupure (triés)
        points = sorted(random.sample(range(1, taille), self.nb_points))
        points = [0] + points + [taille]

        enfant1 = ""
        enfant2 = ""

        for i in range(len(points) - 1):
            d, f = points[i], points[i + 1]

            if i % 2 == 0:  # segments pairs → parent 1
                enfant1 += code1[d:f]
                enfant2 += code2[d:f]
            else:           # segments impairs → parent 2
                enfant1 += code2[d:f]
                enfant2 += code1[d:f]

        return enfant1, enfant2

    #   CROISEMENT RÉEL

    def _croiser_reel(self, parent1, parent2):
        """Croisement simple sur valeurs réelles."""
        coord1 = []
        coord2 = []

        for c1, c2 in zip(parent1.coordonnees, parent2.coordonnees):
            if random.random() < 0.5:
                coord1.append(c1.valeur)
                coord2.append(c2.valeur)
            else:
                coord1.append(c2.valeur)
                coord2.append(c1.valeur)

        return coord1, coord2


    #   MÉTHODE PRINCIPALE

    def croiser(self, parent1, parent2):
        """
        Retourne deux nouveaux individus (enfants) créés par croisement.
        """

        # --- Cas 1 : codage binaire
        if parent1.code is not None and parent2.code is not None:
            enfant1_code, enfant2_code = self._croiser_binaire(parent1.code, parent2.code)

            # Création des enfants (même classe que les parents)
            e1 = type(parent1)(parent1.fenetres, parent1.codage)
            e2 = type(parent2)(parent2.fenetres, parent2.codage)

            e1.code = enfant1_code
            e2.code = enfant2_code

            # Décodage pour obtenir les valeurs réelles
            e1.decoder()
            e2.decoder()

            return e1, e2

        #  Cas 2 : croisement réel
        valeurs1, valeurs2 = self._croiser_reel(parent1, parent2)

        e1 = type(parent1)(parent1.fenetres)
        e2 = type(parent2)(parent2.fenetres)

        # Affectation des valeurs
        for v, coord in zip(valeurs1, e1.coordonnees):
            coord.valeur = v
        for v, coord in zip(valeurs2, e2.coordonnees):
            coord.valeur = v

        return e1, e2



#   TEST LOCAL

if __name__ == "__main__":
    print("Test OperateurCrossOver")

    f1 = Fenetre("x1", -5, 5)
    f2 = Fenetre("x2", -5, 5)

    p1 = Individu([f1, f2])
    p2 = Individu([f1, f2])

    print("Parent 1 :", p1)
    print("Parent 2 :", p2)

    cross = OperateurCrossOver(aNbPoints=2)
    e1, e2 = cross.croiser(p1, p2)

    print("\nEnfant 1 :", e1)
    print("Enfant 2 :", e2)
