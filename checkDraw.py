# To check if all squares are full.
def checkDraw(game, gridSize):
    qtyOfBlanks = 0
    for row in game:
        qtyOfBlanks = qtyOfBlanks + row.count('_')
        
    if qtyOfBlanks == 0:
        return True
    else:
        return False
   
   

    

    
