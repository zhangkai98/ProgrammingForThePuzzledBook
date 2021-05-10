#Programming for the Puzzled -- Srini Devadas
#Counting the Ways You Can Count Change
#Given a target value, and a set of bill denominations, figure out
#all the different ways that you can reach target value using various bills

#This procedure finds the different ways to make change treating
#bills of the same denomination as identical. It repeats some ways.
def makeChange(bills, target, sol = []):

    #Recursion base case -- reached the target
    if sum(sol) == target:
        print (sol)
        return

    #Recursion base case -- exceeded the target
    if sum(sol) > target:
	    return

    #Recursive calls: explore adding each bill denomination
    for bill in bills:
        newSol = sol[:]
        newSol.append(bill)
        makeChange(bills, target, newSol)

    return


bills = [1, 2, 5]
makeChange(bills, 6)
