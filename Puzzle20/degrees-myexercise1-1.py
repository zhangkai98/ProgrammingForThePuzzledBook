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

def degreesOfPairsSeparation(graph, pair):
    start = pair.pop()
    end = pair.pop()
    
    visited = set()
    frontier = set()
    degrees = 0

    visited.add(start)
    frontier.add(start)

    while len(frontier) > 0:
        if end in frontier:
            return degrees

        degrees += 1
        newfront = set()

        for g in frontier:
            for next in graph[g]:
                if next not in visited:
                    visited.add(next)
                    newfront.add(next)
        frontier = newfront

    return -1

def degreesOfGraphsSeparation(graph):
    vertexs = []
    for k in graph:
        vertexs.append(k)

    maxDegree = 0
    maxDegreesPair = {}

    for i in range(len(vertexs)):
        start = vertexs[i]
        for j in range(i+1, len(vertexs)):
            end = vertexs[j]
            vertexsPair = {start, end}
            degree = degreesOfPairsSeparation(graph, vertexsPair)
            if degree > maxDegree:
                maxDegree = degree
                maxDegreesPair = vertexsPair

    return maxDegree


print (degreesOfPairsSeparation(small, {'A', 'C'}))
print (degreesOfGraphsSeparation(small))

print (degreesOfPairsSeparation(large, {'A', 'N'}))
print (degreesOfGraphsSeparation(large))
'''
degreesOfSeparation(small, 'C')

degreesOfSeparation(large, 'A')
degreesOfSeparation(large, 'B')
degreesOfSeparation(large, 'U')
'''
