#Programming for the Puzzled -- Srini Devadas
#Guess Who is Coming to Dinner
#Given a graph where vertices are friends and edges are dislikes relationships
#select a maximum number of friends such that no two friends dislike each other

#Optimized version that does not store all 2**n combinations, rather it
#iterates through them.

#This procedure finds the combination with the maximum number of guests       
def InviteDinnerOptimized(guestList, dislikePairs):

    n = len(guestList)
    invite = []
    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n): 
            if (num % 2 == 1):
                Combination = [guestList[n-1-j]] + Combination
            num = num // 2
        #Check that it is a good combination
        good = True
        for j in dislikePairs:
            #Check that each element of j is in i
            if j[0] in Combination and j[1] in Combination:
                good = False
        if good:
            #Check if it is the best combination so far
            if len(Combination) > len(invite):
                invite = Combination
                
    print ('Optimum Solution:', invite)
    
dislikePairs = [['Alice','Bob'],['Bob','Eve']]
guestList = ['Alice','Bob','Cleo','Don','Eve']
InviteDinnerOptimized(guestList, dislikePairs)

dislikePairs = [['Alice','Bob'],['Bob','Eve']]
guestList = ['Alice','Bob','Eve']
InviteDinnerOptimized(guestList, dislikePairs)

LargeDislikes = [ ['B', 'C'], ['C', 'D'], ['D', 'E'],
                  ['F', 'G'], ['F', 'H'], ['F', 'I'], ['G', 'H'] ]
LargeGuestList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
InviteDinnerOptimized(LargeGuestList, LargeDislikes)

