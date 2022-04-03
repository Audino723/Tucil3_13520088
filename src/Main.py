import timeit

from Puzzle import *
from Node import *
from PuzzleCheck import *
from BnBAlgorithm import *
from PostProc import *

def readFromFile(fileName):
    puzzle = []
    fileName = "Test/" + fileName 
    f = open(fileName, "r")
    Lines = f.readlines()

    for line in Lines:
        #puzzle.append(line.strip().split(" "))
        puzzle.append(list(map(int, line.strip().split(" "))))

    #print(puzzle)
    #print(type(puzzle[0][0]))

    return puzzle

def main():
    filename = input("Masukkan nama file (beserta extensi.txt)   : ")
    delay = float(input("Masukkan delay dalam s penggambaran proses : "))
    progress = []
    costRank =[]
    puzzle = Puzzle(readFromFile(filename))
    
    if (isReachableGoal(puzzle)):
        # Initiate values
        firstNode = Node(puzzle, 0, len(progress), -1)
        progress.append(firstNode)
        costRank = [0]

        # Run Algorithm and Check runtime
        start = timeit.default_timer()
        target = BnBAlgorithm(progress, costRank)
        stop = timeit.default_timer()

        printProgress(progress, findMatrixProgress(progress, target), stop-start, delay)

main()