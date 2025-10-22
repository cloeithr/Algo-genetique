import random
from Individu import Individu 

class Population: 
    def __init__(self, ataille, afenetres, afonction_objectif, acodage=None):
        self.taille = ataille
        self.fenetres = afenetres
        self.fonction_objectif = afonction_objectif
        self.codage = acodage
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
        
    def croiser(self, parent1, parent2):
        """Croisement simple sur les coordonnées réelles"""
        enfant1_coord, enfant2_coord = [], []
        for x1, x2 in zip(parent1.coordonnees, parent2.coordonnees):
            if random.random() < 0.5:
                enfant1_coord.append(x1)
                enfant2_coord.append(x2)
            else:
                enfant1_coord.append(x2)
                enfant2_coord.append(x1)
        return Individu(enfant1_coord, self.fenetres, self.codage), \
            Individu(enfant2_coord, self.fenetres, self.codage)


    def evoluer(self, generations=50, taux_mutation=0.1):
        for _ in range(generations):
            self.evaluer()
            new_individus = []
            while len(new_individus) < self.taille:
                # Sélection de deux parents
                p1 = self.selection_tournoi()
                p2 = self.selection_tournoi()
                
                # Croisement pour obtenir deux enfants
                e1, e2 = self.croiser(p1, p2)
                
                # Mutation
                e1.muter(taux_mutation)
                e2.muter(taux_mutation)
                
                new_individus.extend([e1, e2])
            
            # Remplacer l'ancienne population
            self.individus = new_individus[:self.taille]

    def __repr__(self):
        return f"Population(taille={self.taille}, meilleur={self.meilleur()})"


if __name__ == '__main__':
    
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