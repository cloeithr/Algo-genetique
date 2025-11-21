"""
Classe : AlgorithmeGenetique
Module : AlgorithmeGenetique.py
Description :
    Coordonne l'exécution de l'lgorithme génétique complet.

    Rôle :
        - initialiser la population
        - exécuter les générations successives
        - appliquer : sélection, croisement, mutation, remplacement
        - suivre la performance du meilleur individu
        - détecter une stagnation (simple version)
"""

from Population import Population
from OperateurSelection import OperateurSelection
from CrossOver import OperateurCrossOver
from OperateurMutation import OperateurMutation
from OperateurRemplacement import OperateurRemplacement
from Performance import Performance


class AlgorithmeGenetique:

    def __init__(self, aPopulation, aSelection, aCroisement, aMutation, aRemplacement,
                 aNbGenerations=20, aTauxMutation=0.1):
        """
        Constructeur principal.
        """
        self.population = aPopulation
        self.op_selection = aSelection
        self.op_cross = aCroisement
        self.op_mutation = aMutation
        self.op_remplacement = aRemplacement

        self.nb_generations = aNbGenerations
        self.taux_mutation = aTauxMutation

        self.meilleur = None
        self.historique = []
        self.generation_courante = 0






    # INITIALISATION

    def initialiser(self):
        print("Initialisation de la population")
        self.population.initialiser()
        self.population.evaluer()
        self.meilleur = self.population.meilleur()
        print(f" - Meilleur individu initial : {self.meilleur}")

    # UNE GÉNÉRATION

    def generation(self):
        # 1) Sélection
        p1, p2 = self.op_selection.selectionner(self.population)

        # 2) Croisement
        e1, e2 = self.op_cross.croiser(p1, p2)

        # 3) Mutation
        self.op_mutation.muter(e1)
        self.op_mutation.muter(e2)

        # 4) Évaluation
        e1.evaluer(Performance.evaluate)
        e2.evaluer(Performance.evaluate)

        # 5) Remplacement
        self.op_remplacement.remplacer(self.population, p1, p2, e1, e2)

        # 6) Réévaluation population
        self.population.evaluer()
        self.meilleur = self.population.meilleur()

        print(f"   -> Meilleur : {self.meilleur}")

    # BOUCLE PRINCIPALE

    def lancer(self):
        print(f"\n=== Lancement de {self.nb_generations} générations ===\n")

        for g in range(self.nb_generations):
            print(f">>> Génération {g+1}")
            self.generation()
            self.historique.append(self.meilleur.performance)

        print("\n=== Evolution terminée ===")
        self.afficher_resultats()

    # AFFICHAGE FINAL

    def afficher_resultats(self):
        print("\n=== Résultat final ===")
        print("Meilleur individu :", self.meilleur)
        print("Performance :", self.meilleur.performance)


# TEST LOCAL

if __name__ == "__main__":
    print("=== Test local : AlgorithmeGenetique ===")

    # Construction des objets nécessaires
    from Fenetre import Fenetre

    fenetres = [Fenetre("x1", -5, 5), Fenetre("x2", -5, 5)]

    pop = Population(aTaille=6, aFenetres=fenetres,
                     aFonctionObjectif=Performance.evaluate)

    sel = OperateurSelection()
    cross = OperateurCrossOver(aNbPoints=1)
    mut = OperateurMutation(aTauxMutation=0.3, aAmplitude=0.3)
    remp = OperateurRemplacement()

    algo = AlgorithmeGenetique(pop, sel, cross, mut, remp,
                               aNbGenerations=10)

    algo.initialiser()
    algo.lancer()
