#Programming for the Puzzled -- Srini Devadas
#Counting the Ways You Can Count Change
#Given a target value, and a set of bill denominations, figure out
#all the different ways that you can reach target value using various bills

#This procedure finds the different ways to make change treating
#bills of the same denomination as identical

#Exercise 1: Count the number of solutions rather than printing them all

numSolutions = 0

def makeSmartChange(bills, target, highest, sol = []):

    global numSolutions

    #Recursion base case -- reached the target
    if sum(sol) == target:
        #print (sol)
        numSolutions += 1
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
print ('Bills are', bills, 'target is 6')
print ('Number of solutions is:', numSolutions)

numSolutions = 0
bills2 = [1, 2, 5, 10]
makeSmartChange(bills2, 16, 1)
print ('Bills are', bills2, 'target is 16')
print ('Number of solutions is:', numSolutions)
