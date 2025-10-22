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
        # Si codage binaire présent, muter le binaire
        if self.codage and self.binaire:
            self.binaire = self.codage.mutation(self.binaire, taux_mutation)
            self.coordonnees = self.codage.decoder(self.binaire)
        else:
            # Mutation classique sur les réels
            for i, (xmin, xmax) in enumerate(self.fenetres):
                if random.random() < taux_mutation:
                    amplitude = (xmax - xmin) * 0.1
                    self.coordonnees[i] += random.uniform(-amplitude, amplitude)
                    self.coordonnees[i] = max(min(self.coordonnees[i], xmax), xmin)

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
