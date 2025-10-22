import random

class Individu: 
    def __init__(self, acoordonnees, afenetres, acodage=None):
        self.coordonnees = acoordonnees       # Liste des xi
        self.fenetres = afenetres             # Fenêtres de recherche pour chaque xi
        self.codage = acodage                 
        self.binaire = None                  # Codage binaire
        self.performance = None              # Valeur de f(x)
        
    def evaluer(self, fonction_objectif):
        """Calcule et stocke la performance de l'individu."""
        self.performance = fonction_objectif(self.coordonnees)
        return self.performance 
  
    def muter(self, taux_mutation):
        if self.codage and self.binaire:
            # Mutation sur le code binaire
            self.binaire = self.codage.mutation(self.binaire, taux_mutation)
            # Mettre à jour les coordonnées réelles
            self.coordonnees = self.codage.decoder(self.binaire)
        else:
            # Mutation classique sur les coordonnées réelles
            for i, (xmin, xmax) in enumerate(self.fenetres):
                if random.random() < taux_mutation:
                    amplitude = (xmax - xmin) * 0.1
                    self.coordonnees[i] += random.uniform(-amplitude, amplitude)
                    self.coordonnees[i] = max(min(self.coordonnees[i], xmax), xmin)
                    
    def croiser(self, parent1, parent2):
        if parent1.codage and parent1.binaire and parent2.binaire:
            # Croisement sur le code binaire
            enfant1_binaire, enfant2_binaire = parent1.codage.croiser(parent1.binaire, parent2.binaire)
            e1 = Individu(parent1.codage.decoder(enfant1_binaire), parent1.fenetres, parent1.codage)
            e1.binaire = enfant1_binaire
            e2 = Individu(parent2.codage.decoder(enfant2_binaire), parent2.fenetres, parent2.codage)
            e2.binaire = enfant2_binaire
            return e1, e2
        else:
            # Croisement sur les coordonnées réelles (ton code actuel)
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

    def encoder(self):
        if self.codage:
            self.binaire = self.codage.encoder(self.coordonnees)

    def decoder(self):
        if self.codage and self.binaire:
            self.coordonnees = self.codage.decoder(self.binaire)
            
    def __repr__(self):
        """ Pour faciliter le debogage et l'affichage d'un individu. """
        return f"Individu(coordonnees={self.coordonnees}, perf={self.performance})"


if __name__ == '__main__':

    # Définir une fonction objectif simple
    def fonction_test(x):
        # Exemple : on veut minimiser f(x1, x2) = x1² + x2²
        return x[0]**2 + x[1]**2

    # Définir la fenêtre de recherche pour chaque coordonnée
    fenetres = [(-5, 5), (-5, 5)]

    # Créer un individu aléatoire
    coordonnees = [random.uniform(-5, 5) for _ in range(2)]
    ind = Individu(coordonnees, fenetres)  

    # Évaluer l’individu
    print("Avant mutation :", ind)
    ind.evaluer(fonction_test)
    print("Performance :", ind.performance)

    # Appliquer une mutation
    ind.muter(taux_mutation=0.5)
    print("Après mutation :", ind)