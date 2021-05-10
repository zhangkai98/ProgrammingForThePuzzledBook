#Programming for the Puzzled -- Srini Devadas
#Questions Have a Price
#An OOP-style BST representation is created. This procedure finds the optimal BST
#that minimizes the average (expected) number of guesses to guess a number
#given probabilities for each of the numbers.

#Exercise 1: Add a getVertex() method.


#BST Vertex Class and associated methods
class BSTVertex:
    def __init__(self, val, leftChild, rightChild):
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild

#Defining these methods corresponds to the conventional way of accessing
#and mutating objects

    def getVal(self):
        return self.val

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setVal(self, newVal):
        self.val = newVal

    def setLeftChild(self, newLeft):
        self.leftChild = newLeft

    def setRightChild(self, newRight):
        self.rightChild = newRight


#BST Tree Class and associated methods
class BSTree:
    def __init__(self, root):
        self.root = root

    #Lookup a BST vertex to see if it exists in the tree
    def lookup(self, cVal):
        return self.__lookupHelper(cVal, self.root)

    def __lookupHelper(self, cVal, cVertex):
        if cVertex == None:
            return False
        elif cVal == cVertex.getVal():
            return True
        elif (cVal < cVertex.getVal()):
            return self.__lookupHelper(cVal, cVertex.getLeftChild())
        else:
            return self.__lookupHelper(cVal, cVertex.getRightChild())

    #Similar to lookup, except the vertex is returned rather than True or False
    def getVertex(self, cVal):
        return self.__getVertexHelper(cVal, self.root)

    def __getVertexHelper(self, cVal, cVertex):
        if cVertex == None:
            return None
        elif cVal == cVertex.getVal():
            return cVertex
        elif cVertex is None:
            return None
        elif (cVal < cVertex.getVal()):
            return self.__getVertexHelper(cVal, cVertex.getLeftChild())
        else:
            return self.__getVertexHelper(cVal, cVertex.getRightChild())
   

    def insert(self, val):
        if self.root == None:
            self.root = BSTVertex(val, None, None)
        else:
            self.__insertHelper(val, self.root)

    def __insertHelper(self, val, pred):
        predLeft = pred.getLeftChild()
        predRight = pred.getRightChild()
        if (predRight == None and predLeft == None):
            if val < pred.getVal():
                pred.setLeftChild((BSTVertex(val, None, None)))
            else:
                pred.setRightChild((BSTVertex(val, None, None)))
        elif (val < pred.getVal()):
            if predLeft is None:
                pred.setLeftChild((BSTVertex(val, None, None)))
            else:
                self.__insertHelper(val, pred.getLeftChild())
        else:
            if predRight == None:
                pred.setRightChild((BSTVertex(val, None, None)))
            else:
                self.__insertHelper(val, pred.getRightChild())

    #In order traversal of the tree
    def inOrder(self):
        outputList = []
        return self.__inOrderHelper(self.root, outputList)
    
    def __inOrderHelper(self, vertex, outputList):
        if vertex is None:
            #we've hit the bottom of the tree
            return
        self.__inOrderHelper(vertex.getLeftChild(), outputList)
        outputList.append(vertex.getVal())
        self.__inOrderHelper(vertex.getRightChild(), outputList)
        return outputList


#Print a BST whose root is vertex recursively
def printBST(vertex):

    left = vertex.leftChild
    right = vertex.rightChild
    if left != None and right != None:
        print('Value =', vertex.val, 'Left =', left.val, 'Right =', right.val)
        printBST(left)
        printBST(right)
    elif left != None and right == None:
        print('Value =', vertex.val, 'Left =', left.val, 'Right = None')
        printBST(left)
    elif left == None and right != None:
        print('Value =', vertex.val, 'Left = None', 'Right =', right.val)
        printBST(right)
    else:
        print('Value =', vertex.val, 'Left = None Right = None')

    return
    

#Finding the optimal BST given probabilities of each key being looked up
def optimalBST(keys, prob):

    n = len(keys)

    #Set up the data structure for the values of optimal solutions
    opt = [[0 for i in range(n)] for j in range(n)]

    #Compute the optimal solutions for all the subproblems
    computeOptRecur(opt, 0, n-1, prob)

    #Create optimal OOP-style BST using the computed optimal solutions
    tree = createBSTRecur(None, opt, 0, n-1, keys)
    print('Minimum average number of guesses is', opt[0][n-1][0])
    printBST(tree.root)
    
    return


def computeOptRecur(opt, left, right, prob):

    #base case
    if left == right:
        opt[left][left] = (prob[left], left)
        return

    #need to recurse to find best r
    for r in range(left, right + 1):
        if left <= r - 1:
            computeOptRecur(opt, left, r - 1, prob)
            leftval = opt[left][r-1]
        else:
            leftval = (0, -1)
        if r + 1 <= right:
            computeOptRecur(opt, r + 1, right, prob)
            rightval = opt[r+1][right]
        else:
            rightval = (0, -1)

        if r == left:
            bestval = leftval[0] + rightval[0]
            bestr = r
        elif bestval > leftval[0] + rightval[0]:
            bestr = r
            bestval = leftval[0] + rightval[0]

    #Fill in the best value
    weight = sum(prob[left:right+1])
    opt[left][right] = (bestval + weight, bestr)

    return


def createBSTRecur(bst, opt, left, right, keys):

    #base case
    if left == right:
        bst.insert(keys[left])
        return bst

    rindex = opt[left][right][1]
    rnum = keys[rindex]
    if bst == None:
        bst = BSTree(None)
    bst.insert(rnum)

    #Recursive calls
    if left <= rindex - 1:
        bst = createBSTRecur(bst, opt, left, rindex - 1, keys)
    if rindex + 1 <= right:
        bst = createBSTRecur(bst, opt, rindex + 1, right, keys)

    return bst


root = BSTVertex(22, None, None)
tree = BSTree(root)
tree.insert(14)
tree.insert(33)
tree.insert(2)
tree.insert(17)
tree.insert(27)
tree.insert(45)
tree.insert(47)
print ('We test lookup: let us lookup 14: ' + str(tree.lookup(14)))

print ('In order traversal')
print (tree.inOrder())

print ('get vertex root and value')
print (tree.getVertex(22), 'Value = ', tree.getVertex(22).val)
print ('left child of root is', end = ' ')
print (tree.getVertex(22).getLeftChild().getVal())

tree.insert(34)
print ('In order traversal now')
print (tree.inOrder())

keys = [1, 2, 3, 4, 5, 6, 7]
pr = [0.2, 0.1, 0.2, 0.0, 0.2, 0.1, 0.2]
optimalBST(keys, pr)

keys2 = [1, 2, 3, 4]
pr2 = [1.0/28.0, 10.0/28.0, 9.0/28.0, 8.0/28.0]
optimalBST(keys2, pr2)
