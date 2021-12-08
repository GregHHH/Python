
size = 9


grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
    	[4, 0, 7, 0, 0, 0, 2, 0, 8],
    	[0, 0, 5, 2, 0, 0, 0, 0, 0],
 		[0, 0, 0, 0, 9, 8, 1, 0, 0],
    	[0, 4, 0, 0, 0, 3, 0, 0, 0],
    	[0, 0, 0, 3, 6, 0, 0, 7, 2],
    	[0, 7, 0, 0, 0, 0, 0, 0, 3],
    	[9, 0, 3, 0, 0, 0, 6, 0, 4]]


def display(a):
    for i in range(size):
        for j in range(size):
            print(a[i][j],end = " ")
        print()

def solved(grid, row, col, num):
    for x in range(size):
        if grid[row][x] == num:
            return False
             
    for x in range(size):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Solver(grid, row, col):
 
    if (row == size - 1 and col == size):
        return True
    if col == size:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Solver(grid, row, col + 1)
    for num in range(1, size + 1, 1): 
     
        if solved(grid, row, col, num):
         
            grid[row][col] = num
            if Solver(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 


if (Solver(grid, 0, 0)):
    display(grid)
else:
    print("il n'y a aucunes solutions")