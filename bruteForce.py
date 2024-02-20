# brute force algorithm
import checkLegal
import itertools
import bruteForceAssignResult
import convertGame
import tableBaseData

# generate positions with 0 blank squares
def bruteForce():
    player = "X"
    legalPositions = []
    gridSize = 3
    assignedPositions = []
    tablebase = {}

    # find all possible 9-piece legal positions
    row1 = list(itertools.product(["X","O"], repeat=3))
    row2 = list(itertools.product(["X","O"], repeat=3))
    row3 = list(itertools.product(["X","O"], repeat=3))
    
    for combination1 in row1:
        row1TempVal = []
        row1TempVal.extend(combination1)
        for combination2 in row2:
            row2TempVal = []
            row2TempVal.extend(combination2)
            for combination3 in row3:
                row3TempVal = []
                row3TempVal.extend(combination3)
                game = [row1TempVal, row2TempVal, row3TempVal]

                if checkLegal.checkQtys(game, gridSize):
                    if checkLegal.checkLegal(game, gridSize):
                        #print("legal")
                        legalPositions.append(game)


    for game in legalPositions:
        # calculate position key
        key = convertGame.gameKey(game)
        # calculate the result (resultfn(iteration, game, positiionKey, tablebase_N+1))
        result = bruteForceAssignResult.assignResult(game, player, gridSize)
        # add result to new tablebase
        tablebase[key] = (result, 0, 0)          

        tableBaseData.outputData(tablebase, 0)

bruteForce()

# goodInput check



# discard all illegal positions by looping check through

#def checkLegal(gridSize, checkActive):
    # cannot have a position with 2 winning combinations unless a square is shared and they are of the same "x" or "o"
    #if checkactive.checkActive == False and "X" was the last input:
        #check
    #else:
        #return legal
    

    
# find all positions where game is over
    # all positions

# assign value to every position
#def assignValuetoPositions(gridsize, checkActive):
 #   if checkActive.checkActive(game) == False
  #      assign 1


    
# generate all positions with 1 blank square
# find all postions where game is over assign value
# assign value to all move transitions
# repeat for 2, 3, 4, 5, 6, 7, and 8 blank squares
    
        
    
    
