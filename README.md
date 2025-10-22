# Algo-genetique


Pour cloner le repo, créer un dossier où le mettre, déplacer vous dans le dossier puis : git clone https://github.com/cloeithr/Algo-genetique.git

Ensuite pour ajouter un dossier/fonctionnalité au projet il faut créer une branche avec : git switch --create NomDeLaBranche Puis vous pouvez travailler depuis cette branche. Commandes importantes :

.git status : permet de voir tous les dossiers modifiés depuis le dernier commit

.git add . : permet d'ajouter dans le commit toutes les modifications vues dans le git status

.git commit : permet de sauvegarder sur votre branche locale les modifications ajoutées par le git add

.git push -u NomDeLaBranche : permet de d'ajouter votre branche au repo en ligne (sur github)




# Algorithme Génétique – Conception Orientée Objet (POO)

## Objectif du projet

Ce projet a pour but de **concevoir et programmer un algorithme génétique complet** en **programmation orientée objet (POO)**.
L’idée est de reproduire le **principe de l’évolution naturelle** :
sélection, croisement, mutation et adaptation d’une population d’individus afin d’optimiser une fonction donnée.

Le projet vise à obtenir une architecture **claire, modulaire et réutilisable**, dans laquelle chaque composant (codage, opérateur, évaluation…) peut être **interchangé sans modifier le reste du code**.


##  Principe général

| Concept biologique  | Équivalent informatique       |
| ------------------- | ----------------------------- |
| ADN                 | Génome binaire                |
| Individu            | Solution candidate            |
| Population          | Ensemble de solutions         |
| Sélection naturelle | Choix des meilleurs individus |
| Croisement          | Mélange des gènes             |
| Mutation            | Perturbation aléatoire        |
| Évolution           | Amélioration successive       |


##  Étapes principales de l’algorithme

### 1️ Choix du codage

* Chaque individu possède un **codage propre**, par exemple en **mantisse/exposant binaire**.
* Ce codage définit comment les coordonnées réelles sont converties en bits et inversement.
* Un individu doit **savoir se coder et se décoder lui-même**.
* Si la méthode de codage n’est pas implémentée, le programme doit signaler une erreur (`NotImplementedError`).



### 2️ Définition des paramètres de base

* **Taille de la population** : 50 individus.
* **Taux de mutation** : à ajuster (inspiré de la biologie).
* **Type d’objectif** :

  * Minimisation : `+1 × f(x1, x2, …)`
  * Maximisation : `−1 × f(x1, x2, …)`
* **Fonction de performance (benchmark)** : parabole, sphère, rastrigin, etc.
* **Fenêtres de recherche** : chaque coordonnée `xi` a une borne `[min, max]`.



### 3 Génération de la population initiale

* La population est générée **aléatoirement mais de façon équirépartie** dans l’espace de recherche (méthode Latin Hypercube).
* Chaque individu est constitué de plusieurs coordonnées (`x1, x2, x3…`), chacune ayant sa **fenêtre de recherche**.
* Ainsi, si on est en dimension 4, l’individu aura 4 coordonnées, chacune avec ses propres bornes min et max.



### 4️ Boucle principale de l’évolution

####  Étape 1 : Sélection

* Deux individus sont choisis pour se reproduire (père et mère).
* Méthode utilisée : **Roue de la Fortune** (*Roulette Wheel Selection*).
* Plus un individu est performant, plus il a de chances d’être choisi.
   **Attention** : ne pas rendre la sélection trop déterministe pour préserver la diversité.

####  Étape 2 : Croisement

* On effectue un **croisement multipoint** entre les deux parents.
* On choisit un nombre fini de points de coupure et on échange les segments.
* Le résultat donne **deux enfants** (E1, E2).
   Il faut bien gérer l’ordre des coupures pour éviter les erreurs.

####  Étape 3 : Mutation

* Chaque enfant subit une **mutation aléatoire** selon un taux donné.
* Exemple : inversion de bits (0 ↔ 1).
* Cela introduit de la **variabilité génétique**, essentielle pour explorer d’autres zones de l’espace de recherche.

####  Étape 4 : Évaluation

* Chaque individu (parents et enfants) est évalué selon la **fonction de performance**.
* On obtient une **valeur de performance (fitness)**.

####  Étape 5 : Remplacement

* On choisit **2 individus parmi 4** (Père, Mère, Enfant1, Enfant2) pour les conserver dans la population.
* On évite tout **remplacement systématique** afin de limiter le déterminisme.
* Le remplacement doit toujours préserver la taille totale de la population.

####  Étape 6 : Test de dégénérescence

* Une **population dégénérée** est une population qui n’évolue plus (stagnation).
* On le détecte via la **courbe de convergence** (le meilleur individu ne s’améliore plus).
* Dans ce cas, on :

  * garde le **meilleur individu** et quelques bons éléments (ex. 10/50),
  * **régénère aléatoirement** le reste pour redonner de la diversité.



##  Architecture orientée objet

### Classes principales

| Classe                         | Rôle                                                             |
| ------------------------------ | ---------------------------------------------------------------- |
| **Fenêtre**                    | Définit les bornes min et max d’une coordonnée.                  |
| **Coordonnée** *(optionnelle)* | Représente une composante de l’individu dans la fenêtre.         |
| **Individu**                   | Représente une solution candidate ; sait se coder et se décoder. |
| **Population**                 | Contient l’ensemble des individus et leurs performances.         |
| **AlgorithmeGénétique**        | Coordonne les opérateurs et les générations successives.         |



### Interfaces abstraites

| Interface                    | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| **StratégieCodage**          | Définit les méthodes de codage/décodage des coordonnées.     |
| **OpérateurÉvaluation**      | Définit la fonction de performance à optimiser.              |
| **OpérateurSélection**       | Définit la méthode de sélection (roue, tournoi…).            |
| **OpérateurCroisement**      | Définit comment croiser deux individus.                      |
| **OpérateurMutation**        | Définit comment appliquer une mutation.                      |
| **OpérateurRemplacement**    | Définit la stratégie de remplacement (2 parmi 4, élitisme…). |
| **DétecteurDégénérescence**  | Détecte si la population stagne.                             |
| **RéinitialiseurPopulation** | Régénère une partie des individus en cas de stagnation.      |


###  Implémentations concrètes

| Classe                          | Type                     | Fonction                                                  |
| ------------------------------- | ------------------------ | --------------------------------------------------------- |
| **CodageMantisseExposant**      | StratégieCodage          | Représente le codage binaire (signe, exposant, mantisse). |
| **ÉvaluationParabole**          | OpérateurÉvaluation      | Fonction `f(x) = Σ xᵢ²` (minimisation).                   |
| **SélectionRoulette**           | OpérateurSélection       | Sélection par roue de la fortune.                         |
| **CroisementMultipoint**        | OpérateurCroisement      | Mélange des gènes sur plusieurs coupures.                 |
| **MutationBitAléatoire**        | OpérateurMutation        | Inversion aléatoire de bits.                              |
| **RemplacementDeuxParmiQuatre** | OpérateurRemplacement    | Garde les deux meilleurs individus parmi quatre.          |
| **DétectionPlateau**            | DétecteurDégénérescence  | Détecte les plateaux de performance.                      |
| **RéinitialisationÉlitiste**    | RéinitialiseurPopulation | Garde les meilleurs + crée des individus aléatoires.      |



##  Points essentiels et précautions

*  **Éviter le déterminisme** : toujours laisser une part de hasard dans la sélection et le remplacement.
*  **Maintenir la diversité génétique** : ne pas reproduire uniquement les meilleurs.
*  **Surveiller la précision du codage** : elle influence la qualité de la performance.
*  **Fenêtres de recherche** : doivent permettre à l’algorithme de converger vers la solution optimale.
*  **Préserver la modularité** : tout opérateur ou fonction peut être remplacé sans casser le code.




##  Interprétation de la convergence

La **courbe de convergence** montre la performance du meilleur individu au fil des générations.
Un **palier horizontal** indique une stagnation → il faut alors réinitialiser une partie de la population.



##  Schéma simplifié de l’architecture objet

```
┌────────────────────────────┐
│     AlgorithmeGénétique    │
├────────────────────────────┤
│ - population               │
│ - opérateurs               │
│ - paramètres               │
└──────────┬─────────────────┘
           │
   ┌───────┼──────────────────────────────┐
   ▼                                      ▼
Population                         Opérateurs
│                                      │
├── contient → Individus                ├── Sélection / Mutation / Croisement
│                                      ├── Remplacement / Évaluation
└──────────────────────────────────────┘
```


##  Table UML – Relations entre classes et interfaces

| Classe source           | Relation | Classe cible                 | Type        |
| ----------------------- | -------- | ---------------------------- | ----------- |
| **AlgorithmeGénétique** | contient | **Population**               | Composition |
| **Population**          | contient | **Individu**                 | Agrégation  |
| **Individu**            | utilise  | **StratégieCodage**          | Association |
| **Population**          | utilise  | **OpérateurÉvaluation**      | Association |
| **AlgorithmeGénétique** | utilise  | **OpérateurSélection**       | Association |
| **AlgorithmeGénétique** | utilise  | **OpérateurCroisement**      | Association |
| **AlgorithmeGénétique** | utilise  | **OpérateurMutation**        | Association |
| **AlgorithmeGénétique** | utilise  | **OpérateurRemplacement**    | Association |
| **AlgorithmeGénétique** | utilise  | **DétecteurDégénérescence**  | Association |
| **AlgorithmeGénétique** | utilise  | **RéinitialiseurPopulation** | Association |




##  Pistes d’amélioration

* Implémenter d’autres fonctions de performance (Rastrigin, Ackley, Rosenbrock…).
* Ajouter la **sélection par tournoi**.
* Créer une **mutation gaussienne** pour les variables réelles.
* Intégrer une **visualisation de la convergence** avec Matplotlib.
* Permettre la **sauvegarde automatique** du meilleur individu à chaque génération.


