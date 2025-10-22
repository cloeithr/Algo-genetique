
#  Classe : Performance
#  Module : Performance.py
#  Description :
#      Évalue la performance (fitness) d’un individu à partir
#      d’une fonction objectif donnée (ici : Parabole).


from Parabole import Parabole


class Performance:
    """Classe utilitaire pour évaluer la performance (fitness) d'un individu."""

    # +1 = minimisation, -1 = maximisation
    FACTEUR_OBJECTIF = 1  

    @staticmethod
    def evaluer(individu):
        """
        Calcule et attribue la performance d'un individu.
        Utilise la fonction Parabole pour évaluer la qualité de ses coordonnées.
        """
        # Récupération des coordonnées décodées de l’individu
        try:
            coordonnees = individu.decode()
        except AttributeError:
            # Si l’individu ne possède pas de méthode decode(), on prend directement les coordonnées
            coordonnees = individu.coordonnees

        # Évaluation via la fonction Parabole (fonction objectif)
        valeur = Parabole.evaluate(coordonnees)

        # Calcul de la performance (selon minimisation ou maximisation)
        performance = Performance.FACTEUR_OBJECTIF * valeur

        # On stocke la performance directement dans l’individu
        individu.performance = performance

        return performance


  
# TEST LOCAL
  
if __name__ == "__main__":
    print("=== Test local de la classe Performance ===")

    # Classe Parabole simulée pour le test (f(x, y) = x² + y²)
    class Parabole:
        @staticmethod
        def evaluate(coordonnees):
            x, y = coordonnees
            return x**2 + y**2

    # Classe Individu simulée
    class Individu:
        def __init__(self, coordonnees):
            self.coordonnees = coordonnees
            self.performance = None

        def decode(self):
            return self.coordonnees

        def __str__(self):
            return f"Individu(coordonnees={self.coordonnees}, performance={self.performance})"

    # Test
    individu_test = Individu((3, 4))
    perf = Performance.evaluer(individu_test)
    print(f"Valeur de la performance : {perf}")
    print(f"Individu après évaluation : {individu_test}")
