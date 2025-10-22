# ===============================
#  Fichier : Performance.py
#  Auteur  : Mouna BENSAID
#  Rôle    : Calcul de la performance (fitness) d’un individu
#  ===============================

from Parabole import Parabole

class Performance:
    """Évalue la performance d’un individu avec la fonction Parabole."""

    FACTEUR_OBJECTIF = 1  # +1 = minimisation | -1 = maximisation

    @staticmethod
    def evaluer(individu):
        """Retourne la performance d’un individu et la stocke dans l’objet."""
        coordonnees = individu.decode()
        valeur = Parabole.evaluate(coordonnees)
        performance = Performance.FACTEUR_OBJECTIF * valeur
        individu.performance = performance
        return performance
