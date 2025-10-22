"""
Classe : OperateurSelection
Module : OperateurSelection.py
Description :
    Représente l'opérateur de sélection des individus dans la population.
    Implémente une méthode de sélection par roulette de la fortune (stochastique).
"""

import random

class OperateurSelection:
    """Opérateur de sélection : choisit deux individus selon leur performance."""

 
    # Constructeur
 
    def __init__(self):
        """Constructeur vide (aucune initialisation spécifique pour cet opérateur)."""
        pass

 
    # Méthode principale
 
    def selectionner(self, aPopulation):
        """
        Sélectionne deux parents dans la population à l'aide de la roulette de la fortune.
        Chaque individu a une probabilité proportionnelle à sa performance.
        """
        individus = aPopulation.individus
        performances = [ind.performance for ind in individus]

        # Normalisation (évite les divisions par zéro)
        total = sum(performances)
        if total == 0:
            probabilites = [1 / len(performances)] * len(performances)
        else:
            probabilites = [p / total for p in performances]

        # Sélection aléatoire pondérée
        p1 = random.choices(individus, weights=probabilites, k=1)[0]
        p2 = random.choices(individus, weights=probabilites, k=1)[0]

        print(f"Sélectionnés : {p1} et {p2}")
        return p1, p2

 
    # Affichage

    def __str__(self):
        """Affichage simple."""
        return "OperateurSelection()"


#  Test local

if __name__ == "__main__":
    print("=== Test de la classe OperateurSelection ===")

    class Individu:
        """Classe de test simple pour représenter un individu."""
        def __init__(self, nom, perf):
            self.nom = nom
            self.performance = perf
        def __str__(self):
            return f"{self.nom}({self.performance})"

    class Population:
        """Classe de test simple pour représenter une population d'individus."""
        def __init__(self):
            self.individus = [
                Individu("A", 10),
                Individu("B", 30),
                Individu("C", 60)
            ]

    pop = Population()
    sel = OperateurSelection()
    sel.selectionner(pop)
