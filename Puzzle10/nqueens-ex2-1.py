#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens
#Given the dimension of a square "chess" board, call it N, find a placement
#of N queens such that no two Queens attack each other using recursive search

#This procedure initializes the board to be empty, calls the recursive N-queens
#procedure and prints the returned solution
def nQueens(board):
    size = len(board)
    noPiece = [False] * size
    res = rQueens(board, 0, size, noPiece)
    if res:
        prettyPrint(board)
    else:
        print('No solution!')

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
        return True
    else:
        if board[current] == -1:
            noPiece[current] = True

        for i in range(size):
            if noPiece[current]:
                board[current] = i
            if (noConflicts(board, current)):
                done = rQueens(board, current + 1, size, noPiece)
                if (done):
                    return True
        return False


nQueens([-1, -1, 3, -1, -1, -1, -1, 0, -1, 5])


