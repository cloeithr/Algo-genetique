import random
from Individu import Individu 

class Population: 
    def __init__(self, taille, fenetres, fonction_objectif, codage=None):
        self.taille = taille
        self.fenetres = fenetres
        self.fonction_objectif = fonction_objectif
        self.codage = codage
        self.individus = []  # liste d'objets Individu
 
    def initialiser(self):
        """Crée une population aléatoire d'individus dans les bornes."""
        self.individus = [] 
        for _ in range(self.taille):
            coordonnees = [
                random.uniform(xmin, xmax) for (xmin, xmax) in self.fenetres
            ]
            individu = Individu(coordonnees, self.fenetres, self.codage)
            self.individus.append(individu)

    def evaluer(self):
        """Évalue tous les individus de la population."""
        for individu in self.individus:
            individu.evaluer(self.fonction_objectif)

    def meilleur(self):
        """Retourne le meilleur individu selon la performance."""
        return min(self.individus, key=lambda ind: ind.performance)

    def selection_tournoi(self, taille_tournoi=3):
        """Sélectionne un individu par tournoi."""
        candidats = random.sample(self.individus, taille_tournoi)
        return min(candidats, key=lambda ind: ind.performance)

    def remplacer(self, nouvel_individu, index):
        """Remplace un individu à une position donnée."""
        self.individus[index] = nouvel_individu

    def __repr__(self):
        return f"Population(taille={self.taille}, meilleur={self.meilleur()})"


# Test de la classe pour voir si ça fonctionne

def fonction_test(x):
    return sum([xi**2 for xi in x])  # fonction simple

fenetres = [(-5, 5), (-5, 5)]

# Créer une population
pop = Population(taille=5, fenetres=fenetres, fonction_objectif=fonction_test)

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

# Sélection d'un parent par tournoi
parent = pop.selection_tournoi()
print("\nParent sélectionné :", parent)

