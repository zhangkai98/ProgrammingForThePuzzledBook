#Programming for the Puzzled -- Srini Devadas
#America Has Got Talent
#Given a group of candidates, each with a set of talents and
#given a list of talents that need to be displayed on the show
#choose a minimum number of candidates so they can display the entire
#list of talents on the show

#This procedure checks if cand1 thoroughly defeat thorough2
def Cand1DefeatCand2(cand1, cand2, candList, candTalents):
    candTal1 = candTalents[candList.index(cand1)]
    candTal2 = candTalents[candList.index(cand2)]
    for tal in candTal2:
        if not tal in candTal1:
            return False
    if len(candTal1) == len(candTal2):
        return False
    else : 
        return True

#This procedure remove candidates who can be totally defeated
def RemoveDefeated(candList, candTalents):
    RemovedTalsIndice = []
    for i in range(len(candList)):
        for j in range(len(candList)):
            if i == j:
                continue
            else:
                if Cand1DefeatCand2(candList[i], candList[j], candList, candTalents):
                    RemovedTalsIndice.append(j)

    RemovedCandList = []
    RemovedCandTalents = []
    for i in range(len(candList)):
        if i in RemovedTalsIndice:
            print('Remove candidate', candList[i])
        else:
            RemovedCandList.append(candList[i])
            RemovedCandTalents.append(candTalents[i])

    return RemovedCandList, RemovedCandTalents


#This procedure checks a given combination to see if the combination
#fails to cover any of the talents in AllTalents that need to be covered.
def Good(Comb, candList, candTalents, AllTalents):
    for tal in AllTalents:
        cover = False
        for cand in Comb:
            candTal = candTalents[candList.index(cand)]
            if tal in candTal:
                cover = True
                break
        if not cover:
            return False 
    return True         


#This procedure finds the combination with the minimum number of candidates
#that cover all the required talents by generating all the combinations
#one at a time.
def Hire4Show(candList, candTalents, talentList):
    RemovedCandList, RemovedCandTalents = RemoveDefeated(candList, candTalents)
    n = len(RemovedCandList)
    hire = RemovedCandList[:]
    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n): 
            if (num % 2 == 1):
                Combination = [RemovedCandList[n-1-j]] + Combination
            num = num // 2

        if Good(Combination, RemovedCandList, RemovedCandTalents, talentList):
            if len(hire) > len(Combination):
                hire = Combination

    print ('Optimum Solution:', hire)


Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = ['Aly', 'Bob', 'Cal', 'Don', 'Eve', 'Fay']
CandidateTalents = [ ['Flex', 'Code'], ['Dance', 'Magic'], ['Sing', 'Magic'],
                  ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code'] ]

ShowTalent2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CandidateList2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
CandToTalents2 = [ [4, 5, 7], [1, 2, 8], [2, 4, 6, 9], [3, 6, 9], [2, 3, 9],
                   [7, 8, 9], [1, 3, 7] ]

#Suppose one picked candidate C, we would get this problem to solve
ShowTalent3 = [1, 3, 5, 7, 8]
CandidateList3 = ['A', 'B', 'D', 'E', 'F', 'G']
CandToTalents3 = [ [5, 7], [1, 8], [3], [3],
                   [7, 8], [1, 3, 7] ]

#If one picked candidate G in the above problem, we would get this problem to solve
ShowTalent4 = [5, 8]
CandidateList4 = ['A', 'B', 'D', 'E', 'F']
CandToTalents4 = [ [5], [8], [], [], [8]]


Hire4Show(Candidates, CandidateTalents, Talents)
Hire4Show(CandidateList2, CandToTalents2, ShowTalent2)
Hire4Show(CandidateList3, CandToTalents3, ShowTalent3)
Hire4Show(CandidateList4, CandToTalents4, ShowTalent4)
