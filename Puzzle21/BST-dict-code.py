#Programming for the Puzzled -- Srini Devadas
#Questions Have a Price
#Binary Search Tree code using a dictionary representation

#Sample BST
BST = {'root': [22, 'A', 'B'],
       'A': [14, 'C', 'D'],
       'B': [33, 'E', ''],
       'C': [2, '', ''],
       'D': [17, '', ''],
       'E': [27, '', '']}


#this is the canonical BST version
def lookup(bst, cVal):
    return lookupHelper(bst, cVal, 'root')

def lookupHelper(bst, cVal, current):
    if current == '':
        return False
    elif bst[current][0] == cVal:
            return True
    elif (cVal < bst[current][0]):
        return lookupHelper(bst, cVal, bst[current][1])
    else:
        return lookupHelper(bst, cVal, bst[current][2])


#Insert into a binary tree.
#note that here, val is just the numeric value of the vertex
#'' is the empty value for a vertex name, meaning that there is no vertex there.
def insert(name, val, bst):
    return insertHelper(name, val, 'root', bst)

def insertHelper(name, val, pred, bst):
    predLeft = bst[pred][1]
    predRight = bst[pred][2]
    if ((predRight == '') and (predLeft == '')):
        if val < bst[pred][0]:
            bst[pred][1] = name
        else:
            bst[pred][2] = name
        bst[name] = [val, '', '']
        return bst
    elif (val < bst[pred][0]):
        if predLeft == '':
            bst[pred][1] = name
            bst[name] = [val, '', '']
            return bst
        else:
            return insertHelper(name, val, bst[pred][1], bst)
    else:
        if predRight == '':
            bst[pred][2] = name
            bst[name] = [val, '', '']
            return bst
        else:
            return insertHelper(name, val, bst[pred][2], bst)


#In order traversal of the tree
def inOrder(bst):
    outputList = []
    inOrderHelper(bst, 'root', outputList)
    return outputList
    
def inOrderHelper(bst, vertex, outputList):
    if vertex == '':
        return
    
    inOrderHelper(bst, bst[vertex][1], outputList)
    outputList.append(bst[vertex][0])
    inOrderHelper(bst, bst[vertex][2], outputList)
    return

BST = {}
BST['root'] = [22, '', '']
insert('A', 14, BST)
insert('B', 33, BST)
insert('C', 2, BST)
insert('D', 17, BST)
insert('E', 27, BST)
