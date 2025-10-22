import random
from Fenetre import Fenetre

class Coordonnee:
    """Représente une variable réelle dans son domaine de recherche (fenêtre)."""
    def __init__(self, anom: str, afenetre: Fenetre):
        self.nom = anom
        self.fenetre = afenetre
        self.valeur = self.fenetre.generer_valeur()

    def muter(self, taux_mutation: float):
        """Fait varier légèrement la valeur selon un taux de mutation."""
        if random.random() < taux_mutation:
            amplitude = (self.fenetre.borne_max - self.fenetre.borne_min) * 0.1
            delta = random.uniform(-amplitude, amplitude)
            nouvelle_valeur = self.valeur + delta
            # On reste dans la fenêtre
            self.valeur = max(self.fenetre.borne_min, min(nouvelle_valeur, self.fenetre.borne_max))

    def generer_aleatoire(self):
        """Génère une nouvelle valeur aléatoire dans la fenêtre."""
        self.valeur = self.fenetre.generer_valeur()

    def __repr__(self):
        return f"{self.nom}={self.valeur:.3f}"

#Test Local
if __name__ == "__main__":
    f = Fenetre("x1", -10, 10)
    c = Coordonnee("x1", f)
    print("Coordonnée initiale :", c)
    c.muter(0.5)
    print("Après mutation :", c)
