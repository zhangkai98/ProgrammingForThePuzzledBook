
grapha = {'V': ['W'],
          'W': ['V', 'Y'],
          'Y': ['W', 'Z'],
          'Z': ['Y']}
'''
def deleteVertex(graph, vertex):
    newgraph = {}
    for key in graph:
        if key != vertex:
            newgraph[key] = []
            for i in graph[key]:
                if i != vertex:
                    newgraph[key].append(i)
    return newgraph


def findArticulationPoint(graph):
    artiPoints = []

    for vertex in grapha:
        newgraph = deleteVertex(graph, vertex)
        if isSeperate(newgraph):
            artiPoints.append(vertex)

    if len(artiPoints) == 0:
        print ('There is no articulation point in this graph')
        return 
    else:
        print ('Here is/are', len(artiPoint), 'articulation points in this graph:', artiPoints)
        return 

def isSeperate(graph):
    conVertex = []
    allVertex = list(graph.keys())
    start = allVertex[0]
    conVertex.append(start)
    conVertex = addConnectedPoints(graph, conVertex)
    for vertex in allVertex:
        if vertex not in conVertex:
            return False
    return True
'''

def addConnectedPoints(graph, start, conVertexList):
    if start not in conVertexList:
        conVertexList.append(start)

    if isDone(graph, conVertexList):
        return conVertexList

    for vertex in graph[start]:
        conVertexList = addConnectedPoints(graph, vertex, conVertexList)
    return conVertexList

def isDone(graph, conVertexList):
    for vertex in conVertexList:
        for point in graph[vertex]:
            if point not in conVertexList:
                return False

    return True


print(addConnectedPoints(grapha, 'V', []))

