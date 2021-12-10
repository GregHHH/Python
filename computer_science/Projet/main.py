import numpy as np
import random
import sys

frame = np.array([
		[1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]])

# def generate(lin, col, density):
#  	nbr_1 = int((lin * col) * (density / 100))
#     nbr_0 = int((lin * col) - nbr_1)
#     frame = int(nbr_1)*[1] + int(nbr_0)*[0]
#     random.shuffle(frame)
#     frame = np.reshape(frame, (lin, col))
#     print(frame)

def compute_number_neighbors(paded_frame, index_line, index_column):
	number_neighbors = 0
	for i in range(index_line - 1, index_line + 1):
		for j in range(index_column - 1, index_column + 1):
			if frame[i][j] == 1:
				number_neighbors += number_neighbors
			else:
				continue
	number_neighbors = number_neighbors - paded_frame[index_line][index_column]
	return number_neighbors

def compute_next_frame (frame):
	paded_frame = np.pad(frame, 1, mode='constant')
	return frame


print(frame)
print(compute_number_neighbors(frame,5,6))
frame = compute_next_frame(frame)
	

# valeurs par défaut du tableau: 6x6 avec densité de cellules vivantes de 15%
# nbr_line = int(sys.argv[2]) if len(sys.argv) >= 2 else int(6)
# nbr_column = int(sys.argv[2]) if len(sys.argv) >= 3 else int(6)
# density = int(sys.argv[2]) if len(sys.argv) >= 4 else int(15)
# generate(nbr_line, nbr_column, density)