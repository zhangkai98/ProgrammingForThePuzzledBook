#Programming for the Puzzled -- Srini Devadas
#Six Degrees of Separation
#Use Breadth-First Search to find shortest paths in a graph
#These shortest paths are used to determine degree of separation between vertices
#If the procedure is run with all possible start vertices, the degree of
#separation of the graph can be found

small = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'E'],
         'D': ['B', 'E'],
         'E': ['C', 'D', 'F'],
         'F': ['E']}

large = {'A': ['B', 'C', 'E'], 'B': ['A', 'C'], 'C': ['A', 'B', 'J'],
         'D': ['E', 'F', 'G'], 'E': ['A', 'D', 'K'], 'F': ['D', 'N'],
         'G': ['D', 'H', 'I'], 'H': ['G', 'M'], 'I': ['G', 'P'],
         'J': ['C', 'K', 'L'], 'K': ['E', 'J', 'L'], 'L': ['J', 'K', 'S'],
         'M': ['H', 'N', 'O'], 'N': ['F', 'M', 'O'], 'O': ['N', 'M', 'V'],
         'P': ['I', 'Q', 'R'], 'Q': ['P', 'W'], 'R': ['P', 'X'],
         'S': ['L', 'T', 'U'], 'T': ['S', 'U'], 'U': ['S', 'T', 'V'],
         'V': ['O', 'U', 'W'], 'W': ['Q', 'V', 'Y'], 'X': ['R', 'Y', 'Z'],
         'Y': ['W', 'X', 'Z'], 'Z': ['X', 'Y']}
    
#This procedure finds the maximum degree of separation k_S in
#a given graph from the start vertex S. This means that any vertex can be reached
#from the start vertex by traversing at most k_S edges. It prints out
#each frontier during breadth-first search.
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

def printRoute(graph, startEnd):
    start = startEnd[0]
    end = startEnd[1]
    routes = []
    frontierLists, _ = degreesOfSeparation(graph, start)

    for frontier in frontierLists:
        if end in frontier:
            finalIndex = frontierLists.index(frontier)
            break
    routes.append([end])

    for i in range(finalIndex, 0, -1):
        for j in range(len(routes)):
            end = routes[j][0]
            for vertex in frontierLists[i-1]:
                if vertex in graph[end]:  
                    if routes[j][0] == end: #Judge if there is only one route
                        routes[j].insert(0, vertex)
                    else: #Add a route if there is another route
                        newRoute = routes[j][1:]
                        newRoute.insert(0, vertex)
                        routes.append(newRoute)
    print(routes)

printRoute(large, ['B', 'Z'])

