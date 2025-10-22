from Individu import Individu
import random

class Population:
    """Classe qui gère l'ensemble des individus."""

    def __init__(self, ataille, afenetres, afonction_objectif, acodage=None):
        self.taille = ataille
        self.fenetres = afenetres
        self.fonction_objectif = afonction_objectif
        self.codage = acodage
        self.individus = [] 

    def initialiser(self):
        """Crée une population aléatoire d'individus."""
        self.individus = []
        for _ in range(self.taille):
            coordonnees = [random.uniform(xmin, xmax) for (xmin, xmax) in self.fenetres]
            individu = Individu(coordonnees, self.fenetres, self.codage)
            self.individus.append(individu)

    def evaluer(self):
        """Évalue tous les individus."""
        for individu in self.individus:
            individu.evaluer(self.fonction_objectif)

    def meilleur(self):
        """Retourne le meilleur individu."""
        return min(self.individus, key=lambda ind: ind.performance)

    def remplacer(self, nouvel_individu, index):
        """Remplace un individu à une position donnée."""
        self.individus[index] = nouvel_individu  
        

if __name__ == '__main__':
    from Individu import Individu
    import random

    # Fonction objectif simple
    def fonction_test(x):
        return sum([xi**2 for xi in x])  # minimisation de x1² + x2²

    # Fenêtres de recherche pour chaque coordonnée
    fenetres = [(-5, 5), (-5, 5)]

    # Créer une population
    pop = Population(ataille=5, afenetres=fenetres, afonction_objectif=fonction_test)

    # Initialiser les individus
    pop.initialiser()
    print("Population initiale :")
    for ind in pop.individus:
        print(ind)

    # Évaluer tous les individus
    pop.evaluer()
    print("\nPopulation après évaluation :")
    for ind in pop.individus:
        print(ind)  

    # Trouver le meilleur individu
    print("\nMeilleur individu :", pop.meilleur())
