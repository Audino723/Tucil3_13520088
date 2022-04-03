ROW = 4
COLUMN = 4

class Node:
    def __init__(self, puzzle, depth, node, parentNode):
        self.puzzle = puzzle
        self.cost = puzzle.taksiranCostUntilGoal() + depth
        self.currCost = puzzle.taksiranCostUntilGoal()
        self.depth = depth
        self.node = node
        self.parentNode = parentNode
    
    def isNodeSame(self, other):
        isSame = True
        models = self.puzzle.getModels()
        otherModels = other.puzzle.getModels()
        for i in range(ROW):
            for j in range(COLUMN):
                if (models[i][j] != otherModels[i][j]):
                    isSame = False
                    break

        return isSame

    def getPuzzle(self):
        return self.puzzle

    def getCost(self):
        return self.cost   

    def getCurrCost(self):
        return self.currCost 

    def getDepth(self):
        return self.depth

    def getNode(self):
        return self.node

    def getParentNode(self):
        return self.parentNode

    def printInfo(self):
        print("Cost  : ", self.cost)
        print("Depth : ", self.depth)
        print("Node  : ", self.node)
        print("Parent Node : ", self.parentNode)
        self.puzzle.printInfo()
        print()