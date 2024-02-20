import itertools
gridSize = 3
#legalPositions = []
#for i in range (0, (gridSize*gridSize) + 1, 1):
    #legalPositions.append({})


combs = list(itertools.product(["X","O","_"], repeat=gridSize))

numCombs = len(combs)
for c in range(0, numCombs**gridSize, 1):
    game = []
    for i in range (gridSize-1, -1, -1):
        game.append( combs[(c // numCombs**i) % numCombs] )
    print(game)