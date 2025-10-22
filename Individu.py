import random

class Individu: 
    def __init__(self, coordonnees, fenetres, codage=None):
        self.coordonnees = coordonnees       # Liste des xi
        self.fenetres = fenetres             # Fenêtres de recherche pour chaque xi
        self.codage = codage                 
        self.binaire = None                  # Codage binaire
        self.performance = None              # Valeur de f(x)
        
    def evaluer(self, fonction_objectif):
        """Calcule et stocke la performance de l'individu."""
        self.performance = fonction_objectif(self.coordonnees)
        return self.performance 
  
    def muter(self, taux_mutation):
        """Applique une mutation aléatoire sur chaque coordonnée selon un taux."""
        for i, (xmin, xmax) in enumerate(self.fenetres):
            if random.random() < taux_mutation:
                # On ajoute un bruit proportionnel à la taille de la fenêtre
                amplitude = (xmax - xmin) * 0.1
                self.coordonnees[i] += random.uniform(-amplitude, amplitude)
                # On garde la coordonnée dans les bornes
                self.coordonnees[i] = max(min(self.coordonnees[i], xmax), xmin)

    def encoder(self):
        """Transforme les coordonnées réelles en code binaire."""
        pass  # à implémenter plus tard quand on aura avancé

    def decoder(self):
        """Transforme le code binaire en coordonnées réelles."""
        pass  # à implémenter plus tard quand on aura avancé
    
    def __repr__(self):
        """ Pour faciliter le debogage et l'affichage d'un individu. """
        return f"Individu(coordonnees={self.coordonnees}, perf={self.performance})"


# Test de la classe pour voir si ça fonctionne

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


