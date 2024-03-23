def gameKey(game):
    gridSize = len(game[0])
    a = 0
    n = 0
    for row in game:
        for character in row:
            if character == '_':
                v = 0
            if character == 'X':
                v = 1
            if character == 'O':
                v = 2
            a = a + (v*gridSize**n)
            n += 1
    return a
        
def gameData(key, gridSize):
    index = 0
    game = [['_'] * gridSize for i in range(gridSize)]
    while key > 0:
        v = key % gridSize
        if v == 0:
            c = '_'
        if v == 1:
            c = 'X'
        if v == 2:
            c = 'O'
        game[index // gridSize][index % gridSize] = c
        key = key // gridSize
        index = index + 1
    return game

def main():
    # game =[['O', 'O', 'X', 'X'], ['O', '_', 'X', 'X'], ['_', '_', 'X', 'X'], ['_', '_', 'X', 'X']]
    # key = gameKey(game)
    # print(key)
    # game1 = gameData(key, 4)
    # print(game1)

    print(295.0)
    game2 = gameData(1074298969, 4)
    print(game2[0])
    print(game2[1])
    print(game2[2])
    print(game2[3])

#main()