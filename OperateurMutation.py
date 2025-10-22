"""
Classe : OperateurMutation
Module : OperateurMutation.py
Description :
    Représente l'opérateur de mutation utilisé dans l'algorithme génétique.
    La mutation introduit une petite variation aléatoire sur un individu
    pour maintenir la diversité dans la population.
"""

import random

class OperateurMutation:
    """Classe qui gère la mutation des individus."""

    def __init__(self, aTauxMutation: float = 0.05, aAmplitude: float = 0.1):
        """
        Constructeur.
        :param aTauxMutation: probabilité qu'une coordonnée soit mutée (0.0 à 1.0)
        :param aAmplitude: intensité maximale de la mutation (variation ±)
        """
        self.taux_mutation = aTauxMutation
        self.amplitude = aAmplitude


    def muter(self, individu):
        """
        Applique la mutation sur un individu :
        - Parcourt toutes ses coordonnées,
        - Avec une certaine probabilité, modifie légèrement la valeur.
        """
        if not hasattr(individu, "coordonnees"):
            print("L'individu ne possède pas d'attribut 'coordonnees'")
            return

        for i in range(len(individu.coordonnees)):
            if random.random() < self.taux_mutation:
                # Valeur avant mutation
                ancienne_valeur = individu.coordonnees[i]
                # Ajout d'une petite variation aléatoire
                delta = random.uniform(-self.amplitude, self.amplitude)
                nouvelle_valeur = ancienne_valeur + delta
                individu.coordonnees[i] = nouvelle_valeur
                print(f"Mutation sur coordonnée {i} : {ancienne_valeur:.3f} ce qui donne {nouvelle_valeur:.3f}")

        # Après mutation, on réinitialise la performance (à réévaluer ensuite)
        if hasattr(individu, "performance"):
            individu.performance = None

    def __str__(self):
        return f"OperateurMutation(taux={self.taux_mutation}, amplitude={self.amplitude})"
    

# Test local (exécutable seul)

if __name__ == "__main__":
    print("=== Test de la classe OperateurMutation ===")

    class Individu:
        def __init__(self, coordonnees):
            self.coordonnees = coordonnees
            self.performance = 10
        def __str__(self):
            return f"Individu(coords={self.coordonnees}, perf={self.performance})"

    ind = Individu([0.5, -1.2, 3.4])
    print("Avant mutation :", ind)

    mut = OperateurMutation(aTauxMutation=0.8, aAmplitude=0.5)
    mut.muter(ind)

    print("Après mutation :", ind)
