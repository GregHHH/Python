from a import *

a = np.array([[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
    	[4, 0, 7, 0, 0, 0, 2, 0, 8],
    	[0, 0, 5, 2, 0, 0, 0, 0, 0],
 		[0, 0, 0, 0, 9, 8, 1, 0, 0],
    	[0, 4, 0, 0, 0, 3, 0, 0, 0],
    	[0, 0, 0, 3, 6, 0, 0, 7, 2],
    	[0, 7, 0, 0, 0, 0, 0, 0, 3],
    	[9, 0, 3, 0, 0, 0, 6, 0, 4]])

# print(a[1][0])

# for i in range(10):
#     if i in list_test:
#         print(i)
#


# print(6//3)
sudoku = SudokuSolver(problem_grid = a)

a = sudoku.solve()
# print(sudoku)
# print(sudoku.problem_grid)
# print(a)