#Comp Input
def compInput(game, gridSize):
    c = 0
    r = 0

    for row in game:
        c = 0
        for col in row:
            #print("Computer looking at: ", row, c, row[c], "\n")
            if row[c] == '_':
                #print("Computer picked blank at: ", row, c, row[c], "\n")
                return (r, c)            
            c = c + 1
        r = r + 1
                    
    return(-1, -1)
   
