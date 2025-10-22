import random

class Crossover:
    """Classe responsable du croisement multipoint entre deux individus."""

    def __init__(self, aNb_points=2):
        """
        nb_points : nombre de points de coupure.
        Par défaut, on fait un crossover à 2 points.
        """
        self.nb_points = aNb_points

    def appliquer(self, aParent1, aParent2):
        """
        Effectue un crossover multipoint entre deux parents (père, mère)
        et retourne deux enfants (e1, e2).
        """

        # --- Étape 1️⃣ : Récupération des mantisses binaires des parents
        m1 = aParent1.mantisse
        m2 = aParent2.mantisse
        taille = len(m1)

        # --- Étape 2️⃣ : Vérification de cohérence
        if len(m1) != len(m2):
            raise ValueError("Les deux parents doivent avoir la même taille de mantisse")

        # --- Étape 3️⃣ : Choix aléatoire des points de coupure ---
        points = sorted(random.sample(range(1, taille), self.nb_points))
        points = [0] + points + [taille]  # On ajoute le début et la fin pour couvrir toute la mantisse

        # --- Étape 4️⃣ : Construction des enfants par alternance de segments
        enfant1, enfant2 = "", ""
        for i in range(len(points) - 1):
            debut, fin = points[i], points[i + 1]
            if i % 2 == 0:  # segment pair → père → enfant1
                enfant1 += m1[debut:fin]
                enfant2 += m2[debut:fin]
            else:  # segment impair → mère → enfant1
                enfant1 += m2[debut:fin]
                enfant2 += m1[debut:fin]

        # --- Étape 5️⃣ : Création des nouveaux objets enfants ---
        e1 = type(aParent1)()
        e2 = type(aParent2)()

        e1.mantisse, e2.mantisse = enfant1, enfant2
        e1.exposant, e2.exposant = aParent1.exposant, aParent2.exposant
        e1.signe, e2.signe = random.choice([aParent1.signe, aParent2.signe]), random.choice([aParent1.signe, aParent2.signe])

        e1.decoder()
        e2.decoder()

        return e1, e2
