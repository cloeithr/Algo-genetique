"""
Classe : StrategieCodage
Module : StrategieCodage.py
Description :
    Classe abstraite qui définit l’interface pour les différentes stratégies de codage
    des individus (ex : binaire, mantisse/exposant, réel…).
"""

from abc import ABC, abstractmethod

class StrategieCodage(ABC):
    """Interface de base pour toutes les stratégies de codage."""

    @abstractmethod
    def encoder(self, valeur):
        """Encode une valeur réelle en représentation interne (ex : binaire)."""
        pass

    @abstractmethod
    def decoder(self, code):
        """Décode une représentation interne vers une valeur réelle."""
        pass



# Test local

if __name__ == "__main__":
    print("=== Test de la classe abstraite StrategieCodage ===")

    # Exemple temporaire (bouchon)
    class CodageReel(StrategieCodage):
        def encoder(self, valeur): return valeur
        def decoder(self, code): return code

    codage = CodageReel()
    print("Encodage 5.2 ->", codage.encoder(5.2))
    print("Décodage 5.2 ->", codage.decoder(5.2))