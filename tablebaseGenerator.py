import itertools
import convertGame
import checkLegal
import bruteForceCheckForWin
import tableBaseData


def bruteforceGame():
    gridSize = 3
    tablebases = generateEmptyTablebases(gridSize)
    for numBlanks in range (0, (gridSize*gridSize) + 1, 1):
        prevTablebase = {}
        if numBlanks > 0:
            prevTablebase = tablebases[numBlanks-1]
        for position in tablebases[numBlanks]:
            game = convertGame.gameData(position, gridSize)
            if numBlanks == 0:
                tablebases[numBlanks][position] = (0, 0.5, -1, -1)
            else:
                r = calculateNextMove(game, numBlanks, gridSize, prevTablebase)
                tablebases[numBlanks][position] = r
        tableBaseData.outputData(tablebases[numBlanks], numBlanks)


def generateEmptyTablebases(gridSize):
    legalPositions = []
    for i in range (0, (gridSize*gridSize) + 1, 1):
        legalPositions.append({})

    gridSize = 3
    row1 = list(itertools.product(["X","O","_"], repeat=gridSize))
    row2 = list(itertools.product(["X","O", "_"], repeat=gridSize))
    row3 = list(itertools.product(["X","O","_"], repeat=gridSize))

    for combination1 in row1:
        for combination2 in row2:
            for combination3 in row3:
                game = [combination1, combination2, combination3]
                numBlanks = countBlanks(game)
                # check game is legal (based on blanks)
                if checkLegal.checkLegalN(game, numBlanks, gridSize) == False:
                    continue

                key = convertGame.gameKey(game)
                # add game to table base
                legalPositions[numBlanks][key] = (0, 0, 0, 0)
    return legalPositions

def countBlanks(game):
    qtyOfBlanks = 0
    for row in game:
        qtyOfBlanks = qtyOfBlanks + row.count("_")
    return qtyOfBlanks

def calculateNextMove(game, numBlanks, gridSize, prevTablebase):
    # when using prevTablebase result is for other player so it must be flipped when
    #  interpreted to give best result for current player.
    winCoord = ()
    drawCoord = ()
    maxDrawScore = 0
    maxWinScore = 0
    win = False
    draw = False
    score = 0
    blankCoords = getBlanks(game)
    nextPlayer = "X"
    if numBlanks % 2 == 0:
        nextPlayer = "O"
    for blankCoord in blankCoords:
        game[blankCoord[0]][blankCoord[1]] = nextPlayer
        if checkWin(game, numBlanks-1, gridSize):
            return (1, 1, blankCoord[0], blankCoord[1] )

        key = convertGame.gameKey(game)
        r = prevTablebase[key][0]
        s = prevTablebase[key][1]
        if r == -1:
            win = True
            score += s
            if s >= maxWinScore:
                winCoord = blankCoord
                maxWinScore = s
        elif r == 0:
            # remember draw, but wait for better move
            draw = True
            score += s
            if s >= maxDrawScore:
                drawCoord = blankCoord
                maxDrawScore = s

        game[blankCoord[0]][blankCoord[1]] = '_'

    score = score / numBlanks

    if win:
        return (1, score, winCoord[0], winCoord[1] )

    if draw:
        return (0, score, drawCoord[0], drawCoord[1] )

    return (-1, score, blankCoords[0][0], blankCoords[0][1])

def checkWin(game, numBlanks, gridSize):
    lastPlayer = "X"
    if numBlanks % 2 == 1:
        lastPlayer = "O"
    for row in game:
        if bruteForceCheckForWin.checkRow(row, lastPlayer):
            return True
    for col in range(0, gridSize):
        if bruteForceCheckForWin.checkCol(game, col, lastPlayer):
            return True
    if bruteForceCheckForWin.eastDiagonal(game, lastPlayer):
        return True
    if bruteForceCheckForWin.westDiagonal(game, lastPlayer):
        return True
    return False

def getBlanks(game):
    blanks = []
    x = 0
    for row in game:
        y = 0
        for v in row:
            if v == '_':
                blanks.append( (x, y) )
            y = y + 1
        x = x + 1
    #print(blanks)
    # Only prints lists with 1 blanks
    return blanks 

def getMove(game, tablebase):    
    numBlanks = countBlanks(game)
    key = convertGame.gameKey(game)
    result = (0, 0, 0, 0)
    t = tablebase[numBlanks]
    result = t[key]

    return result[2], result[3]

bruteforceGame()
