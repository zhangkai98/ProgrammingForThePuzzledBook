#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens
#Given the dimension of a square "chess" board, call it N, find a placement
#of N queens such that no two Queens attack each other using recursive search

#This procedure initializes the board to be empty, calls the recursive N-queens
#procedure and prints the returned solution
def nQueens(board):
    size = len(board)
    noPiece = [False] * size
    for i in range(size):
        if board[i] == -1:
            noPiece[i] = True
    ##print(noPiece)

    rQueens(board, 0, size, noPiece)

def prettyPrint(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if j == board.index(i):
                print('Q', end = ' ')
            else:
                print('.', end = ' ')
        print('')
    return 

#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


#This procedure places a queens on the board on a given column so it does
#not conflict with the existing queens, and then calls itself recursively
#to place subsequent queens till the requisite number of queens are placed
def rQueens(board, current, size, noPiece):
    if (current == size):
        prettyPrint(board)
        print()
    else:
        if noPiece[current]:
            for i in range(size):
                board[current] = i
                if (noConflicts(board, current)):
                    rQueens(board, current + 1, size, noPiece)
        else:
            if (noConflicts(board, current)):
                rQueens(board, current + 1, size, noPiece)


nQueens([-1, -1, 4, -1, -1, -1, -1, 0, -1, 5])
##nQueens([5, -1, -1, -1, 0 ,-1, 1])


