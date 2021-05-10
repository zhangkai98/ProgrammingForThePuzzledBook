#Programming for the Puzzled -- Srini Devadas
#Greed is Good
#A greedy algorithm is used to find the most packed course schedule, i.e.,
#the one with the maximum number of non-conflicting classes

#Exercise 1: New rule that uses earliest finish time but tiebreaks based
#on length of the class.

#This procedure is given a course and a list of other courses, and removes
#all courses in the list that conflict with the given course. 
def removeConflictingCourses(selCourse, courses):
    nonConflictingCourses = []
    for s in courses:
        if s[1] <= selCourse[0] or s[0] >= selCourse[1]:
            nonConflictingCourses.append(s)
    
    return nonConflictingCourses

#This procedure iteratively picks a course using a function selectionRule that is
#an argument to the procedure, and removes all conflicting courses, and repeats
#until the list of courses is empty
def executeSchedule(courses, selectionRule):
    selectedCourses = []
    while len(courses) > 0:
        selCourse = selectionRule(courses)
        selectedCourses.append(selCourse)
        courses = removeConflictingCourses(selCourse, courses)
    return selectedCourses


#This procedure implements the earliest start time rule
def earliestStartTime(courses):
    for s in courses:
        if s == courses[0]: 
            earliestStartTime = s
        if s[0] < earliestStartTime[0]:
            earliestStartTime = s
    return earliestStartTime

#This procedure implements the shortest duration time rule
def shortDuration(courses):
    shortDuration = courses[0]
    for s in courses:
        if s[1] - s[0] < shortDuration[1] - shortDuration[0]:
            shortDuration = s
    return shortDuration

#This procedure implements the least number of conflicts rule
def leastConflicts(courses):
    conflictTotal = []
    conflictList = []
    for i in courses:
        for j in courses:
            if i == j or i[1] <= j[0] or i[0] <= j[1]:
                continue
            conflictList.append(courses.index(j))
        conflictTotal.append(conflictList)
        conflictList = []
    leastConflict = min(conflictTotal, key = len)
    leastConflictCourse = courses[conflictTotal.index(leastConflict)]
    return leastConflictCourse

#This procedure implements the earliest finish time rule
def earliestFinishTime(courses):
    earliestFinishTime = courses[0]
    for i in courses:
        if i[1] < earliestFinishTime[1]:
            earliestFinishTime = i
    return earliestFinishTime

#This procedure implements the earliest finish time rule with the 
#additional check that the shortest duration class is added in the case of ties
def earliestFTwithSD(courses):
    earliestFT = courses[0]
    for i in courses:
        if i[1] < earliestFT[1] or\
           (i[1] <= earliestFT[1] and i[1] - i[0] < earliestFT[1] - earliestFT[0]):
            earliestFT = i
    return earliestFT


mycourses2 = [[8,9],[9,12],[11,12],[12,13],[15,16],[16,17],[18,20],[17,19],[13,20]]
scourses = [ [8, 10], [9, 10], [10, 12], [11, 12], [12, 14], [13, 14] ]

print ('Earliest finish time:', executeSchedule(scourses, earliestFinishTime))
print ('Earliest finish time with tiebreak:', executeSchedule(scourses, earliestFTwithSD))

print ('Earliest finish time:', executeSchedule(mycourses2, earliestFinishTime))
print ('Earliest finish time with tiebreak:', executeSchedule(mycourses2, earliestFTwithSD))
