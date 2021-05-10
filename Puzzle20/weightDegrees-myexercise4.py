#Programming for the Puzzled -- Srini Devadas
#Six Degrees of Separation
#Use Breadth-First Search to find shortest paths in a graph
#These shortest paths are used to determine degree of separation between vertices
#If the procedure is run with all possible start vertices, the degree of
#separation of the graph can be found

smallw = {'A': [('B', 1), ('C', 2)],
         'B': [('A', 1), ('C', 1), ('D', 1)],
         'C': [('A', 2), ('B', 1), ('E', 2)],
         'D': [('B', 1), ('E', 1)],
         'E': [('C', 2), ('D', 1), ('F', 2)],
         'F': [('E', 2)]}

    
#This procedure finds the maximum degree of separation k_S in
#a given graph from the start vertex S. This means that any vertex can be reached
#from the start vertex by traversing at most k_S edges. It prints out
#each frontier during breadth-first search.
def transformGraph(graph):
    newGraph = {}
    for g in graph:
        newGraph[g] = []
        for nextWeight in graph[g]:
            next = nextWeight[0]
            weight = nextWeight[1]

            if weight == 1:
                newGraph[g].append(next)
            elif weight == 2:
                newVertex = g + next
                if newVertex[::-1] not in newGraph:
                    newGraph[g].append(newVertex)
                    newGraph[newVertex] = [g, next]
                else:
                    newGraph[g].append(newVertex[::-1])
    return newGraph


def checkSymmetry(graph):
   isSymmetric = True
   for start in graph:
      for end in graph[start]:
         if start not in graph[end]:
            isSymmetric = False
            print('lack of \'', end, '\': [\'', start, '\']', sep='')
   return isSymmetric

def degreesOfSeparation(graph, start):
    if start not in graph:
        return -1

    frontierLists = []
    visited = set()
    frontier = set()
    degrees = 0

    visited.add(start)
    frontier.add(start)

    while len(frontier) > 0:
        print (frontier, ':', degrees)
        frontierLists.append(frontier)

        degrees += 1
        newfront = set()
        for g in frontier:
            for next in graph[g]:
                if next not in visited:
                    visited.add(next)
                    newfront.add(next)
        frontier = newfront       
    return frontierLists, degrees - 1

def weightDegreesOfSeparation(graph, start):
    if start not in graph:
        return -1
    newGraph = transformGraph(graph)
    print('Original graph = ', graph, '\n')
    print('New graph = ', newGraph, '\n')

    
    if checkSymmetry(newGraph):
        print('New graph separation:')
        frontierLists, _ = degreesOfSeparation(newGraph, start)
        print('')

    print('Original graph separation:')
    degrees = 0
    for frontier in frontierLists:
        originalFrontier = set()
        for g in frontier:
            if g in graph:
                originalFrontier.add(g)
        if originalFrontier != set():  #In judgment, {} means empty dictionary while set() means empty set, so {} is not equal to set()
            print (originalFrontier, ':', degrees)
        degrees += 1
    return degrees-1

weightDegreesOfSeparation(smallw, 'A')

