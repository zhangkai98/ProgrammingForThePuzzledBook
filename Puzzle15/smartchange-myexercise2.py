#Programming for the Puzzled -- Srini Devadas
#Counting the Ways You Can Count Change
#Given a target value, and a set of bill denominations, figure out
#all the different ways that you can reach target value using various bills

#This procedure finds the different ways to make change treating
#bills of the same denomination as identical
def makeSmartChange(bills, target, highest, sol = []):

    #Recursion base case -- reached the target
    if sum(sol) == target:
        print (sol)
        return

    #Recursion base case -- exceeded the target
    if sum(sol) > target:
	    return

    #Recursive calls: explore adding each bill denomination
    for i in range(len(bills)):
        #Add bill only if bill is large enough
        if bills[i][0] >= highest and bills[i][1] > 0:
            newSol = sol[:]
            newSol.append(bills[i][0])
            newBills = bills[0:i] + [(bills[i][0], bills[i][1] - 1)] + bills[i+1:]

            makeSmartChange(newBills, target, bills[i][0], newSol)

    return

money = [(1, 3), (2, 3), (5, 1)]
makeSmartChange(money, 6, 1)

'''
bills2 = [1, 2, 5, 10]
makeSmartChange(bills2, 16, 1)
yourMoney =  [7, 59, 71, 97]
makeSmartChange(yourMoney, 1305, 1)
'''
