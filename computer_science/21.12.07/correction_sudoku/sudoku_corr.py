import numpy as np

class SudokuSolver:
	
	def __init__(self,grid):
		self.grid = grid


	def __str__(self):
		return f"La réponse est:\n{self.grid}"


	def modify_grid(self):
		self.grid[0][0] = 5


	def empty_cells(self):
		nbr_lin = self.grid.shape[0]
		nbr_col = self.grid.shape[1]
		for index_lin in range(0, nbr_lin):
			for index_col in range(0, nbr_col):
				
				if (self.grid[index_lin][index_col] == 0):
					print(f"La cellule {index_lin}, {index_col} est vide.")


	