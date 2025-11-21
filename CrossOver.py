"""
Classe : OperateurCrossOver
Module : CrossOver.py
Description :
    Opérateur de croisement multipoint pour l'algorithme génétique.

    Deux cas :
        1) Les parents possèdent un attribut 'code' (génome binaire) :
           croisement sur ce génome.
        2) Sinon :
           croisement sur la liste des valeurs réelles des coordonnées.

    Le croisement multipoint :
        - choisir N points de coupure
        - alterner les segments P1/P2 pour produire deux enfants
"""

import random
from Fenetre import Fenetre
from Coordonnee import Coordonnee

class OperateurCrossOver:
    """Croisement multipoint entre 2 individus."""

    def __init__(self, aNbPoints: int = 2):
        """
        Constructeur.
        :param aNbPoints: nombre de points de coupure (>=1)
        """
        if aNbPoints < 1:
            raise ValueError("Le nombre de points de coupure doit être ≥ 1.")
        self.nb_points = aNbPoints

    # CROISEMENT

    def croiser(self, aParent1, aParent2):
        """
        Effectue un croisement multipoint.
        Retourne (enfant1, enfant2).
        """

        # 1) Déterminer le support de croisement

        mode = None

        if (hasattr(aParent1, "code") and aParent1.code is not None and
            hasattr(aParent2, "code") and aParent2.code is not None):

            # Mode binaire
            genome1 = list(aParent1.code)
            genome2 = list(aParent2.code)
            mode = "code"

        else:
            # Mode réel : coordonnées
            genome1 = [c.valeur for c in aParent1.coordonnees]
            genome2 = [c.valeur for c in aParent2.coordonnees]
            mode = "reel"

        # 2) Vérifications

        if len(genome1) != len(genome2):
            raise ValueError("Les génomes doivent avoir la même taille.")

        taille = len(genome1)
        if taille < 2:
            raise ValueError("Le génome doit avoir ≥ 2 éléments.")

        # Nombre effectif de coupures
        nb_points_eff = min(self.nb_points, taille - 1)

        # 3) Points de coupure

        points = sorted(random.sample(range(1, taille), nb_points_eff))
        points = [0] + points + [taille]

        enfant1_genome = []
        enfant2_genome = []

        # Alterner les segments
        for i in range(len(points) - 1):
            start, end = points[i], points[i + 1]

            seg1 = genome1[start:end]
            seg2 = genome2[start:end]

            if i % 2 == 0:   # segment pair : P1 → E1, P2 → E2
                enfant1_genome.extend(seg1)
                enfant2_genome.extend(seg2)
            else:           # segment impair : P2 → E1, P1 → E2
                enfant1_genome.extend(seg2)
                enfant2_genome.extend(seg1)

        #  4) Construction des enfants

        enfant1 = type(aParent1)(aParent1.fenetres, aParent1.codage)
        enfant2 = type(aParent2)(aParent2.fenetres, aParent2.codage)

        enfant1.performance = None
        enfant2.performance = None

        if mode == "code":
            # On reconstruit une string binaire
            enfant1.code = "".join(enfant1_genome)
            enfant2.code = "".join(enfant2_genome)

            # On décode vers les valeurs réelles
            enfant1.decoder()
            enfant2.decoder()

        else:
            # Mode réel  valeurs dans les Coordonnee
            for coord, val in zip(enfant1.coordonnees, enfant1_genome):
                coord.valeur = val
            for coord, val in zip(enfant2.coordonnees, enfant2_genome):
                coord.valeur = val

        return enfant1, enfant2

    # AFFICHAGE

    def __str__(self):
        return f"OperateurCrossOver(multipoint, nb_points={self.nb_points})"


# TEST LOCAL (MAIN)


if __name__ == "__main__":
    print("=== Test LOCAL OperateurCrossOver ===")

    class IndividuReel:
        """Bouchon temporaire uniquement pour tester."""
        def __init__(self, fenetres, codage=None):
            self.fenetres = fenetres
            self.codage = codage
            self.coordonnees = [Coordonnee(f"X{i+1}", f) for i, f in enumerate(fenetres)]
            self.code = None
            self.performance = None

        def __str__(self):
            coords = ", ".join(str(c) for c in self.coordonnees)
            return f"IndividuReel({coords})"

    # Fenêtres
    fen1 = Fenetre("x1", -5, 5)
    fen2 = Fenetre("x2", -5, 5)
    fenetres = [fen1, fen2]

    # Deux parents
    p1 = IndividuReel(fenetres)
    p2 = IndividuReel(fenetres)

    print("Parent 1 :", p1)
    print("Parent 2 :", p2)

    # Croisement multipoint
    op = OperateurCrossOver(aNbPoints=1)
    e1, e2 = op.croiser(p1, p2)

    print("\nEnfant 1 :", e1)
    print("Enfant 2 :", e2)
