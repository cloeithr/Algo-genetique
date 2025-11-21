"""
Classe : OperateurMutation
Module : OperateurMutation.py
Description :
    Opérateur de mutation pour l'algorithme génétique.
    Peut fonctionner :
        - sur un code binaire (si 'code' existe)
        - sur les valeurs réelles des coordonnées
"""

import random
from Fenetre import Fenetre
from Coordonnee import Coordonnee

class OperateurMutation:
    """Mutation génétique : binaire OU réel."""

    def __init__(self, aTauxMutation: float = 0.05, aAmplitude: float = 0.1):
        """
        Constructeur.
        :param aTauxMutation: probabilité de muter un gène
        :param aAmplitude: amplitude max de mutation (pour les réels)
        """
        self.taux = aTauxMutation
        self.amplitude = aAmplitude

    # MUTATION

    def muter(self, individu):
        """Applique la mutation sur un individu."""

        # Mode binaire si 'code' existe
        if hasattr(individu, "code") and individu.code is not None:
            self._muter_code(individu)
        else:
            self._muter_reel(individu)

        # invalider la performance
        individu.performance = None

    # MUTATION SUR CODE BINAIRE

    def _muter_code(self, individu):
        """Mutation bit à bit sur un code binaire."""

        genome = list(individu.code)   # string → liste de caractères
        taille = len(genome)

        for i in range(taille):
            if random.random() < self.taux:
                genome[i] = "1" if genome[i] == "0" else "0"

        individu.code = "".join(genome)

        # mise à jour coordonnees après mutation
        if hasattr(individu, "decoder"):
            individu.decoder()

    # MUTATION SUR RÉELS

    def _muter_reel(self, individu):
        """Mutation Gaussienne légère sur les valeurs réelles."""

        for coord in individu.coordonnees:
            if random.random() < self.taux:

                delta = random.uniform(-self.amplitude, self.amplitude)
                nouvelle_valeur = coord.valeur + delta

                # respect de la fenêtre
                nouvelle_valeur = max(coord.fenetre.borne_min,
                                      min(nouvelle_valeur, coord.fenetre.borne_max))

                coord.valeur = nouvelle_valeur

    # AFFICHAGE

    def __str__(self):
        return f"OperateurMutation(taux={self.taux}, amplitude={self.amplitude})"


#TEST LOCAL
if __name__ == "__main__":
    print("=== Test local OperateurMutation ===")
    class IndividuTest:
        """Individu réel pour tests."""
        def __init__(self, fenetres):
            self.fenetres = fenetres
            self.coordonnees = [Coordonnee(f"X{i+1}", f) for i, f in enumerate(fenetres)]
            self.code = None
            self.performance = 0

        def __str__(self):
            c = ", ".join(str(co) for co in self.coordonnees)
            return f"IndividuTest({c})"

    # Fenêtres
    fen1 = Fenetre("x1", -10, 10)
    fen2 = Fenetre("x2", -10, 10)
    fenetres = [fen1, fen2]

    # Création d’un individu
    ind = IndividuTest(fenetres)
    print("Avant mutation :", ind)

    # Mutation
    mut = OperateurMutation(aTauxMutation=1.0, aAmplitude=3)
    mut.muter(ind)

    print("Après mutation :", ind)
