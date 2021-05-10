#Programming for the Puzzled -- Srini Devadas
#Please Do Break the Crystal
#This is an interactive procedure that given n floors and d balls determines
#what floors to drop the balls from to minimize the worst-case number of
#drops required to determine the hardness coefficient of the crystal.
#The hardness coefficient will range from 0 (breaks at Floor 1) or n (does not
#break at n.
def howHardIsTheCrystal(n, d):

    #First determine the radix r
    r = 1
    while (r**d <= n):
        r = r + 1
    print('Radix chosen is', r)

    #Decide how many balls should be used
    while (r**(d-1) > n):
        d -= 1
    print(d, 'balls should be used in fact.')

    numDrops = 0
    floorNoBreak = [0] * d
    interval = [0, n]
    indexBrokenBalls = []
    for i in range(d):
        #Begin phase i
        for j in range(r-1):
            #increment ith digit of representation
            floorNoBreak[i] += 1
            Floor = convertToDecimal(r, d, floorNoBreak)
            #Make sure you aren't higher than the highest floor
            if Floor > n:
                floorNoBreak[i] -= 1
                break
            print('Interval:', interval)
            print ('Drop ball', i+1, 'from Floor', Floor)
            yes = input('Did the ball break (yes/no)?:')
            numDrops += 1
            if yes == 'yes':
                floorNoBreak[i] -= 1
                indexBrokenBalls.append(i+1)
                interval = [interval[0], Floor]
                break
            interval = [Floor, interval[1]]

    print('Interval:', interval)
    hardness = convertToDecimal(r, d, floorNoBreak)
    print('Hardness coefficient is', hardness)
    print('Total number of drops is', numDrops)
    print('Ball', indexBrokenBalls, 'was/were broken.')

    return

def convertToDecimal(r, d, rep):
    number = 0
    for i in range(d-1):
        number = (number + rep[i]) * r
    number += rep[d-1]

    return number

howHardIsTheCrystal(128, 6)    
