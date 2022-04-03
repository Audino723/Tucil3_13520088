from Puzzle import *
from Node import *

def addNodes(progress, node, costRank):
    count = -1
    while(count < 4):
        count+=1

        addNode = False
        depth = node.getDepth()

        tempPuzzle = Puzzle(node.getPuzzle().getModels())
        if (count == 0 and tempPuzzle.moveUp()):
            addNode = True
        if (count == 2 and tempPuzzle.moveLeft()):
            addNode = True
        if (count == 3 and tempPuzzle.moveRight()):
            addNode = True
        if (count == 1 and tempPuzzle.moveDown()):
            addNode = True
        
        if addNode:
            newNode = Node(tempPuzzle, depth+1, len(progress), node.getNode())
            #Check if node already found before
            if (isNodeFoundBefor(progress, newNode)):
                continue
            
            progress.append(newNode)

            for i, iCost in enumerate(costRank):
                if (progress[iCost].getCost() > newNode.getCost()):
                    costRank.insert(i, len(progress)-1)
                    break

                if (i == len(costRank) - 1):
                    costRank.append(len(progress)-1)
                    break               

def isNodeFoundBefor(progress, otherNode):
    isFoundBefore = False
    for node in progress:
        if (node.getCurrCost() != otherNode.getCurrCost()):
            continue
        if (node.isNodeSame(otherNode)):
            isFoundBefore = True
            break

    return isFoundBefore

def BnBAlgorithm(progress, costRank):
    iNode = 0

    while(iNode < len(progress)):
        node = progress[costRank[0]]
        # Check if node is already target
        if (node.getPuzzle().isReachGoal()):
            return node
            
        addNodes(progress, node, costRank)
        costRank.pop(0)
        
        iNode+=1
    