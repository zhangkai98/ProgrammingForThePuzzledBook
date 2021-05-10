#Programming for the Puzzled -- Srini Devadas
#Hip To Be a Square Root
#Given a number, find the square root to within a given error
#Use bisection search.

##Find the square root to within a certain error using bisection search
def bisectionSearchForSquareRoot(x, epsilon):
    if x < 0:
        print ('Sorry, imaginary numbers are out of scope!')
        return
    
    numGuesses = 0
    low = 0.0
    #Small change to fix issue with numbers less than 1
    high = max(x, 1.0)

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

bisectionSearchForSquareRoot(0.7, .01)
bisectionSearchForSquareRoot(0.25, .01)

