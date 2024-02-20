# Tic-tac-toe
import createGrid
import displayGrid
import userInput
import checkActive
import checkDraw
import compInput
import randomCompMove


def main():
    gridSize = 3

    game = createGrid.createGrid(gridSize)
    
    gameIsActive = True
    while gameIsActive == True:

        displayGrid.displayXGrid(game)
        
        # Request computer move
        row, col = randomCompMove.randomCompMove(game, gridSize)
        # print("computer move", row, col, "\n")                

        # Check the computer move
        game[row][col] = 'X'
        if checkActive.checkActive(game, gridSize, row, col) == True:
            gameIsActive = False
            print("Game is Over - X won")
            displayGrid.displayXGrid(game)
            break
        if checkDraw.checkDraw(game, gridSize) == True:
            gameIsActive = False
            print("Game is Over - draw")
            displayGrid.displayXGrid(game)
            break
        

        # Update position
        displayGrid.displayXGrid(game)

        # Request computer move
        row, col = randomCompMove.randomCompMove(game, gridSize)
        # print("computer move", row, col, "\n")                

        # Check the computer move
        game[row][col] = 'O'
        if checkActive.checkActive(game, gridSize, row, col) == True:
            gameIsActive = False
            print("Game is Over - O won")
            displayGrid.displayXGrid(game)
            break
        if checkDraw.checkDraw(game, gridSize) == True:
            gameIsActive = False
            print("Game is Over - draw")
            displayGrid.displayXGrid(game)
            break
                
#main()
