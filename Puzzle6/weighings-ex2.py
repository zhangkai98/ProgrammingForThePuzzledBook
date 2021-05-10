#Programming for the Puzzled -- Srini Devadas
#Find the Fake
#Given a collection of coins, one of which is fake and is slightly heavier
#find the counterfeit using a minimum number of weighings.

#The procedure splits coin pile into 3 groups
def splitCoins(coinsList):
    length = len(coinsList)
    group1 = coinsList[0:length//3]
    group2 = coinsList[length//3:length//3*2]
    group3 = coinsList[length//3*2:length]
    return group1, group2, group3
    
#This procedure compares the weight of 2 groups like a balance
def compare(groupA, groupB):
    if sum(groupA) > sum(groupB):
        result = 'left'
    elif sum(groupB) > sum(groupA):
        result = 'right'
    elif sum(groupB) == sum(groupA): #Could just be an else
        result = 'equal'
    return result

#This procedure finds the fake coin group and if the fake coin 
#is heavier or lighter
def findFakeGroupandType(group1, group2, group3):
    result1and2 = compare(group1, group2)
    result1and3 = compare(group1, group3)
    
    if result1and2 == 'left':
        if result1and3 == 'left':
            fakeGroup = group1
            typeFake = 'heavier'
        elif result1and3 == 'equal':
            fakeGroup = group2
            typeFake = 'lighter'
    elif result1and2 == 'right':
        if result1and3 == 'right':
            fakeGroup = group1
            typeFake = 'lighter'
        elif result1and3 == 'equal':
            fakeGroup = group2
            typeFake = 'heavier'
    elif result1and2 == 'equal':
        fakeGroup = group3
        if result1and3 == 'left':
            typeFake = 'lighter'
        elif result1and3 == 'right':
            typeFake = 'heavier'
        elif result1and3 == 'equal': 
            typeFake = 'noFakeCoin'
    return fakeGroup, typeFake

#This procedure finds the fake coin group, knowing that the
#fake coin is heavier
def findFakeGroupHeavier(group1, group2, group3):
    result1and2 = compare(group1, group2)
    
    if result1and2 == 'left':
        fakeGroup = group1
    elif result1and2 == 'right':
        fakeGroup = group2
    elif result1and2 == 'equal': #Could just be an else
        fakeGroup = group3
        
    return fakeGroup
 
#This procedure finds the fake coin group, knowing that the
#fake coin is lighter
def findFakeGroupLighter(group1, group2, group3):
    result1and2 = compare(group1, group2)
    
    if result1and2 == 'left':
        fakeGroup = group2
    elif result1and2 == 'right':
        fakeGroup = group1
    elif result1and2 == 'equal': #Could just be an else
        fakeGroup = group3
        
    return fakeGroup   

#This procedure iteratively keeps dividing the pile into 3 smaller piles and
#using the balance to choose one of the smaller piles until the fake coin is found
def CoinComparisonGeneral(coinsList):
    counter = 0
    #Make a copy of coinsList
    currList = coinsList[:]

    #Make first decision and find the type of fake coin
    group1, group2, group3 = splitCoins(currList)
    currList, typeFakeCoin = findFakeGroupandType(group1, group2, group3)
    counter += 2

    #Make the rest of decision depending on the type of fake coin
    if typeFakeCoin == 'noFakeCoin':
        print ('There is no fake coin!')
        print ('Number of weighings:', counter)
        return
    elif typeFakeCoin == 'heavier':
        while len(currList) > 1:
            group1, group2, group3 = splitCoins(currList)
            currList = findFakeGroupHeavier(group1, group2, group3)
            counter += 1
    elif typeFakeCoin == 'lighter':
        while len(currList) > 1:
            group1, group2, group3 = splitCoins(currList)
            currList = findFakeGroupLighter(group1, group2, group3)
            counter += 1

    #We are down to one coin in the pile so we found the fake
    fake = currList[0]
        
    print ('The fake coin is coin', coinsList.index(fake) + 1, 'in the original list')
    print ('The type of fake coin:', typeFakeCoin)
    print ('Number of weighings:', counter)

    
#Pretend that you actually can't see the values in coinsList!
coinsList2 = [10, 10, 10, 10, 10, 10, 11, 10, 10]
coinsList = [10, 10, 10, 10, 10, 10, 9, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10]

##CoinComparison(coinsList2)
CoinComparisonGeneral(coinsList)

