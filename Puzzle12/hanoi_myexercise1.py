#Programming for the Puzzled -- Srini Devadas
#The Towers of Brahma with a Twist
#Given n rings arranged from bigger at the bottom to smaller at the top on
#a peg, move the rings to another peg, utilizing a 3rd peg. ALl 3 pegs
#are assumed be on a line.
#The standard problem has no other constraints
#The variant problem disallows the move of a ring between non-adjacent pegs

#This procedure solves the Towers of Hanoi problem
#numRingsPlus means that the #num of Rings should be current num of Rings plus numRingsPlus
def hanoi(numRings, numRingsPlus, startPeg, endPeg, middlePeg):
    
    numMoves = 0
    if numRings > 0:
        numMoves += hanoi(numRings - 1, numRingsPlus,startPeg, middlePeg, endPeg)
        print ('Move ring', numRings+numRingsPlus, 'from peg', startPeg, 'to peg', endPeg)
        numMoves += 1
        numMoves += hanoi(numRings - 1, numRingsPlus, middlePeg, endPeg, startPeg)
    return numMoves



#hanoi(3, 0, 1, 3, 2)

def hanoiDiv(numRings, startPeg, endPeg, middlePeg, fourthPeg):

    numMoves = 0
    if numRings > 0:
        numMoves += hanoi(numRings//2, 0, startPeg, fourthPeg, middlePeg)
        numMoves += hanoi(numRings-numRings//2, numRings//2, startPeg, endPeg, middlePeg)
        #numMoves += hanoi(numRings//2, 0, fourthPeg, endPeg, startPeg)
        numMoves += hanoi(numRings//2, 0, fourthPeg, endPeg, middlePeg)
    print("num of moves = ", numMoves)
    return numMoves

hanoiDiv(8, 1, 3, 2, 4)