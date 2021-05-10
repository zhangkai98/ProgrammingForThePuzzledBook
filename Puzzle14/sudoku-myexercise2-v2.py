#Programming for the Puzzled -- Srini Devadas
#You Will Never Want to Play Sudoku Again
#Given a partially filled in Sudoku board, complete the puzzle
#obeying the rules of Sudoku

#Global variable set to 0
backtracks = 0


#This procedure finds the next empty square to fill on the Sudoku grid
def findNextCellToFill(grid):
    #Look for an unfilled grid location
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


#This procedure checks if setting the (i, j) square to e is valid
def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            #finding the top left x,y co-ordinates of
            #the section or sub-grid containing the i,j cell
            secTopX, secTopY = 3 *(i//3), 3 *(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            if i!=j and (i+j)!=8:
                return True
            else:
                if i==j and (i+j)!=8:
                    maindiagonalOK = all([e != grid[x][x] for x in range(9)])
                    if maindiagonalOK:
                        return True

                elif i!=j and(i+j)==8:
                    minordiagonalOK = all([e != grid[x][8-x] for x in range(9)])
                    if minordiagonalOK:
                        return True

                else:
                    maindiagonalOK = all([e != grid[x][x] for x in range(9)])
                    minordiagonalOK = all([e != grid[x][8-x] for x in range(9)])
                    if maindiagonalOK and minordiagonalOK:
                        return True
                return False
    return False

#This procedure fills in the missing squares of a Sudoku puzzle
#obeying the Sudoku rules through brute-force guessing and checking
def solveSudoku(grid, i=0, j=0):

    global backtracks

    #find the next cell to fill
    i, j = findNextCellToFill(grid)
    if i == -1:
        return True

    for e in range(1, 10):
        #Try different values in i, j location
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            
            #Undo the current cell for backtracking
            backtracks += 1
            grid[i][j] = 0

    return False


def printSudoku(grid):
    numrow = 0
    for row in grid:
        if numrow % 3 == 0 and numrow != 0:
            print (' ')
        print (row[0:3], ' ', row[3:6], ' ', row[6:9])
        numrow += 1       
    return

input = [[1,0,5,7,0,2,6,3,8],
         [2,0,0,0,0,6,0,0,5],
         [0,6,3,8,4,0,2,1,0],
         [0,5,9,2,0,1,3,8,0],
         [0,0,2,0,5,8,0,0,9],
         [7,1,0,0,3,0,5,0,2],
         [0,0,4,5,6,0,7,2,0],
         [5,0,0,0,0,4,0,6,3],
         [3,2,6,1,0,7,0,0,4]]




printSudoku(input)
print(solveSudoku(input))
printSudoku(input)
print ('Backtracks = ', backtracks, )
print (' ')

