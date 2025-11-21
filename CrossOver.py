"""
Classe : OperateurCrossOver
Module : CrossOver.py
Description :
    Opérateur de croisement multipoint pour l'algorithme génétique.

    - Si les parents possèdent un attribut 'code' (génome binaire, mantisse/exposant),
      le croisement s'effectue sur ce code.
    - Sinon, le croisement est réalisé directement sur les valeurs réelles
      de leurs coordonnées.

    Le croisement multipoint consiste à :
        - choisir N points de coupure,
        - découper les deux génomes en segments,
        - alterner les segments (P1/P2) pour produire deux enfants.
"""

import random
from Fenetre import Fenetre
from Coordonnee import Coordonnee

class OperateurCrossOver:
    """Classe responsable du croisement multipoint entre deux individus."""

    def __init__(self, aNbPoints: int = 2):
        """
        Constructeur.
        :param aNbPoints: nombre de points de coupure (>= 1)
        """
        if aNbPoints < 1:
            raise ValueError("Le nombre de points de coupure doit être au moins 1.")
        self.nb_points = aNbPoints


    def croiser(self, aParent1, aParent2):
        """
        Effectue un croisement multipoint entre deux parents
        et retourne deux enfants.

        Stratégie :
            - si les parents possèdent un génome 'code' non nul,
              le croisement s'effectue sur ce code ;
            - sinon, le croisement s'effectue sur la liste des valeurs
              des coordonnées (réels).
        """

        # 1) Déterminer le support de croisement : génome ou valeurs réelles

        mode = None

        if hasattr(aParent1, "code") and hasattr(aParent2, "code") \
           and (aParent1.code is not None) and (aParent2.code is not None):
            # Mode "code" (binaire / mantisse-exposant…)
            genome1 = aParent1.code
            genome2 = aParent2.code
            mode = "code"

        else:
            # Mode "réel" : on travaille directement sur les valeurs des coordonnées
            genome1 = [c.valeur for c in aParent1.coordonnees]
            genome2 = [c.valeur for c in aParent2.coordonnees]
            mode = "reel"

        # 2) Vérifications de cohérence

        if len(genome1) != len(genome2):
            raise ValueError("Les deux parents doivent avoir des génomes de même taille.")

        taille = len(genome1)
        if taille < 2:
            raise ValueError("Le génome doit avoir au moins 2 éléments pour le croisement.")

        # Nombre de points effective : ne peut pas dépasser taille - 1
        nb_points_eff = min(self.nb_points, taille - 1)

        # 3) Tirage des points de coupure et construction des segments

        points = sorted(random.sample(range(1, taille), nb_points_eff))
        points = [0] + points + [taille]  # on encadre début et fin

        enfant1_genome = []
        enfant2_genome = []

        # On alterne les segments entre parent1 et parent2
        for i in range(len(points) - 1):
            start, end = points[i], points[i + 1]

            # Segment de P1 et P2
            seg1 = genome1[start:end]
            seg2 = genome2[start:end]

            if i % 2 == 0:
                # Segment pair : enfant1 <- P1, enfant2 <- P2
                enfant1_genome.extend(seg1)
                enfant2_genome.extend(seg2)
            else:
                # Segment impair : enfant1 <- P2, enfant2 <- P1
                enfant1_genome.extend(seg2)
                enfant2_genome.extend(seg1)

        # 4) Création des objets enfants

        enfant1 = type(aParent1)(aParent1.fenetres, aParent1.codage)
        enfant2 = type(aParent2)(aParent2.fenetres, aParent2.codage)

        # On invalide leur performance (à réévaluer ensuite)
        enfant1.performance = None
        enfant2.performance = None

        if mode == "code":
            # On assigne le génome binaire et on décode vers les coordonnées
            enfant1.code = enfant1_genome if isinstance(enfant1_genome, str) else "".join(enfant1_genome)
            enfant2.code = enfant2_genome if isinstance(enfant2_genome, str) else "".join(enfant2_genome)

            if hasattr(enfant1, "decoder"):
                enfant1.decoder()
            if hasattr(enfant2, "decoder"):
                enfant2.decoder()

        else:  # mode == "reel"
            # On met à jour les valeurs des coordonnées
            for coord, val in zip(enfant1.coordonnees, enfant1_genome):
                coord.valeur = val
            for coord, val in zip(enfant2.coordonnees, enfant2_genome):
                coord.valeur = val

        return enfant1, enfant2



    def __str__(self):
        return f"OperateurCrossOver(multipoint, nb_points={self.nb_points})"


# TEST LOCAL

if __name__ == "__main__":
    print("=== Test de OperateurCrossOver (mode réel) ===")



    class IndividuReel:
        """Petit bouchon d'individu pour tester le croisement sur des réels."""
        def __init__(self, aFenetres, aCodage=None):
            self.fenetres = aFenetres
            self.codage = aCodage
            self.coordonnees = [Coordonnee(f"X{i+1}", f) for i, f in enumerate(aFenetres)]
            self.code = None
            self.performance = None

        def __str__(self):
            coords = ", ".join(str(c) for c in self.coordonnees)
            return f"IndividuReel({coords})"

    # Fenêtres
    fen1 = Fenetre("x1", -5, 5)
    fen2 = Fenetre("x2", -5, 5)
    fenetres = [fen1, fen2]

    # Création de 2 parents
    p1 = IndividuReel(fenetres)
    p2 = IndividuReel(fenetres)
    print("Parent 1 :", p1)
    print("Parent 2 :", p2)

    # Croisement
    op = OperateurCrossOver(aNbPoints=1)
    e1, e2 = op.croiser(p1, p2)

    print("\nEnfant 1 :", e1)
    print("Enfant 2 :", e2)
