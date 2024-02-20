# Assign result
import bruteForceCheckForWin
def assignResult(game, player, gridSize):
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
        if playerwin == 0:
            return 0
        elif playerwin > 0:
            return 1
 
