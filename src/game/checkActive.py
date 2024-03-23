#check if game is active
def checkActive(game, gridSize, row, col):
  
    userValue = game[row][col]
    
    # horizontal check
    hCount = 0
    win = []
    for c in range(0,gridSize):
        if game[row][c] == userValue:
            hCount += 1
            win.append((row, c))
    if hCount == gridSize:
        return True, win
    
    # vertical
    vCount = 0
    win = []
    for r in range(0,gridSize):
        if game[r][col] == userValue:
            vCount += 1
            win.append((r,col))
    if vCount == gridSize:
        return True, win
    
    # slope == 1
    diagonalOne = (row == col)
    # slop == -1
    diagonalTwo = (row == (gridSize -1) - col)
                           
    # diagonal check
    if diagonalOne == True:
        countOne = 0
        win = []
        for i in range(0,gridSize):
            if game[i][i] == userValue:
                countOne += 1
                win.append((i, i))
        if countOne == gridSize:
            return True, win

    # diagonal check
    if diagonalTwo == True:
        Count2 = 0
        win = []
        for i in range(0,gridSize):
            if game[(gridSize - 1) - i][i] == userValue:
                Count2 += 1
                win.append(((gridSize - 1) - i,i))
        if Count2 == gridSize:
            return True, win

    return False, []
    
                      
                      
                    
                      
                      
