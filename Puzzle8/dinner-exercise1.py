#Programming for the Puzzled -- Srini Devadas
#Guess Who is Coming to Dinner
#Given a graph where vertices are friends and edges are dislikes relationships.

#Exercise 1: Each friend has a weight, and the algorithm selects a set of friends with
#maximum weight such that no two friends dislike each other

#This procedure converts each number from 0 to 2^n - 1 into binary
#and uses the binary representation to determine the combination of guests
#and returns all possible combinations
def Combinations(n, guestList):
    allCombL = []
    for i in range(2**n):
        num = i
        cList = []
        for j in range(n): 
            if (num % 2 == 1):
                #Take the first element of the tuple in guestList
                cList = [guestList[n-1-j]] + cList
            num = num // 2
        allCombL.append(cList)
    return allCombL

#This procedure checks the given combinations to see if the combination
#contains any pair of guests who dislike each other and removes the
#combination if that is the case
def removeBadCombinations(allCombL, dislikePairs):
    allGoodCombinations = []
    for i in allCombL:
        good = True
        for j in dislikePairs:
            #Check that each element of j is in i
            #i is now a set of tuples
            if member(j[0], i) and member(j[1], i):
                good = False
        if good:
            allGoodCombinations.append(i)          
    return allGoodCombinations

#Check that the guest is a member of the combination
#Combination is a list of 2-tuples, the first of which is the guest
def member(guest, gtuples):
    for g in gtuples:
        if guest == g[0]:
            return True
    return False

#This procedure finds the combination with the maximum number of guests       
def InviteDinner(guestList, dislikePairs):
    allCombL = Combinations(len(guestList), guestList)
    allGoodCombinations = removeBadCombinations(allCombL, dislikePairs)

    #Find the maximum weight combination
    invite = max(allGoodCombinations, key=weight)
    print ('Optimum Solution:', invite)
    print ('Weight is:', weight(invite))


#Compute the weight of the combination
def weight(comb):
    return sum(c[1] for c in comb)

    
dislikePairs = [['Alice','Bob'],['Bob','Eve']]
guestList = [('Alice', 2), ('Bob', 6), ('Cleo', 3), ('Don', 10), ('Eve', 3)]
InviteDinner(guestList, dislikePairs)

LargeDislikes = [ ['B', 'C'], ['C', 'D'], ['D', 'E'],
                  ['F', 'G'], ['F', 'H'], ['F', 'I'], ['G', 'H'] ]
LargeGuestList = [('A', 2), ('B', 1), ('C', 3), ('D', 2), ('E', 1), ('F', 4),
                  ('G', 2), ('H', 1), ('I', 3)]
InviteDinner(LargeGuestList, LargeDislikes)

