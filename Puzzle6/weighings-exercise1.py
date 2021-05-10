#Programming for the Puzzled -- Srini Devadas
#Find the Fake
#Given a collection of coins, one of which is fake and is slightly heavier
#find the counterfeit using a minimum number of weighings.

#Exercise 1: Handle the case where there is no fake coin.

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

#This procedure finds the fake coin group, knowing that the
#fake coin is heavier
def findFakeGroup(group1, group2, group3):
    result1and2 = compare(group1, group2)
    
    if result1and2 == 'left':
        fakeGroup = group1
    elif result1and2 == 'right':
        fakeGroup = group2
    elif result1and2 == 'equal': #Could just be an else
        fakeGroup = group3
        
    #Added another return value
    return fakeGroup, result1and2
    

#This procedure iteratively keeps dividing the pile into 3 smaller piles and
#using the balance to choose one of the smaller piles until the fake coin is found
def CoinComparison(coinsList):
    counter = 0
    #Make a copy of coinsList
    #currList = coinsList[:]
    currList = coinsList
    while len(currList) > 1:
        group1, group2, group3 = splitCoins(currList)
        currList, res = findFakeGroup(group1, group2, group3)
        #Here's the additional check after we are down to one coin
        if len(currList) == 1 and res == 'equal':
            if compare(currList, group1) == 'equal':
                print ('There is no fake coin!')
                return
        counter += 1

    #We are down to one coin in the pile so we found the fake
    fake = currList[0]
        
    print ('The fake coin is coin', coinsList.index(fake) + 1, 'in the original list')
    print ('Number of weighings:', counter)

    
#Pretend that you actually can't see the values in these lists!
coinsList2 = [10, 10, 10, 10, 10, 10, 11, 10, 10]
coinsList = [10, 10, 10, 10, 10, 10, 11, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10]
noFakeList = [10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10]

##coinComparison(coinsList2)
CoinComparison(coinsList)
CoinComparison(noFakeList)

