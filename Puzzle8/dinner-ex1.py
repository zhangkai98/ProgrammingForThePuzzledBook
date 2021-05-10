#Programming for the Puzzled -- Srini Devadas
#Guess Who is Coming to Dinner
#Given a graph where vertices are friends and edges are dislikes relationships
#select a maximum number of friends such that no two friends dislike each other

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
                cList = [guestList[n-1-j][0]] + cList
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
            if j[0] in i and j[1] in i:
                good = False
                break
        if good:
            allGoodCombinations.append(i)          
    return allGoodCombinations

#This procedure gets the weights of current combination according to the
#orginal weight list
def ListWeight(cList, guestList):
    weight = 0
    for i in guestList:
        if i[0] in cList:
            weight += i[1]
    return weight

#This procedure finds the combination with the maximum number of guests       
def InviteDinner(guestList, dislikePairs):
    allCombL = Combinations(len(guestList), guestList)
    allGoodCombinations = removeBadCombinations(allCombL, dislikePairs)
    invite = []
    for i in allGoodCombinations:
        if ListWeight(i, guestList) > ListWeight(invite, guestList):
            invite = i
##    invite = max(allGoodCombinations, key=len)
    print ('Optimum Solution:', invite)


dislikePairs = [['Alice','Bob'],['Bob','Eve']]
guestList = [('Alice', 2), ('Bob', 6), ('Cleo', 3), ('Don', 10), ('Eve', 3)]
InviteDinner(guestList, dislikePairs)
'''
dislikePairs = [['Alice','Bob'],['Bob','Eve']]
guestList = ['Alice','Bob','Eve']
InviteDinner(guestList, dislikePairs)

LargeDislikes = [ ['B', 'C'], ['C', 'D'], ['D', 'E'],
                  ['F', 'G'], ['F', 'H'], ['F', 'I'], ['G', 'H'] ]
LargeGuestList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
InviteDinner(LargeGuestList, LargeDislikes)
'''
