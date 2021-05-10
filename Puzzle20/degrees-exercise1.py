#Programming for the Puzzled -- Srini Devadas
#Six Degrees of Separation
#Use Breadth-First Search to find shortest paths in a graph
#These shortest paths are used to determine degree of separation between vertices
#If the procedure is run with all possible start vertices, the degree of
#separation of the graph can be found

#Exercise 1: Write a procedure to determine the degree of separation
#of a pair of vertices.  Use the procedure to find the degree of separation
#of the graph by running it on each pair of vertices.

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
    
#This procedure finds the shortest distance between a start vertex and an end vertex.
#It does this using breadth-first search.
def degreesOfSeparationVertices(graph, start, end):
    if not start in graph or not end in graph:
        return -1

    visited = set()
    frontier = set()
    degrees = 0

    visited.add(start)
    frontier.add(start)

    while len(frontier) > 0:
        #print (frontier, ':', degrees)
        degrees += 1
        newfront = set()
        for g in frontier:
            for next in graph[g]:
                if next == end:
                    #print ('Found vertex', next, 'Degree = ', degrees)
                    return degrees
                if next not in visited:
                    visited.add(next)
                    newfront.add(next)
        frontier = newfront
        
    return None


#This procedure computes the degree of separation for each pair of
#vertices in the given graph and reports the maximum number
def graphDegreeOfSeparation(graph):

    maxDegree = 0
    for g in graph:
        for h in graph:
            if g == h:
                continue
            deg = degreesOfSeparationVertices(graph, g, h)
            if maxDegree < deg:
                maxDegree = deg
                vertexpair = (g, h)

    print ('Maximum separation is between vertices', vertexpair[0], 'and',\
           vertexpair[1], 'and is equal to', maxDegree)
    
    return maxDegree

print('Distance between A and C is', degreesOfSeparationVertices(small, 'A', 'C'))
print('Distance between C and F is', degreesOfSeparationVertices(small, 'C', 'F'))

print('Distance between A and U is', degreesOfSeparationVertices(large, 'A', 'U'))
print('Distance between B and Z is', degreesOfSeparationVertices(large, 'B', 'Z'))
print('Distance between U and C is', degreesOfSeparationVertices(large, 'U', 'C'))

graphDegreeOfSeparation(large)


