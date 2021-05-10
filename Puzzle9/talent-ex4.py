#Programming for the Puzzled -- Srini Devadas
#America Has Got Talent
#Given a group of candidates, each with a set of talents and
#given a list of talents that need to be displayed on the show
#choose a minimum number of candidates so they can display the entire
#list of talents on the show

#This procedure checks if candW1 thoroughly defeat thorough2
def Cand1DefeatCand2(candW1, candW2, candListW, candTalentsW):
    candTal1 = candTalentsW[candListW.index(candW1)]
    candTal2 = candTalentsW[candListW.index(candW2)]
    for tal in candTal2:
        if not tal in candTal1:
            return False
    if len(candTal1) == len(candTal2):
        return False
    else: 
        if candW1[1] > candW2[1]:
            return False
        else:
            return True

#This procedure remove candidates who can be totally defeated
def RemoveDefeated(candListW, candTalentsW):
    RemovedTalsIndice = []
    for i in range(len(candListW)):
        for j in range(len(candListW)):
            if i == j:
                continue
            else:
                if Cand1DefeatCand2(candListW[i], candListW[j], candListW, candTalentsW):
                    RemovedTalsIndice.append(j)

    RemovedCandListW = []
    RemovedCandTalentsW = []
    for i in range(len(candListW)):
        if i in RemovedTalsIndice:
            print('Remove candidate', candListW[i])
        else:
            RemovedCandListW.append(candListW[i])
            RemovedCandTalentsW.append(candTalentsW[i])

    return RemovedCandListW, RemovedCandTalentsW


def FindSpecial(candListW, candTalentsW, AllTalentsW):
    SpecialCandsW = []
    for tal in AllTalentsW:
        candsWhoCanTalW = []
        for candW in candListW:
            candTal = candTalentsW[candListW.index(candW)]
            if tal in candTal:
                candsWhoCanTalW.append(candW)
        if len(candsWhoCanTalW) == 1:
            SpecialCandsW.append(candsWhoCanTalW[0])

    print('Special candidates: ', SpecialCandsW)
    return SpecialCandsW

#This produre removes the special candidates and all the talents they have
def RemoveSpeCands(SpeCandsW, candListW, candTalents, AllTalents):
    candListWAftRem = [ cand for cand in candListW if cand not in SpeCandsW]

    AllTalentsAftRem = []
    for tal in AllTalents:
        speCandCan = False
        for speCandW in SpeCandsW:
            speCandTal = candTalents[candListW.index(speCandW)]
            if tal in speCandTal:
                speCandCan = True
                break
        if not speCandCan:
            AllTalentsAftRem.append(tal)

    candTalentsAftRem = []
    for candW in candListW:
        candTalAftRem = []
        candTal = candTalents[candListW.index(candW)]
        
        if candW in SpeCandsW:
            continue
        for tal in candTal:
            if tal in AllTalentsAftRem:
                candTalAftRem.append(tal)
        candTalentsAftRem.append(candTalAftRem)

    print('Candidates with special candidates removed:', candListWAftRem)
    print('Candidate talents after removing:', candTalentsAftRem)
    print('AllTalents after removing:', AllTalentsAftRem)
    return candListWAftRem, candTalentsAftRem, AllTalentsAftRem



#This procedure checks a given combinationW to see if the combinationW
#fails to cover any of the talents in AllTalents that need to be covered.
def Good(CombW, candListW, candTalentsW, AllTalentsW):
    for tal in AllTalentsW:
        cover = False
        for candW in CombW:
            candTal = candTalentsW[candListW.index(candW)]
            if tal in candTal:
                cover = True
                break
        if not cover:
            return False 
    return True         

def Weight(CombW):
    weight = 0
    for candW in CombW:
        weight += candW[1]
    return weight


#This procedure finds the combinationW with the minimum number of candidates
#that cover all the required talents by generating all the combinationWs
#one at a time.
def Hire4Show(candListW, candTalentsW, talentListW):
    RemovedCandListW, RemovedCandTalentsW = RemoveDefeated(candListW, candTalentsW)


    SpeCandsW = FindSpecial(RemovedCandListW, RemovedCandTalentsW, talentListW)
    candListWAftRem, candTalentsAftRem, talentListAftRem = (
        RemoveSpeCands(SpeCandsW, RemovedCandListW, RemovedCandTalentsW, talentListW))

    n = len(candListWAftRem)
    hireWAftRem = candListWAftRem[:]
    for i in range(2**n):
        CombinationW = []
        num = i
        for j in range(n): 
            if (num % 2 == 1):
                CombinationW = [candListWAftRem[n-1-j]] + CombinationW
            num = num // 2

        if Good(CombinationW, candListWAftRem, candTalentsAftRem, talentListAftRem):
            if Weight(hireWAftRem) > Weight(CombinationW):
                hireWAftRem = CombinationW
    print ('Optimum Solution without special talents:', hireWAftRem)
    hireW = hireWAftRem + SpeCandsW
    print ('Optimum Solution:', hireW)
    print ('Weight is :', Weight(hireW))


'''
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
'''

ShowTalentW = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CandidateListW = [('A', 3), ('B', 2), ('C', 1), ('D', 4), ('E', 5), ('F', 2), ('G', 7)]
CandToTalentsW = [ [1, 5], [1, 2, 8], [2, 3, 6, 9], [4, 6, 8], [2, 3, 9],
                   [7, 8, 9], [1, 3, 5] ]


Hire4Show(CandidateListW, CandToTalentsW, ShowTalentW)



