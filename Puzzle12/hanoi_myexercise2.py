#Programming for the Puzzled -- Srini Devadas
#The Towers of Brahma with a Twist
#Given n rings arranged from bigger at the bottom to smaller at the top on
#a peg, move the rings to another peg, utilizing a 3rd peg. ALl 3 pegs
#are assumed be on a line.
#The standard problem has no other constraints
#The variant problem disallows the move of a ring between non-adjacent pegs

'''
def hanoiN(numPegs, numRings):
    numMovesResult = 10000000

    #if numRings == 0:
         #return 0
    if numPegs == 3:
        return 2**numRings-1

    if numRings == 1:
        return 1

    for k in range(1, numRings):
        numMoves = 2 * hanoiN(numPegs, k) + hanoiN(numPegs-1, numRings-k)
        if numMoves < numMovesResult:
            numMovesResult = numMoves
    
    return numMovesResult

print("4 pegs 8 rings: ", hanoiN(4, 8))
'''

def hanoiN(numPegs, numRings):
    numMovesResult = 10000000

    if numRings == 1:
        return 1

    for k in range(1, numRings):
        if (numPegs-1) == 2:
            if (numRings-k) != 1:
                continue
        numMoves = 2 * hanoiN(numPegs, k) + hanoiN(numPegs-1, numRings-k)
        if numMoves < numMovesResult:
            numMovesResult = numMoves
    
    return numMovesResult

print("4 pegs 8 rings: ", hanoiN(4, 8))
