
import numpy as np


def lecture_instance(nom_fichier):
	try:
		f = open("Instances/" + nom_fichier, "r")
		grille = {}
		buts = []
		nb_lig = int(f.readline())
		nb_col = int(f.readline())
		for i in range(nb_lig):
			grille[i] = []
			line = f.readline()
			line = line.split(" ")
			for j in range(nb_col):
				grille[i].append(int(line[j]))
				if grille[i][j] == 2:
					buts.append((i, j))
		f.close()
		return grille, buts
	except FileNotFoundError:
		print("File not found")
		return 1, 1





if __name__ == '__main__':
	grille, buts = lecture_instance("instance5.txt")
	# chemin, cout = a_star(grille, len(grille), len(grille[0]), buts)
	# print(cout, chemin)
