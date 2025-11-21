"""
Classe : MantisseExposant
Module : MantisseExposant.py
Description :
    Implémente une stratégie de codage basée sur la représentation
    mantisse + exposant (structure préparée pour de futurs travaux).
"""

from StrategieCodage import StrategieCodage


class MantisseExposant(StrategieCodage):
    """
    Codage Mantisse + Exposant.
    Cette classe respecte l'interface mais laisse les méthodes
    à implémenter plus tard (méthodes "non implémentées").
    """

    def __init__(self):
        """Constructeur vide pour le moment."""
        pass

    def encoder(self, aCoordonnees):
        """
        Encode une liste de valeurs réelles en mantisse/exposant.
        NON IMPLÉMENTÉ va génèrer une erreur volontaire.
        """
        raise NotImplementedError(
            "La méthode encoder() n'est pas encore implémentée dans MantisseExposant."
        )

    def decoder(self, aCode):
        """
        Décode un code mantisse/exposant en valeurs réelles.
        NON IMPLÉMENTÉ va génèrer une erreur volontaire.
        """
        raise NotImplementedError(
            "La méthode decoder() n'est pas encore implémentée dans MantisseExposant."
        )



#TEST LOCAL 

if __name__ == "__main__":
    print(" Test de la classe MantisseExposant")

    m = MantisseExposant()

    print("Test encodage (doit lever une erreur volontaire) :")
    try:
        m.encoder([1.2, 3.4])
    except NotImplementedError as e:
        print("Erreur capturée :", e)

    print("\nTest décodage (doit lever une erreur volontaire) :")
    try:
        m.decoder("1010101")
    except NotImplementedError as e:
        print("Erreur capturée :", e)
