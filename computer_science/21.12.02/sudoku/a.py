import numpy as np


class SudokuSolver:
    def __init__(self, problem_grid):
        self.problem_grid = problem_grid
        self.n = len(problem_grid)
#--------------------------------------------------------------------#
    def verify_if_value_is_valid(self,index_row,index_column,value):
        for i in range(self.n):
            if value == self.problem_grid[index_row][i] and value:
                return False

        for i in range(self.n):
            if value == self.problem_grid[i][index_column]:
                return False


        matr_line = index_row - index_row % 3
        matr_column = index_column - index_column % 3


        for i in range(3):
            for k in range(3):
                if value == self.problem_grid[matr_line + i][matr_column + k]:
                    return False
        return True

#--------------------------------------------------------------------#

    def __str__(self):
        return "no soluce"
#--------------------------------------------------------------------#

    def count(self):
        for i in range(self.n):
            for k in range(self.n):
                if self.problem_grid[i][k] == 0:
                    for m in range(1, self.n + 1):
                        if self.verify_if_value_is_valid(i,k,m):
                            self.problem_grid[i][k] = m
                            self.count()
                            
#--------------------------------------------------------------------#
    def solve(self):
        self.count()
        print(self.problem_grid)