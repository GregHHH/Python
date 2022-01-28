from generate import *

import pygame as pg
import numpy as np
import sys

array = np.array([
		[1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0],
		[0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0, 0]])


def compute_number_neighbors(paded_frame, index_line, index_column):
	number_neighbors = 0
	for i in range(index_line - 1, index_line + 2):
		for j in range(index_column - 1, index_column + 2):
				number_neighbors += paded_frame[i][j]
	number_neighbors -= paded_frame[index_line][index_column]
	return number_neighbors

def add_padding (frame):
	paded_frame = np.pad(frame, 1, mode='constant')
	return paded_frame

def copy_with_rules(array):
	size_lin = len(array)
	size_col = len(array[0])
	cp_array = np.zeros((size_lin, size_col), int)
 	
	# TODO: toute la grille n'est pas visitée à cause du -1 (bordures)
	for i in range(1, size_lin - 1):
		for j in range(1, size_col - 1):
			# On applique les règles du Jeu de la Vie
			number_neighbors = compute_number_neighbors(array, i, j)
			if array[i][j] == 0 and number_neighbors == 3:
				cp_array[i][j] = 1
			elif array[i][j] == 1 and (number_neighbors == 2 or number_neighbors == 3):
				cp_array[i][j] = 1
			else:
				continue
	return cp_array

def print_frame(surface):
    screen.fill((30, 30, 30))
    screen.blit(surface, (100, 100))
    pg.display.flip()

# TODO: Verif avec les cellules qui prennent vie dans la bordure : disparition de la figure :( (encore  incrémenter la taille de la bordure à ce moment ?)
size_lin = int(sys.argv[2]) if len(sys.argv) >= 2 else int(6)
size_col = int(sys.argv[2]) if len(sys.argv) >= 3 else int(6)
density = int(sys.argv[2]) if len(sys.argv) >= 4 else int(15)

i = 0
array = generate(size_lin, size_col, density)
array = add_padding(array)

pg.init()
clock = pg.time.Clock()

size_lin = len(array)
size_col = len(array[0])
size_pixel = 30

screen = pg.display.set_mode((800, 800))


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    colors = np.array([[255, 255, 255], [250, 90, 120]])
    surface = pg.surfarray.make_surface(colors[array])
    surface = pg.transform.scale(surface, (size_lin * size_pixel, size_col * size_pixel))
    surface = pg.transform.rotate(surface, -90)

    print_frame(surface)
    time.sleep(0.2)
    i+=1
    array = copy_with_rules(array)
    clock.tick(60)
