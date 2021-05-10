#Programming for the Puzzled -- Srini Devadas
#The Towers of Brahma with a Twist
#Given n rings arranged from bigger at the bottom to smaller at the top on
#a peg, move the rings to another peg, utilizing a 3rd peg. ALl 3 pegs
#are assumed be on a line.

#This procedure solves the modified Towers of Hanoi problem with a 4th peg

def hanoiOffset(numRings, offset, startPeg, middlePeg, endPeg):
    
    numMoves = 0
    if numRings > 0:
        numMoves += hanoiOffset(numRings - 1, offset, startPeg, endPeg, middlePeg)
        print ('Move ring', numRings + offset, 'from peg', startPeg, 'to peg', endPeg)
        numMoves += 1
        numMoves += hanoiOffset(numRings - 1, offset, middlePeg, startPeg, endPeg)
    return numMoves


#This procedure assumes that numRings is an even number
def hanoi4pegs(numRings, startPeg, middlePeg, endPeg, fourthPeg):

    numMoves = 0
    if numRings > 0:
        numMoves += hanoiOffset(numRings//2, 0, startPeg, middlePeg, fourthPeg)
        numMoves += hanoiOffset(numRings//2, numRings//2, startPeg, middlePeg, endPeg)
        numMoves += hanoiOffset(numRings//2, 0, fourthPeg, middlePeg, endPeg)
    return numMoves


#hanoi4pegs(4, 1, 2, 3, 4)
hanoi4pegs(8, 1, 2, 3, 4)
