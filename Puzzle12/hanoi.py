#Programming for the Puzzled -- Srini Devadas
#The Towers of Brahma with a Twist
#Given n rings arranged from bigger at the bottom to smaller at the top on
#a peg, move the rings to another peg, utilizing a 3rd peg. ALl 3 pegs
#are assumed be on a line.
#The standard problem has no other constraints
#The variant problem disallows the move of a ring between non-adjacent pegs

#This procedure solves the Towers of Hanoi problem
def hanoi(numRings, startPeg, endPeg):
    
    numMoves = 0
    if numRings > 0:
        numMoves += hanoi(numRings - 1, startPeg, 6 - startPeg - endPeg)
        print ('Move ring', numRings, 'from peg', startPeg, 'to peg', endPeg)
        numMoves += 1
        numMoves += hanoi(numRings - 1, 6 - startPeg - endPeg, endPeg)
    return numMoves

#hanoi(3, 1, 3)

#This procedure solves the Adjacent Towers of Hanoi problem
def aHanoi(numRings, startPeg, endPeg):

    numMoves = 0                   # counting number of moves made
    if numRings == 1 :             # base case: move one ring from peg 1 to 2 to 3
        print ('Move ring', numRings, 'from peg', startPeg, 'to peg', 6-startPeg-endPeg)
        print ('Move ring', numRings, 'from peg', 6-startPeg-endPeg, 'to peg', endPeg)
        numMoves += 2              # add two moves
    else :
        numMoves += aHanoi(numRings - 1, startPeg, endPeg)      # perform function on n-1 rings
        print ('Move ring', numRings, 'from peg', startPeg, 'to peg', 6-startPeg-endPeg)    # moves next largest ring between adjacent pegs
        numMoves += 1              # add one move
        numMoves += aHanoi(numRings - 1, endPeg, startPeg)                      # perform the function on n-1 rings, pegs in reverse
        print ('Move ring', numRings, 'from peg', 6-startPeg-endPeg, 'to peg', endPeg)      # moves next largest ring between adjacent pegs
        numMoves += 1              #add one move
        numMoves += aHanoi(numRings - 1, startPeg, endPeg)                      # performs the function on n-1 rings

    return numMoves

aHanoi(3, 1, 3)
