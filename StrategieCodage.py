"""
Classe : StrategieCodage
Module : StrategieCodage.py
Description :
    Interface abstraite définissant les méthodes de codage/décodage
    nécessaires pour tout type de représentation d'un individu
    (ex : codage binaire, codage mantisse/exposant, codage réel…).
"""

from abc import ABC, abstractmethod


class StrategieCodage(ABC):
    """
    Classe abstraite pour toutes les stratégies de codage.
    Toute classe fille doit implémenter :
      - encoder(coordonnees)
      - decoder(code)
    """

    @abstractmethod
    def encoder(self, aCoordonnees):
        """
        Encode une liste de valeurs réelles en une représentation interne.
        Exemple : convertir [x1, x2] en un code binaire.
        """
        pass

    @abstractmethod
    def decoder(self, aCode):
        """
        Décode une représentation interne vers une liste de valeurs réelles.
        Exemple : convertir un code binaire vers [x1, x2].
        """
        pass



# TEST LOCAL

if __name__ == "__main__":
    print("=== Test de la classe StrategieCodage ===")

    # Exemple de classe fille "bouchon" juste pour le test
    class CodageIdentite(StrategieCodage):
        """Codage trivial : encode = decode = identique"""
        def encoder(self, aCoordonnees):
            return aCoordonnees

        def decoder(self, aCode):
            return aCode

    cod = CodageIdentite()
    print("Encodage :", cod.encoder([1.5, -2.3]))
    print("Décodage :", cod.decoder([1.5, -2.3]))
