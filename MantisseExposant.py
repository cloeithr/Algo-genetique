from StrategieCodage import StrategieCodage


class MantisseExposant(StrategieCodage):
    """Classe MantisseExposant héritant de StrategieCodage."""

    def __init__(self):
        """Constructeur de la classe MantisseExposant."""
        super().__init__()  # Appel du constructeur parent

    def encoder(self, aValeur):
        """Méthode d'encodage (sera implémentée plus tard)."""
        self.valeur= aValeur
        pass

    def decoder(self, aCode):
        """Méthode de décodage (sera implémentée plus tard)."""
        self.code= aCode
        pass
#  Test local

if __name__ == "__main__":
    print("=== Test de la classe MantisseExposant ===")
    codeur = MantisseExposant()
    print("Encodage test :", codeur.encoder(5.2))
    print("Décodage test :", codeur.decoder("101010"))
