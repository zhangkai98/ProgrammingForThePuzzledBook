#Programming for the Puzzled -- Srini Devadas
#The Best Time to Party
#Given a list of intervals when celebrities will be at the party
#Output is the time that you want to go the party when the maximum number of
#celebrities are still there.
#Clever algorithm that will work with fractional times

sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
         (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
sched3 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2),
          (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),
          (8.0, 10.0, 1), (9.0, 12.0, 2),
          (9.5, 10.0, 4), (10.0, 11.0, 2),
          (10.0, 12.0, 3), (11.0, 12.0, 7)]

def bestTimeToPartySmart(schedule):

    maxweight = 0
    time = 0
    for c in schedule:
        rweight = 0 
        for cother in schedule:
            if cother[0] <= c[0] and cother[1] > c[0]:
                rweight += cother[2]

        if rweight > maxweight:
            maxweight = rweight
            time = c[0]

    #Output best time to party
    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', maxweight, 'weight will be gotten!')

bestTimeToPartySmart(sched3)

                
            
        
