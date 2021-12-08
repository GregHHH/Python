import numpy as np
import random
import sys

def generate(lin, col, density):
 
    
    
    nbr_1 = int((lin * col) * (density / 100))
    nbr_0 = int((lin * col) - nbr_1)
    grid = int(nbr_1)*[1] + int(nbr_0)*[0]
    random.shuffle(grid)
    grid = np.reshape(grid, (lin, col))
    print(grid)
   
#TODO
# génerer un certain pourcentage de 1 dans la grille.

# Parcourir le tableau, à enlever plus tard ou à adapter pour la géneration
    # for i in range(1, lin-1):
    #     for j in range(1, col-1):
    #         r = random.randint(1, 101)
    #         if r <= density:
    #             grid[i][j] = 1
     # compteur pour ne pas depasser la densité

    np.savetxt("array.txt", grid, fmt="%s")
#-----------------------------------------------------------------------------------------

nbr_line = int(sys.argv[2]) if len(sys.argv) >= 2 else int(6)
nbr_column = int(sys.argv[2]) if len(sys.argv) >= 3 else int(6)
density = int(sys.argv[2]) if len(sys.argv) >= 4 else int(15)
generate(nbr_line, nbr_column, density)