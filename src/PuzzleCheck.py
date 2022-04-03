ROW = 4
COLUMN = 4

def fungsiKurang(puzzle):
    # CONST
    greyArea = [1, 3, 4, 6, 9, 11, 12, 14]
    arrayLen = ROW*COLUMN
    
    # Convert matriks into array
    puzzleArray  = convertPuzzleToArray(puzzle)

    kurang = 0
    X = 0

    for i in range(arrayLen):
        kurangTemp = 0

        #Check empty position
        if (puzzleArray[i] == -1) :
            if (i in greyArea):
                X = 1
            kurangTemp = arrayLen - i - 1

        else:
            for j in range(i, arrayLen):
                if (puzzleArray[j] == -1):
                    continue

                elif (j > i and puzzleArray[j] < puzzleArray[i]):
                    kurangTemp += 1

        kurang += kurangTemp
        #print("Kurang", puzzleArray[i], "=", kurangTemp)

    # Add value of X
    kurang += X
    return kurang

def convertPuzzleToArray(puzzle):
    models = puzzle.getModels()
    puzzleArray = []

    for i in range(ROW):
        for j in range(COLUMN):
            puzzleArray.append(models[i][j])

    return puzzleArray

def isReachableGoal(puzzle):
    value = fungsiKurang(puzzle)

    if (value % 2 == 0):
        print("Puzzle dapat diselesaikan")
        return True
    else:
        print("Puzzle tidak dapat diselesaikan")
        return False