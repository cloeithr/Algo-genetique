from Fenetre import Fenetre
from Coordonnee import Coordonnee

if __name__ == "__main__":
    f1 = Fenetre("x1", -5, 5)
    f2 = Fenetre("x2", 0, 10)

    c1 = Coordonnee("x1", f1)
    c2 = Coordonnee("x2", f2)

    print("Avant mutation :", c1, c2)
    c1.muter(0.5)
    c2.muter(0.5)
    print("Après mutation :", c1, c2)

