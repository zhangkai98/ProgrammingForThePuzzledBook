#Programming for the Puzzled -- Srini Devadas
#America Has Got Talent
#Given a group of candidates, each with a set of talents and
#given a list of talents that need to be displayed on the show
#choose a minimum number of candidates so they can display the entire
#list of talents on the show

##This procedure finds the special candidate in candidate list. Special
##means he or she has the talents which all other candidates don't have
def FindSpecial(candList, candTalents, AllTalents):
    SpecialCands = []
    for tal in AllTalents:
        candsWhoCanTal = []
        for cand in candList:
            candTal = candTalents[candList.index(cand)]
            if tal in candTal:
                candsWhoCanTal.append(cand)
        if len(candsWhoCanTal) == 1:
            SpecialCands.append(candsWhoCanTal[0])

    print('Special candidates: ', SpecialCands)
    return SpecialCands

#This produre removes the special candidates and all the talents they have
def RemoveSpeCands(SpeCands, candList, candTalents, AllTalents):
    candListAftRem = [ cand for cand in candList if cand not in SpeCands]

    AllTalentsAftRem = []
    for tal in AllTalents:
        speCandCan = False
        for speCand in SpeCands:
            speCandTal = candTalents[candList.index(speCand)]
            if tal in speCandTal:
                speCandCan = True
                break
        if not speCandCan:
            AllTalentsAftRem.append(tal)

    candTalentsAftRem = []
    for cand in candList:
        candTalAftRem = []
        candTal = candTalents[candList.index(cand)]
        
        if cand in SpeCands:
            continue
        for tal in candTal:
            if tal in AllTalentsAftRem:
                candTalAftRem.append(tal)
        candTalentsAftRem.append(candTalAftRem)

    print('Candidates with special candidates removed:', candListAftRem)
    print('Candidate talents after removing:', candTalentsAftRem)
    print('AllTalents after removing:', AllTalentsAftRem)
    return candListAftRem, candTalentsAftRem, AllTalentsAftRem


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
    SpeCands = FindSpecial(candList, candTalents, talentList)
    candListAftRem, candTalentsAftRem, talentListAftRem = (
        RemoveSpeCands(SpeCands, candList, candTalents, talentList))

    n = len(candListAftRem)
    hireAftRem = candListAftRem[:]
    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n): 
            if (num % 2 == 1):
                Combination = [candListAftRem[n-1-j]] + Combination
            num = num // 2

        if Good(Combination, candListAftRem, candTalentsAftRem, talentListAftRem):
            if len(hireAftRem) > len(Combination):
                hireAftRem = Combination
    print ('Optimum Solution without special talents:', hireAftRem)
    hire = hireAftRem + SpeCands
    print ('Optimum Solution:', hire)

'''
Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = ['Aly', 'Bob', 'Cal', 'Don', 'Eve', 'Fay']
CandidateTalents = [ ['Flex', 'Code'], ['Dance', 'Magic'], ['Sing', 'Magic'],
                  ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code'] ]
'''
ShowTalent2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CandidateList2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
CandToTalents2 = [ [4, 5, 7], [1, 2, 8], [2, 4, 6, 9], [3, 6, 9], [2, 3, 9],
                   [7, 8, 9], [1, 3, 7] ]
'''
#Suppose one picked candidate C, we would get this problem to solve
ShowTalent3 = [1, 3, 5, 7, 8]
CandidateList3 = ['A', 'B', 'D', 'E', 'F', 'G']
CandToTalents3 = [ [5, 7], [1, 8], [3], [3],
                   [7, 8], [1, 3, 7] ]

#If one picked candidate G in the above problem, we would get this problem to solve
ShowTalent4 = [5, 8]
CandidateList4 = ['A', 'B', 'D', 'E', 'F']
CandToTalents4 = [ [5], [8], [], [], [8]]
'''

##Hire4Show(Candidates, CandidateTalents, Talents)
Hire4Show(CandidateList2, CandToTalents2, ShowTalent2)
##Hire4Show(CandidateList3, CandToTalents3, ShowTalent3)
##Hire4Show(CandidateList4, CandToTalents4, ShowTalent4)
