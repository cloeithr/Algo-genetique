"""
Classe : OperateurMutation
Module : OperateurMutation.py
Description :
    Implémente l'opérateur de mutation de l'algorithme génétique.
    Deux cas sont pris en charge :
        - mutation binaire (0 ↔ 1)
        - mutation réelle (variation dans la fenêtre)
"""

import random
from Fenetre import Fenetre
from Coordonnee import Coordonnee
from Individu import Individu

class OperateurMutation:
    """Opérateur de mutation générique."""

    def __init__(self, aTauxMutation: float = 0.05):
        """
        :param aTauxMutation: probabilité qu’un gène soit muté
        """
        self.taux = aTauxMutation


    def _mutation_binaire(self, code_binaire: str) -> str:
        """Inverse aléatoirement des bits selon le taux de mutation."""
        nouveau_code = ""

        for bit in code_binaire:
            if random.random() < self.taux:
                nouveau_code += "1" if bit == "0" else "0"
            else:
                nouveau_code += bit

        return nouveau_code


    def _mutation_reelle(self, individu):
        """Applique une petite variation dans la fenêtre de chaque coordonnée."""
        for coord in individu.coordonnees:
            if random.random() < self.taux:
                amplitude = (coord.fenetre.borne_max - coord.fenetre.borne_min) * 0.1
                delta = random.uniform(-amplitude, amplitude)
                nouvelle_valeur = coord.valeur + delta

                # On reste dans la fenêtre
                coord.valeur = max(coord.fenetre.borne_min,
                                   min(nouvelle_valeur, coord.fenetre.borne_max))



    def muter(self, individu):
        """
        Applique la mutation à un individu :
            - Si individu.code existe → mutation binaire
            - Sinon → mutation réelle
        """
        if individu.code is not None:
            # Mutation du code binaire
            individu.code = self._mutation_binaire(individu.code)
            # Décodage vers valeurs réelles
            individu.decoder()
        else:
            # Mutation sur valeurs réelles
            self._mutation_reelle(individu)

        individu.performance = None  # invalide la performance

    def __str__(self):
        return f"OperateurMutation(taux={self.taux})"



#  TEST LOCAL

if __name__ == "__main__":
    print("Test de OperateurMutation")



    # Individu réel
    f1 = Fenetre("x1", -5, 5)
    f2 = Fenetre("x2", -5, 5)
    ind = Individu([f1, f2])

    print("Avant mutation :", ind)

    mut = OperateurMutation(aTauxMutation=1.0)  # mutation forcée pour tester
    mut.muter(ind)

    print("Après mutation :", ind)
