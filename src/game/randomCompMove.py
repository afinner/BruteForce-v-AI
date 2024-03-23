#Comp random
import random
def randomCompMove(game, gridSize):

    while True:
        r = random.randint(0,gridSize-1)
        c = random.randint(0,gridSize-1)
        #print("Computer looking at: ", game[r], c, game[r][c], "\n")
        if game[r][c] == '_':
                #print("Computer picked blank at: ", game[r], c, game[r][c], "\n")
                return (r, c)            

