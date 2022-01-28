import pygame as pg
import numpy as np
import random 
import time
import sys
import os

def generate(lin, col, density):
    nbr_1 = int((lin * col) * (density / 100))
    nbr_0 = int((lin * col) - nbr_1)
    grid = int(nbr_1)*[1] + int(nbr_0)*[0]
    random.shuffle(grid)
    grid = np.reshape(grid, (lin, col))
    np.savetxt("array.txt", grid, fmt="%s")
    return grid

#TODO
# génerer un certain pourcentage de 1 dans la grille.

# Parcourir le tableau, à enlever plus tard ou à adapter pour la géneration
    # for i in range(1, lin-1):
    #     for j in range(1, col-1):
    #         r = random.randint(1, 101)
    #         if r <= density:
    #             grid[i][j] = 1
     # compteur pour ne pas depasser la densité

    
#-----------------------------------------------------------------------------------------
