from Population import Population
from Fenetre import Fenetre
from Performance import Performance

# exécution de la première fonction
fenetres = [Fenetre("x", 0, 500), Fenetre("y", 0, 500)]

pop = Population(
    aTaille=50,
    aFenetres=fenetres,
    aFonctionObjectif=Performance.schaffer 
)

pop.initialiser()
pop.evaluer()

print("Meilleur individu :", pop.meilleur())
