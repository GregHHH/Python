from generate import *

# Tableau de jeu
""" frame = np.array([
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]])
 """
def compute_number_neighbors(paded_frame, index_line, index_column):
	number_neighbors = 0
	for i in range(index_line - 1, index_line + 2):
		for j in range(index_column - 1, index_column + 2):
				number_neighbors = number_neighbors + frame[i][j]
	number_neighbors = number_neighbors - paded_frame[index_line][index_column]
	return number_neighbors

def compute_next_frame (frame):
	paded_frame = np.pad(frame, 1, mode='constant')
	return paded_frame

def copy_with_rules(frame):
	
	size_lin = len(frame)
	size_col = len(frame[0])
	cp_frame = np.empty((size_lin, size_col), int)
 # TODO: quelque chose louche avec size: IndexError: index 10 is out of bounds for axis 0 with size 10
 #TODO: les bordures disparaissent lors de l'utilisation d'une grille :((((((
	for i in range(1, size_lin - 1 ):
		for j in range(1, size_col - 1 ):
			# On applique les règles du Jeu de la Vie
			if frame[i][j] == 0 and compute_number_neighbors(frame, i, j) == 3:
				cp_frame[i][j] = 1
			elif frame[i][j] == 1 and (compute_number_neighbors(frame, i, j) == 2 or compute_number_neighbors(frame, i, j) == 3):
				cp_frame[i][j] = 1
			else:
				cp_frame[i][j] = 0
	return cp_frame

#TODO: Probleme avec les itération 1 sur 2 (souvent mais pas toujours) :nombres random (semble lié à pygame, quand include present, bug, sinon affichage normal.) 
#TODO: Verif avec les cellules qui prennent vie dans la bordure : disparition de la figure :( (encore  incrémenter la taille de la bordure à ce moment ?)


size_lin = len(frame)
# size_lin = int(sys.argv[2]) if len(sys.argv) >= 2 else int(6)
size_col = len(frame[0])
# size_col = int(sys.argv[2]) if len(sys.argv) >= 3 else int(6)

#density = int(sys.argv[2]) if len(sys.argv) >= 4 else int(15)
# frame = generate(size_lin, size_col, density)
# frame = compute_next_frame(frame)
i = 0
frame = compute_next_frame(frame)

while True:
	os.system('clear')
	print(frame)
	print(i)
	i += 1
	time.sleep(0.2)
	frame = copy_with_rules(frame)
