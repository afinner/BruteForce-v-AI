#user input function
def userInput(game, gridSize):
    x = 0
    y = 0

    goodPosition = False
    while goodPosition == False:
    
        goodInput = False
        while goodInput == False:
            x = int(input("Please enter first coordinate \n"))
            if x >= 0 and x < gridSize:
                goodInput = True
            else:
                print("Coordinate is out of range: 0 to ", gridSize-1, "\n")

        goodInput = False
        while goodInput == False:
            y = int(input("Please enter second coordinate \n"))
            if y >= 0 and y < gridSize:
                goodInput = True
            else:
                print("Coordinate is out of range: 0 to ", gridSize-1, "\n")

        col = x
        row = (gridSize - 1) - y
        if game[row][col] == '_':
            goodPosition = True
        else:
            print("That square is occupied. Try again:\n")
    col = x
    row = (gridSize - 1) - y        
    return(row, col)
