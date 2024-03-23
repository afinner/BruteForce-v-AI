# check legal
import bruteForceCheckForWin

def checkLegal(game, gridSize):
   #X-count
   # must check at least 3 x combinations
   # TODO work for 3x3 grid only as only one win is possible (i.e. X has max of 5 moves)
   # TODO adjust win check for NxN where >1 concurrent win is Ok
    win = 0
    for player in ["X", "O"]:
        playerwin = 0
        for row in game:
            if bruteForceCheckForWin.checkRow(row, player):
                playerwin += 1
                break
    
        for col in range(0, gridSize - 1):
            if bruteForceCheckForWin.checkCol(game, col, player):
                playerwin += 1
                break
         
        if bruteForceCheckForWin.eastDiagonal(game, player):
            playerwin += 1
        if bruteForceCheckForWin.westDiagonal(game, player):
            playerwin += 1

        if playerwin > 0:
            win += 1

    if win < 2:
        return True

    return False       
  
def checkQtys(game, gridSize):
    qtyOfBlanks = 0
    qtyOfX = 0
    qtyOfO = 0
    for row in game:
        qtyOfBlanks = qtyOfBlanks + row.count("_")
        qtyOfX = qtyOfX + row.count("X")
        qtyOfO = qtyOfO + row.count("O")

    if qtyOfBlanks + qtyOfX + qtyOfO != 9:
        return False

    qtyOfBlanksWanted = 0
    expectedX = (((gridSize*gridSize))//2) + ((gridSize*gridSize)- qtyOfBlanksWanted)%2
    expectedO = ((gridSize*gridSize)-qtyOfBlanksWanted)//2
    if qtyOfBlanks == qtyOfBlanksWanted and qtyOfX == expectedX and qtyOfO == expectedO:
        return True
    
    return False

def checkQtysXandO(game, blanks, gridSize):
    qtyOfX = 0
    qtyOfO = 0
    for row in game:
        qtyOfX = qtyOfX + row.count("X")
        qtyOfO = qtyOfO + row.count("O")

    expectedX = (((gridSize*gridSize)-blanks)//2) + ((gridSize*gridSize)- blanks)%2
    expectedO = ((gridSize*gridSize)-blanks)//2
    if qtyOfX == expectedX and qtyOfO == expectedO:
        return True
    
    return False

def checkLegalN(game, numBlanks, gridSize):
    # legal position if
    #   correct number of Xs and Os
    #   position is not already won
    if checkQtysXandO(game, numBlanks, gridSize) == False:
        return False
    
    for player in ["X", "O"]:
        for row in game:
            if bruteForceCheckForWin.checkRow(row, player):
                return False    
        for col in range(0, gridSize):
            if bruteForceCheckForWin.checkCol(game, col, player):
                return False
        if bruteForceCheckForWin.eastDiagonal(game, player):
                return False
        if bruteForceCheckForWin.westDiagonal(game, player):
                return False

    return True

def main():
    game = [['O', 'O', 'X'], ['O', '_', 'X'], ['_', '_', 'X']]
    print( checkLegalN(game, 3, 3) )

#main()
