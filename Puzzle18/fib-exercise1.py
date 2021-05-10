#Programming for the Puzzled -- Srini Devadas
#Memory Serves You Well

#Exercise 1: Add memoization to Fibonacci to raise efficiency to iterative
#            version.

#This procedure recursively computes the xth Fibonacci number
#Initially called with memo={}
def rFibMemoize(x, memo):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x in memo:
        return memo[x]
    else:
        #Subproblem was not solved, need to solve it
        result = rFibMemoize(x-1, memo) + rFibMemoize(x-2, memo)
        memo[x] = result
        return result

#This procedure iteratively computes the xth Fibonacci number
def iFib(x):
    if x < 2:
        return x
    else:
        f, g = 0, 1
        for i in range(x-1):
            f, g = g, f + g
        return g

print(iFib(30))
print(rFibMemoize(30, {}))

