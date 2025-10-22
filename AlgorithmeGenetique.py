"""
Classe : AlgorithmeGenetique
Module : AlgorithmeGenetique.py
Description :
    Cette classe coordonne le déroulement complet de  notre algorithme génétique.
    Elle initialise la population, gère les générations successives,
    et appelle les opérateurs de sélection, croisement, mutation et remplacement.
"""

# Importation des classes nécessaires
from Population import Population
from OperateurSelection import OperateurSelection
from CrossOver import CrossOver
from OperateurMutation import OperateurMutation
from Evaluation import EvaluationParabole

# Ma classe 

class AlgorithmeGenetique:
    """Classe principale qui pilote l'évolution génétique."""

    def __init__(self, aPopulation, aSelection, aCroisement, aMutation, aRemplacement, aNbGenerations):
        """Constructeur : initialise tous les composants de l'algorithme."""
        self.population = aPopulation
        self.operateur_selection = aSelection
        self.operateur_croisement = aCroisement
        self.operateur_mutation = aMutation
        self.operateur_remplacement = aRemplacement
        self.nb_generations = aNbGenerations
        self.generation_courante = 0
        self.meilleur_individu = None
        self.historique_performance = []


    def initialiser_population(self):
        """Initialise la population de départ et évalue les individus."""
        print("Initialisation de la population...")
        self.population.initialiser()
        self.population.evaluer()
        self.meilleur_individu = self.population.meilleur()
        print(f"Meilleur individu initial : {self.meilleur_individu}")

    def lancer_evolution(self):
        """Boucle principale de l'évolution génétique."""
        print(f"Lancement de {self.nb_generations} générations.")
        for g in range(self.nb_generations):
            print(f"--- Génération {g+1} ---")
            self.generation_courante = g + 1
            self.generation()
            self.historique_performance.append(self.meilleur_individu.performance)
        print("Évolution terminée.")
        self.afficher_resultats()

    def generation(self):
        """Effectue une génération complète (sélection, croisement, mutation, remplacement)."""
        # Sélection de deux parents
        p1, p2 = self.operateur_selection.selectionner(self.population)

        # Croisement donne deux enfants
        e1, e2 = self.operateur_croisement.croiser(p1, p2)

        # Mutation des enfants
        self.operateur_mutation.muter(e1)
        self.operateur_mutation.muter(e2)

        # Remplacement dans la population
        self.operateur_remplacement.remplacer(self.population, p1, p2, e1, e2)

        # Réévaluation de la population
        self.population.evaluer()

        # Mise à jour du meilleur individu
        self.meilleur_individu = self.population.meilleur()
        print(f"Meilleur de la génération {self.generation_courante} : {self.meilleur_individu}")


    def afficher_resultats(self):
        """Affiche les résultats finaux de l'évolution."""
        print("\n=== Résultats finaux ===")
        print(f"Meilleur individu : {self.meilleur_individu}")
        print(f"Performance : {self.meilleur_individu.performance}")


    def __str__(self):
        """Affichage simplifié de l'état de l'algorithme."""
        return f"AlgorithmeGénétique : génération {self.generation_courante}/{self.nb_generations}"
    

# Test local

if __name__ == "__main__":
    print("=== Test de la classe AlgorithmeGenetique ===")

    class Population:
        def initialiser(self): print(" Population initialisée")
        def evaluer(self): print(" Population évaluée")
        def meilleur(self): return "IndividuTemporaire"

    class OperateurSelection:
        def selectionner(self, population): print(" Sélection"); return "P1", "P2"

    class CrossOver:
        def croiser(self, p1, p2): print(" Croisement"); return "E1", "E2"

    class OperateurMutation:
        def muter(self, individu): print(f" Mutation sur {individu}")

    class OperateurRemplacement:
        def remplacer(self, population, p1, p2, e1, e2): print("Remplacement effectué")

    algo = AlgorithmeGenetique(Population(), OperateurSelection(), CrossOver(), OperateurMutation(), OperateurRemplacement(), 5)
    algo.initialiser_population()
    algo.lancer_evolution()
