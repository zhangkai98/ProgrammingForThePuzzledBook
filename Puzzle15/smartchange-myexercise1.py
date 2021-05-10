#Programming for the Puzzled -- Srini Devadas
#Counting the Ways You Can Count Change
#Given a target value, and a set of bill denominations, figure out
#all the different ways that you can reach target value using various bills

#This procedure finds the different ways to make change treating
#bills of the same denomination as identical
count = 0

def makeSmartChange(bills, target, highest, sol = []):
    global count

    #Recursion base case -- reached the target
    if sum(sol) == target:
        count += 1
        return

    #Recursion base case -- exceeded the target
    if sum(sol) > target:
	    return

    #Recursive calls: explore adding each bill denomination
    for bill in bills:
        #Add bill only if bill is large enough
        if bill >= highest:
            newSol = sol[:]
            newSol.append(bill)
            makeSmartChange(bills, target, bill, newSol)

    return

bills = [1, 2, 5]
makeSmartChange(bills, 6, 1)
print("There are", count, "solutions.")

'''
bills2 = [1, 2, 5, 10]
makeSmartChange(bills2, 16, 1)
yourMoney =  [7, 59, 71, 97]
makeSmartChange(yourMoney, 1305, 1)
'''
