import heapq
from a_star_grille_etu import *
class Case:
    def __init__(self, position, cost_g=0, cost_h=0, parent=None):
        self.position = position  # Les coordonnées de la cellule sur la grille
        self.cost_g = cost_g      # Le coût du chemin du départ à la cellule
        self.cost_h = cost_h      # Le coût heuristique estimé du nœud au but
        self.parent = parent      # La cellule parent dans le chemin

    def cost_f(self):
        # Le coût total 'f' est la somme du coût réel 'g' et du coût heuristique 'h'
        return self.cost_g + self.cost_h

    def __lt__(self, other):
        # Définir une comparaison pour que heapq puisse ordonner les Cases
        return self.cost_f() < other.cost_f()

# Ajoutons maintenant l'utilisation de la classe Case dans a_star
def a_star(grille, start, buts, heuristic_func):
    print("buts : ",buts)
    start_case = Case(start, cost_g=0, cost_h=heuristic_func(Case(start), buts))
    
    open_set = []
    heapq.heappush(open_set, start_case)
    came_from = {start: None}
    g_score = {start: 0}

    while open_set:
        current_case = heapq.heappop(open_set)

        if current_case.position in buts:
            return reconstruct_path(came_from, current_case), current_case.cost_g

        for neighbor_case in get_neighbors(current_case, grille):
            if neighbor_case.position in g_score and g_score[neighbor_case.position] <= neighbor_case.cost_g:
                continue

            if neighbor_case.cost_g < g_score.get(neighbor_case.position, float('inf')):
                came_from[neighbor_case.position] = current_case
                g_score[neighbor_case.position] = neighbor_case.cost_g
                heapq.heappush(open_set, neighbor_case)

    return None, float('inf')  # Si aucun chemin n'est trouvé

# La fonction reconstruct_path devrait aussi être mise à jour pour travailler avec des objets Case.
def reconstruct_path(came_from, end_case):
    path = []
    current_case = end_case
    while current_case in came_from:
        path.append(current_case.position)
        current_case = came_from[current_case]
    path.reverse()  # Inverse le chemin car on l'a reconstruit à l'envers
    return path


def get_neighbors(case, grille):
    neighbors = []
    (x, y) = case.position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Verticalement et horizontalement
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonalement
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]) and grille[nx][ny] != 1:
            move_cost = get_travel_cost(case.position, (nx, ny))
            neighbor_case = Case((nx, ny), case.cost_g + move_cost)
            neighbors.append(neighbor_case)
    return neighbors

def get_travel_cost(current_position, neighbor_position):
    # Calculer si le déplacement est diagonal ou pas
    dx = abs(current_position[0] - neighbor_position[0])
    dy = abs(current_position[1] - neighbor_position[1])
    if dx == 1 and dy == 1:
        return 1.5  # Coût pour le mouvement diagonal
    else:
        return 1    # Coût pour le mouvement horizontal ou vertical

def heuristic(case, buts):
    # case.position donne les coordonnées (x, y) de la case actuelle
    # buts est une liste de tuples représentant les positions des buts
        x, y = case.position
        print("b   ",buts)
        return min(abs(x - bx) + abs(y - by) for (bx, by) in buts)

def main():
    # Supposons que vous avez une fonction heuristic qui est déjà définie.
   
    fichier = ["instance1.txt","instance2.txt","instance2.txt","instance3.txt","instance4.txt",]
    for i in range(0, 5):  # Pour les 5 instances fournies
        nom_fichier = fichier[i]
        grille, buts = lecture_instance(nom_fichier)
        start = (0, 0)  # Point de départ fixé à (0, 0)
        print("main buts : ",buts)
        # Exécutez l'algorithme A* pour trouver le chemin et le coût.
        chemin, cout = a_star(grille, start, buts, heuristic)
        
        # Affichez les résultats pour chaque instance.
        print(f"Pour l'instance {i}, le chemin trouvé est : {chemin} avec un coût de {cout}")

if __name__ == "__main__":
    main()
