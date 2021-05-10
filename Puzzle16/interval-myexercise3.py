#Programming for the Puzzled -- Srini Devadas
#Greed is Good
#A greedy algorithm is used to find the most packed course schedule, i.e.,
#the one with the maximum number of non-conflicting classes

#This procedure is given a course and a list of other courses, and removes
#all courses in the list that conflict with the given course. 
def getSubCourses(course, courses):
    subCourses = []
    for c in courses:
        if c[0] >= course[1]:
            subCourses.append(c)
    return subCourses


def recursiveSelect(courses):
    if len(courses) == 0:
        return []

    if len(courses) > 0:
        maxWeight = 0
        selectedCourses = []

        for c in courses:
            subCourses = getSubCourses(c, courses)
            selCourses = [c] + recursiveSelect(subCourses)

            weight = 0
            for selC in  selCourses:
                weight += (selC[1]-selC[0])

            if weight > maxWeight:
                maxWeight = weight
                selectedCourses = selCourses
        return selectedCourses


scourses = [ [8, 10], [9, 10], [10, 12], [11, 12], [12, 14], [13, 14] ]

wcourses = [[8,10,1], [9,12,3], [11,12,1],
             [12,13,1], [15,16,1], [16,17,1],
             [18,20,2], [17,19,2], [13,20,7]]

##wcourses1 = [[8,10,3], [9,12,1]]
print ('Maximum duration courses:', recursiveSelect(scourses))
print ('Maximum duration courses:', recursiveSelect(wcourses))
