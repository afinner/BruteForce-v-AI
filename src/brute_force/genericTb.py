import itertools
import convertGame
import checkLegal
import bruteForceCheckForWin
import tableBaseData
import time


def bruteforceGame(gridSize, max):

    # ts_comb = time.perf_counter_ns()
    # tablebases = generateEmptyTablebases(gridSize)
    # t_comb = time.perf_counter_ns() - ts_comb
    # print("Initial combination generation time: ", t_comb // 1000)

    tablebases = []
    numTablebases = min(max, (gridSize*gridSize)+1)

    for numBlanks in range (0, numTablebases, 1):
        ts_tb = time.perf_counter_ns()

        tablebases.append(generateEmptyTablebaseN(gridSize, numBlanks))
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
        tableBaseData.outputData(tablebases[numBlanks], numBlanks, gridSize)
        t_tb = time.perf_counter_ns() - ts_tb
        print("Tablebase(N) - entries - generation time (ms): ", (gridSize*gridSize)-numBlanks, len(tablebases[numBlanks]), t_tb // 1000)    


def generateEmptyTablebases(gridSize):
    generateTime = 0
    et = 0
    sgt = time.perf_counter_ns()
    legalPositions = []
    for i in range (0, (gridSize*gridSize) + 1, 1):
        legalPositions.append({})

    combs = list(itertools.product(["X","O","_"], repeat=gridSize))

    numCombs = len(combs)
    for c in range(0, numCombs**gridSize, 1):
        game = []
        for i in range (gridSize-1, -1, -1):
            game.append( combs[(c // numCombs**i) % numCombs] )

        numBlanks = countBlanks(game)
        # check game is legal (based on blanks)
        if checkLegal.checkLegalN(game, numBlanks, gridSize) == False:
            continue

        key = convertGame.gameKey(game)
        # add game to table base
        legalPositions[numBlanks][key] = (0, 0, 0, 0)
    et = time.perf_counter()-sgt
    generateTime += et
    print("The generation time is:", generateTime)
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
    maxWinScore = 0
    win = False

    drawCoord = ()
    maxDrawScore = 0
    draw = False

    score = 0
    nextPlayer = "X"
    if ((gridSize*gridSize)-numBlanks) % 2 == 1:
        nextPlayer = "O"

    blankCoords = getBlanks(game)
    for blankCoord in blankCoords:
        game[blankCoord[0]][blankCoord[1]] = nextPlayer
        if checkWin(game, numBlanks-1, gridSize):
            return (1, 1, blankCoord[0], blankCoord[1] )

        key = convertGame.gameKey(game)
        r = prevTablebase[key][0]
        s = 1 - prevTablebase[key][1]
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
    if ((gridSize*gridSize)-numBlanks) % 2 == 0:
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
    blankCoords = []
    r = 0
    for row in game:
        c = 0
        for val in row:
            if val == '_':
                blankCoords.append( (r, c) )
            c = c + 1
        r = r + 1
    return blankCoords 

def getMove(game, tablebase):    
    numBlanks = countBlanks(game)
    key = convertGame.gameKey(game)
    result = (0, 0, 0, 0)
    t = tablebase[numBlanks]
    result = t[key]
    return result[2], result[3]

def generateEmptyTablebaseN(gridSize, numBlanks):
    tablebase = {}

    combs = list(itertools.product(["X","O","_"], repeat=gridSize))
    numCombs = len(combs)

    if numBlanks == gridSize*gridSize:
        game = []
        for r in range(gridSize):
            game.append(combs[len(combs)-1])
        key = convertGame.gameKey(game)
        tablebase[key] = (0, 0, 0, 0)
        return tablebase
    
    expectedX = (((gridSize*gridSize)-numBlanks)//2) + ((gridSize*gridSize)-numBlanks)%2
    expectedO = ((gridSize*gridSize)-numBlanks)//2

    combBlanks = []
    combXs = []
    combOs = []
    for comb in combs:
        combBlanks.append(comb.count('_'))
        combXs.append(comb.count('X'))
        combOs.append(comb.count('O'))

    # TODO based on ordering of combs, max be possible to skip past remaining combination is a row without testing each once blank limit is reached. 
    for c in range(0, numCombs**gridSize, 1):
        game = []
        blanks = 0
        xs = 0
        os = 0
        for i in range (gridSize-1, -1, -1):
            ci = (c // numCombs**i) % numCombs
            blanks += combBlanks[ci]
            xs += combXs[ci]
            os += combOs[ci]
            if (blanks > numBlanks) or (xs > expectedX) or (os > expectedO):
                break;
            comb = combs[ci]
            game.append( combs[(c // numCombs**i) % numCombs] )
        
        if (blanks != numBlanks) or (xs != expectedX) or (os != expectedO) or (len(game) < gridSize):
            continue

        if checkLegal(game, gridSize) == False:
            continue

        key = convertGame.gameKey(game)
        # add game to table base
        tablebase[key] = (0, 0, 0, 0)

    return tablebase


def checkLegal(game, gridSize):
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

