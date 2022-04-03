ROW = 4
COLUMN = 4

class Puzzle:
    def __init__(self, models):
        self.models = [[-1 for _ in range(COLUMN)] for _ in range(ROW)]

        for i in range(ROW):
            for j in range(COLUMN):
                if (models[i][j] == -1):
                    emptyPos = [i, j]
                self.models[i][j] = models[i][j]
        
        self.startingEmptyPos = emptyPos
        self.emptyPos = emptyPos

    def getEmptyPos(self):
        return self.emptyPos

    def getModels(self):
        return self.models

    def moveEmptyPos(self, iEmpty, jEmpty, iTarget, jTarget):
        self.models[iEmpty][jEmpty] = self.models[iTarget][jTarget]
        self.models[iTarget][jTarget] = -1
        self.emptyPos = [iTarget, jTarget]

    def moveUp(self):
        i = self.emptyPos[0]
        j = self.emptyPos[1]

        if (i == 0):
            return False
        else:
            self.moveEmptyPos(i, j, i-1, j)
            return True

    def moveLeft(self):
        i = self.emptyPos[0]
        j = self.emptyPos[1]

        if (j == 0):
            return False
        else:
            self.moveEmptyPos(i, j, i, j-1)
            return True

    def moveRight(self):
        i = self.emptyPos[0]
        j = self.emptyPos[1]

        if (j == COLUMN-1):
            return False
        else:
            self.moveEmptyPos(i, j, i, j+1)
            return True

    def moveDown(self):
        i = self.emptyPos[0]
        j = self.emptyPos[1]

        if (i == ROW-1):
            return False
        else:
            self.moveEmptyPos(i, j, i+1, j)
            return True
    
    def taksiranCostUntilGoal(self):
        totalCost = 0

        for i in range(ROW):
            for j in range(COLUMN):
                if (self.models[i][j] == -1):
                    continue
                if (self.models[i][j] != (i*4 + j + 1)):
                    totalCost += 1
        
        return totalCost

    def isReachGoal(self):
        goalReaches = True
        count = 0

        for i in range(ROW):
            for j in range(COLUMN):
                count += 1

                if (self.models[i][j] != count and count < 16):
                    goalReaches = False

        return goalReaches

    def printInfo(self):
        print("Goal Reached: ", self.isReachGoal())
        for i in range(ROW):
            print(self.models[i])

