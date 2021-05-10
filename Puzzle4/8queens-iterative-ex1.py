#Programming for the Puzzled -- Srini Devadas
#Keep Those Queens Apart
#Given a 8 x 8 chess board, figure out how to place 8 Queens such that
#no Queen attacks another queen.
#This code uses a single-dimensional list to represent Queen positions

import random

#This procedure checks that the most recently placed queen on the board on column
#current does not conflict with existing queens.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        #We have two diagonals hence need the abs()
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 

#This procedure places 8 Queens on a board so they don't conflict.
#It assumes n = 8 and won't work with other n!
def EightQueens(nsol, n=8):
    solutions = []

    board = [-1] * n
    for i in range(n):
        board[0] = i
        for j in range(n):
            board[1] = j
            if not noConflicts(board, 1):
                continue
            for k in range(n):
                board[2] = k
                if not noConflicts(board, 2):
                    continue
                for l in range(n):
                    board[3] = l
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if noConflicts(board, 7):
                                        solutions.append(board)   #问题可能出在此处，列表内存过大导致溢出
    
    if len(solutions) < nsol:
        print('There are no such many solutions.')
    else:
        randomindices = []
        while len(randomindices) < nsol:
            randomint = random.randint(0, len(solutions)-1)
            if not randomint in randomindices:
                randomindices.append(randomint)
                print(solutions[randomint])

    return
    '''

EightQueens(7)

