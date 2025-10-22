import random

class Coordonnee:
    def __init__(self, nom: str, fenetre: Fenetre):
        self.nom = nom
        self.fenetre = fenetre
        self.valeur = self.fenetre.generer_valeur()

    def muter(self, taux_mutation: float):
        if random.random() < taux_mutation:
            amplitude = (self.fenetre.borne_max - self.fenetre.borne_min) * 0.1
            delta = random.uniform(-amplitude, amplitude)
            nouvelle_valeur = self.valeur + delta
            # On reste dans la fenêtre
            self.valeur = max(self.fenetre.borne_min, min(nouvelle_valeur, self.fenetre.borne_max))

    def generer_aleatoire(self):
        self.valeur = self.fenetre.generer_valeur()

    def __repr__(self):
        return f"{self.nom}={self.valeur:.3f}"
