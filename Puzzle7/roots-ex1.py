#Programming for the Puzzled -- Srini Devadas
#Hip To Be a Square Root
#Given a number, find the square root to within a given error
#Two strategies are shown: Iterative search and bisection search

##Find the square root of a perfect square using iterative search
def findSquareRoot(x):
    if x < 0:
        print ('Sorry, imaginary numbers are out of scope!')
        return
        
    ans = 0
    while ans**2 < x:
        ans = ans + 1

    if ans**2 != x:
        print (x, 'is not a perfect square')
        print ('Square root of ' + str(x) +
               ' is close to ' + str(ans - 1))
    else:
        print ('Square root of ' + str(x) + ' is ' + str(ans))

    return

##Find the square root to within a certain error using iterative search
def findSquareRootWithinError(x, epsilon, increment):
    if x < 0:
        print ('Sorry, imaginary numbers are out of scope!')
        return
    
    numGuesses = 0
    ans = 0.0
    while x - ans**2 > epsilon:
        ans += increment
        numGuesses += 1

    print ('numGuesses =', numGuesses)
    if abs(x - ans**2) > epsilon:
        print ('Failed on square root of', x)
    else:
        print (ans, 'is close to square root of', x)

    return


##Find the square root to within a certain error using bisection search
def bisectionSearchForSquareRoot(x, epsilon):
    if x < 0:
        print ('Sorry, imaginary numbers are out of scope!')
        return
    
    numGuesses = 0

    ##Judge if x is smaller than 1-epsilon
    if x < 1 - epsilon:
        low = x
        high = 1.0
    else:
        low = 0.0
        high = x

    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
        numGuesses += 1
        #print('low = ', low, 'high = ', high, 'guess = ', ans)
    print ('numGuesses =', numGuesses)
    print (ans, 'is close to square root of', x)

    return

##findSquareRoot(65536)
##findSquareRootWithinError(65535, .01, .001)
##findSquareRootWithinError(65535, .01, .0001)
##findSquareRootWithinError(65535, .01, .00001)
##bisectionSearchForSquareRoot(65535, .01)
bisectionSearchForSquareRoot(0.25, .001)
