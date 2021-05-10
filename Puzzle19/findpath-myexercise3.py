#Programming for the Puzzled -- Srini Devadas
#A Weekend to Remember
#This puzzle deals with the problem of inviting friends to dinner over two days
#such that no two of your friends who dislike each other are invited on the same
#day.  This can be done if the graph is a bipartite graph.

#The code determines if a graph is bipartite or not. If the graph can be colored
#using two colors, it is bipartite, else it is not.

graph = {'B': ['C'],
         'C': ['B', 'D'],
         'D': ['C', 'E', 'F'],
         'E': ['D'],
         'F': ['D', 'G', 'H', 'I'],
         'G': ['F'],
         'H': ['F'],
         'I': ['F']}
grapht = {'A': ['B'],
          'B': ['A', 'C'],
          'C': ['B', 'D', 'E'],
          'D': ['C'],
          'E': ['C']}


def bipartiteGraphColor(graph, start, coloring, color):
    if start not in graph:
        return False, {}
    
    if start not in coloring:
        coloring[start] = color
    elif coloring[start] != color:
        return False, {}
    else:
        return True, coloring
    
    if color == 'Sha':
        newcolor = 'Hat'
    else:
        newcolor = 'Sha'
        
    for vertex in graph[start]:
        val, coloring = bipartiteGraphColor(graph, vertex, coloring, newcolor)
        if val == False:
            return False, {}
        
    return True, coloring

def findPath(graph, start, end, line):

    line.append('start')

    for vertex in graph[start]:
        if vertex not in line:
            line = findPath(graph, vertex, end, line)

        if vertex == end:
            return line 
        else:
            line = line[:-1]
            return line


print (findPath(grapht, 'A', 'E', []))
