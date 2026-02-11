# A* Pathfinding sur Grille (multi-buts + diagonales)

Projet Python d’implémentation de l’algorithme **A\*** (A-star) pour trouver un chemin optimal sur une **grille** avec obstacles, en autorisant les déplacements **horizontaux/verticaux** et **diagonaux** (coût différent).

## Fonctionnalités
- Recherche de chemin avec **A\*** sur une grille
- Gestion de **plusieurs buts** : l’algorithme s’arrête dès qu’il atteint un des buts
- Déplacements 8-directions :
  - Horizontal/Vertical : coût `1`
  - Diagonal : coût `1.5`
- Heuristique : **distance de Manhattan** (minimale) vers l’ensemble des buts

## Structure du code
- `Case` : représente une cellule (position, coût `g`, heuristique `h`, parent)
- `a_star(grille, start, buts, heuristic_func)` : exécute A* et renvoie `(chemin, coût)`
- `get_neighbors(case, grille)` : génère les voisins (8 directions) et calcule le coût
- `heuristic(case, buts)` : Manhattan vers le but le plus proche
- `main()` : exécute l’algorithme sur plusieurs instances

## Prérequis
- Python 3.8+
- Le fichier dépend d’un module externe :
  - `a_star_grille_etu.py` (fonctions attendues : `lecture_instance(...)` et éventuelles fonctions utilitaires)

## Données d’entrée (instances)
Le programme s’appuie sur des fichiers d’instances (exemples) :
- `instance1.txt`
- `instance2.txt`
- `instance3.txt`
- `instance4.txt`

Chaque instance doit permettre à `lecture_instance(nom_fichier)` de retourner :
- `grille` : matrice 2D (0 = libre, 1 = obstacle)
- `buts` : liste de positions cibles `[(x1,y1), (x2,y2), ...]`

Le départ est fixé à `(0, 0)` dans `main()`.

## Exécution
1) Place ce fichier et `a_star_grille_etu.py` dans le même dossier  
2) Ajoute les fichiers `instance*.txt`  
3) Lance :

```bash
python main.py
