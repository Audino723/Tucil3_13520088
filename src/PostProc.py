import time
# Post Proccessing after solving the puzzle

def findMatrixProgress(progress, target):

    progressMatrix = [-1]
    tempNode = target

    while(True):
        currNode = tempNode.getNode()
        parentNode = tempNode.getParentNode()

        progressMatrix.insert(0, currNode)

        # Get Parent Node
        if (parentNode == -1):
            break
        else:
            tempNode = progress[parentNode]
    
    # Delete initial values
    progressMatrix.pop()
    print("Progress Matrix : ", progressMatrix)

    return progressMatrix

def printProgress(progress, progressMatrix, runTime, delay):
    print("Progress\n")
    
    for i in progressMatrix:
        time.sleep(delay)
        progress[i].printInfo()

    print("Total runtime:", runTime*1000, "ms")
    print("Total Node Generated", len(progress))
