"""
Classe : NomDeClasse
Module : NomDeClasse.py
Description :
    Modèle standard de classe pour le projet d’algorithme génétique.
    Chaque membre du groupe doit respecter cette structure :
    - Docstring claire et complète
    - Constructeur standardisé
    - Méthodes d’action numérotées (action01, action02, ...)
    - Méthode __str__() pour l’affichage
    - Zone de test local en bas du fichier
"""

# =====================================================
#  Importations (uniquement si nécessaires)
# =====================================================
# Exemple :
# import random
# from AutreModule import AutreClasse


# =====================================================
#  Définition de la classe
# =====================================================
class NomDeClasse:
    """Brève description de la classe (une ligne)."""

    # -------------------------------------------------
    # Constructeur
    # -------------------------------------------------
    def __init__(self, aParametre01, aParametre02=None):
        """
        Constructeur de la classe.
        :param aParametre01: description du premier paramètre
        :param aParametre02: description du second paramètre
        """
        self.parametre01 = aParametre01  # attributs en minuscules
        self.parametre02 = aParametre02  # pluriel si liste

    # -------------------------------------------------
    # Méthodes d’action
    # -------------------------------------------------
    def action01_nom_action(self):
        """Première action réalisée par la classe."""
        print("→ Action 01 exécutée")

    def action02_nom_action(self):
        """Deuxième action (exemple)."""
        pass

    # -------------------------------------------------
    # Méthode d’affichage
    # -------------------------------------------------
    def __str__(self):
        """Retourne une représentation lisible de l’objet."""
        return f"NomDeClasse(parametre01={self.parametre01}, parametre02={self.parametre02})"


# =====================================================
#  Exemple concret : Classe Coordonnees
# =====================================================
"""
# Exemple d’application du modèle :

class Coordonnees:
    '''Représente une coordonnée d’un individu dans une dimension donnée.'''

    def __init__(self, aValeurInitiale, aFenetre):
        '''
        :param aValeurInitiale: valeur réelle initiale
        :param aFenetre: objet Fenetre définissant les bornes min et max
        '''
        self.valeur = aValeurInitiale
        self.fenetre = aFenetre

    def action01_muter(self, amplitude):
        '''Fait varier la coordonnée d’une petite valeur aléatoire dans les bornes.'''
        import random
        delta = random.uniform(-amplitude, amplitude)
        nouvelle_valeur = self.valeur + delta
        # on vérifie qu’on reste dans les bornes
        if nouvelle_valeur < self.fenetre.min: nouvelle_valeur = self.fenetre.min
        if nouvelle_valeur > self.fenetre.max: nouvelle_valeur = self.fenetre.max
        print(f"→ Coordonnée modifiée : {self.valeur:.3f} → {nouvelle_valeur:.3f}")
        self.valeur = nouvelle_valeur

    def __str__(self):
        return f"Coordonnee(valeur={self.valeur:.3f}, min={self.fenetre.min}, max={self.fenetre.max})"
"""


# =====================================================
#  Zone de test local
# =====================================================
if __name__ == "__main__":
    print("=== Test du modèle de classe ===")
    exemple = NomDeClasse(aParametre01="test", aParametre02=10)
    print(exemple)
    exemple.action01_nom_action()
import Performance
print(Performance.__file__)
