#Programming for the Puzzled -- Srini Devadas
#Guess Who is Coming to Dinner
#Given a graph where vertices are friends and edges are dislikes relationships
#Each friend has a weight, and the algorithm selects a set of friends with
#maximum weight such that no two friends dislike each other

#Exercise 1: Find maximum weight group to invite.  This is the version
#that does not store 2**n combinations but iterates through them.

#Check that the guest is a member of the combination
#Combination is a list of 2-tuples, the first of which is the guest
def member(guest, gtuples):
    for g in gtuples:
        if guest == g[0]:
            return True
    return False

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
            #i is now a set of tuples
            if member(j[0], Combination) and member(j[1], Combination):
                good = False
        if good:
            #Check if it is the best combination so far
            if weight(Combination) > weight(invite):
                invite = Combination
                
    print ('Optimum Solution:', invite)
    print ('Weight is:', weight(invite))


#Compute the weight of the combination
def weight(comb):
    return sum(c[1] for c in comb)

    
dislikePairs = [['Alice','Bob'],['Bob','Eve']]
guestList = [('Alice', 2), ('Bob', 6), ('Cleo', 3), ('Don', 10), ('Eve', 3)]
InviteDinnerOptimized(guestList, dislikePairs)

LargeDislikes = [ ['B', 'C'], ['C', 'D'], ['D', 'E'],
                  ['F', 'G'], ['F', 'H'], ['F', 'I'], ['G', 'H'] ]
LargeGuestList = [('A', 2), ('B', 1), ('C', 3), ('D', 2), ('E', 1), ('F', 4),
                  ('G', 2), ('H', 1), ('I', 3)]
InviteDinnerOptimized(LargeGuestList, LargeDislikes)

