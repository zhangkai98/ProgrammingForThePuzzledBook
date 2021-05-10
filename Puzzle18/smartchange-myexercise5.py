#Programming for the Puzzled -- Srini Devadas
#Counting the Ways You Can Count Change
#Given a target value, and a set of bill denominations, figure out
#all the different ways that you can reach target value using various bills

#This procedure finds the different ways to make change treating
#bills of the same denomination as identical

#Exercise 1: Count the number of solutions rather than printing them all

def makeSmartChange(bills, biScale, target):

    #This condition is very important
    if target == 0:
        return 1

    elif target < min(bills):
        return 0
    elif biScale == 1:
        return 1
    else:
        return makeSmartChange(bills, biScale-1, target) + makeSmartChange(bills, biScale, target-bills[biScale-1])

bills = [1, 2, 5]
print ('Bills are', bills, 'target is 6')
print ('Number of solutions is:', makeSmartChange(bills, 3, 6))

bills2 = [1, 2, 5, 10]
print ('Bills are', bills2, 'target is 16')
print ('Number of solutions is:', makeSmartChange(bills2, 4, 16))
