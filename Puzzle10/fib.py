#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens

#This procedure recursively computes the xth Fibonacci number
def rFib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return rFib(x-1) + rFib(x-2)


#This procedure iteratively computes the xth Fibonacci number
def iFib(x):
    if x < 2:
        return x
    else:
        f, g = 0, 1
        for i in range(x-1):
            f, g = g, f + g
        return g
